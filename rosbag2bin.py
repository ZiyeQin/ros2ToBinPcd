import os
import csv
import numpy as np
import rosbag2_py
from sensor_msgs.msg import PointCloud2
from sensor_msgs_py import point_cloud2 as pc2
from rclpy.serialization import deserialize_message
from datetime import datetime

def pointcloud_to_kitti(pc):
    points_list = []
    for point in pc2.read_points(pc, field_names=("x", "y", "z", "intensity"), skip_nans=True):
        points_list.append([point[0], point[1], point[2], point[3]])
        
    return np.array(points_list)

def save_kitti_file(points, filename):
    points = np.array(points, dtype=np.float32)
    points.tofile(filename)


def main():
    bag_path = '/home/mybag'
    output_dir = '/home/ponitcloudsOutput'
    os.makedirs(output_dir, exist_ok=True)

    csv_file = open(os.path.join(output_dir, 'timestamps.csv'), mode='w', newline='')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['filename', 'utc_timestamp'])

    reader = rosbag2_py.SequentialReader()
    storage_options = rosbag2_py.StorageOptions(uri=bag_path, storage_id='sqlite3')
    converter_options = rosbag2_py.ConverterOptions(input_serialization_format='cdr', output_serialization_format='cdr')
    reader.open(storage_options, converter_options)

    topic_types = reader.get_all_topics_and_types()
    type_dict = {topic.name: topic.type for topic in topic_types}

    while reader.has_next():
        (topic, data, t) = reader.read_next()
        if topic == '/ouster/points':
            msg = deserialize_message(data, PointCloud2)
            timestamp = t / 1e9  # Convert from nanoseconds to seconds
            utc_timestamp = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            filename = f"{int(timestamp * 1e6)}.bin"
            filepath = os.path.join(output_dir, filename)

            points = pointcloud_to_kitti(msg)
            save_kitti_file(points, filepath)

            csv_writer.writerow([filename, utc_timestamp])

    csv_file.close()

if __name__ == '__main__':
    main()



