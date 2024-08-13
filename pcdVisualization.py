import open3d as o3d

def visualize_pcd(pcd_file):
    """Loads and visualizes a .pcd file."""
    # Load the point cloud
    pc = o3d.io.read_point_cloud(pcd_file)

    # Visualize the point cloud
    o3d.visualization.draw_geometries([pc])

# Example usage
pcd_file = 'YOUR_PCD_FILE_PATH'  # e.g. '/home/pcd_files/000014.pcd'
visualize_pcd(pcd_file)
