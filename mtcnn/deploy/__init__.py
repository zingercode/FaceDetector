import os
import numpy as np
import mtcnn.network.mtcnn_pytorch as mtcnn_pytorch


def get_net(weight_folder=None):
    """
    Create pnet, rnet, onet for detector.
    """

    pnet = mtcnn_pytorch.PNet()
    rnet = mtcnn_pytorch.RNet()
    onet = mtcnn_pytorch.ONet()

    if weight_folder is not None:
        pnet.load(os.path.join(weight_folder, 'pnet'))
        rnet.load(os.path.join(weight_folder, 'rnet'))
        onet.load(os.path.join(weight_folder, 'onet'))

    return pnet, rnet, onet


def get_net_caffe(weight_folder):
    """
    Create pnet, rnet, onet for detector. And init weights with caffe model from original mtcnn repo.
    """
    pnet, rnet, onet = get_net()
    pnet.load_caffe_model(
        np.load(os.path.join(weight_folder, 'pnet.npy'), allow_pickle=True)[()])
    rnet.load_caffe_model(
        np.load(os.path.join(weight_folder, 'rnet.npy'), allow_pickle=True)[()])
    onet.load_caffe_model(
        np.load(os.path.join(weight_folder, 'onet.npy'), allow_pickle=True)[()])

    return pnet, rnet, onet
