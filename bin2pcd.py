import os
import numpy as np
import open3d as o3d

def bin_to_pcd(bin_file, pcd_file):
    """Converts .bin file to .pcd file."""
    points = np.fromfile(bin_file, dtype=np.float32).reshape(-1, 4)

    # Extract intensity values
    intensity = points[:, 3]

    # Normalize intensity to [0, 1]
    intensity_normalized = intensity / np.max(intensity)

    # Create Open3D point cloud
    pc = o3d.geometry.PointCloud()
    pc.points = o3d.utility.Vector3dVector(points[:, :3])  # X, Y, Z coordinates
    pc.colors = o3d.utility.Vector3dVector(np.stack((intensity_normalized, intensity_normalized, intensity_normalized), axis=-1))

    # Save the point cloud to a .pcd file
    o3d.io.write_point_cloud(pcd_file, pc)

def convert_all_bin_in_directory(bin_dir, pcd_dir):
    """Converts all .bin files in a directory to .pcd files."""
    if not os.path.exists(pcd_dir):
        os.makedirs(pcd_dir)

    for bin_file in os.listdir(bin_dir):
        if bin_file.endswith('.bin'):
            bin_path = os.path.join(bin_dir, bin_file)
            pcd_file = os.path.splitext(bin_file)[0] + '.pcd'
            pcd_path = os.path.join(pcd_dir, pcd_file)
            bin_to_pcd(bin_path, pcd_path)
            print(f"Converted {bin_file} to {pcd_file}")

# Example
bin_dir = '/home/ziye/ZiyeApp/CooperDetProject/UCRDaRLi/PcdData'  # e.g. '/home/bin_files/'
pcd_dir = '/home/ziye/ZiyeApp/CooperDetProject/UCRDaRLi/LidarPcd'  # e.g. '/home/pcd_files/'
convert_all_bin_in_directory(bin_dir, pcd_dir)








