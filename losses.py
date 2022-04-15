import torch
import pytorch3d.loss

# define losses
def voxel_loss(voxel_src, voxel_tgt):
  loss = torch.nn.BCEWithLogitsLoss()
  prob_loss = loss(voxel_src, voxel_tgt)
  return prob_loss
	
def chamfer_loss(point_cloud_src,point_cloud_tgt):
  # implement chamfer loss from scratch
  p1_dists, p1_idx, p1_nn = pytorch3d.ops.knn_points(point_cloud_src, point_cloud_tgt, lengths1=None, lengths2=None, K=1, return_nn=True)
  p2_dists, p2_idx, p2_nn = pytorch3d.ops.knn_points(point_cloud_tgt, point_cloud_src, lengths1=None, lengths2=None, K=1, return_nn=True)
  loss_chamfer = torch.sum(p1_dists) + torch.sum(p2_dists)
  return loss_chamfer
  

def smoothness_loss(mesh_src):
  # implement laplacian smoothening loss
	loss_laplacian = pytorch3d.loss.mesh_laplacian_smoothing(mesh_src)
	return loss_laplacian