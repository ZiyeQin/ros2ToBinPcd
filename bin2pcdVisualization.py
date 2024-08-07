import numpy as np
import open3d as o3d

def bin_to_pcd(bin_file, pcd_file):
    """Converts .bin file to .pcd file and visualizes the point cloud."""
    points = np.fromfile(bin_file, dtype=np.float32).reshape(-1, 4)

    # Extract intensity values
    intensity = points[:, 3]

    # Normalize intensity to [0, 1]
    intensity_normalized = intensity / np.max(intensity)

    # Create Open3D point cloud
    pc = o3d.geometry.PointCloud()
    pc.points = o3d.utility.Vector3dVector(points[:, :3])  # X, Y, Z coordinates
    pc.colors = o3d.utility.Vector3dVector(np.stack((intensity_normalized, intensity_normalized, intensity_normalized), axis=-1))

    # Visualize point cloud
    o3d.visualization.draw_geometries([pc])




# Example
bin_file = 'YOUR_BIN_FILE_PATH' # e.g. '/home/000014.bin'
pcd_file = 'output.pcd'
pcd = bin_to_pcd(bin_file, pcd_file)







