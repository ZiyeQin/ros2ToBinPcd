import numpy as np
import matplotlib.pyplot as plt

def read_bin_file(filename):
    """Reads .bin file and returns numpy array of points."""
    
    points = np.fromfile(filename, dtype=np.float32).reshape(-1, 4)
    return points

def visualize_point_cloud(points):
    """Visualizes point cloud data."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], s=1)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

if __name__ == '__main__':
    filename = 'YOUR_BIN_FILE_PATH' # e.g. '/home/000014.bin'
    points = read_bin_file(filename)
    visualize_point_cloud(points)
