from utils import open_file
import numpy as np

# CUSTOM_DATASETS_CONFIG = {
#          'DFC2018_HSI': {
#             'img': '2018_IEEE_GRSS_DFC_HSI_TR.HDR',
#             'gt': '2018_IEEE_GRSS_DFC_GT_TR.tif',
#             'download': False,
#             'loader': lambda folder: dfc2018_loader(folder)
#             }
#     }
#
#
# def dfc2018_loader(folder):
#         img = open_file(folder + '2018_IEEE_GRSS_DFC_HSI_TR.HDR')[:,:,:-2]
#         gt = open_file(folder + '2018_IEEE_GRSS_DFC_GT_TR.tif')
#         gt = gt.astype('uint8')
#
#         rgb_bands = (47, 31, 15)
#
#         label_values = ["Unclassified",
#                         "Healthy grass",
#                         "Stressed grass",
#                         "Artificial turf",
#                         "Evergreen trees",
#                         "Deciduous trees",
#                         "Bare earth",
#                         "Water",
#                         "Residential buildings",
#                         "Non-residential buildings",
#                         "Roads",
#                         "Sidewalks",
#                         "Crosswalks",
#                         "Major thoroughfares",
#                         "Highways",
#                         "Railways",
#                         "Paved parking lots",
#                         "Unpaved parking lots",
#                         "Cars",
#                         "Trains",
#                         "Stadium seats"]
#         ignored_labels = [0]
#         palette = None
#         return img, gt, rgb_bands, ignored_labels, label_values, palette

CUSTOM_DATASETS_CONFIG = {
         'DFC2018_HSI': {
            'img': '2018_IEEE_GRSS_DFC_HSI_TR.HDR',
            'gt': '2018_IEEE_GRSS_DFC_GT_TR.tif',
            'download': False,
            'loader': lambda folder: dfc2018_loader(folder)
            }
    }


def dfc2018_loader(folder):
        img = open_file(folder + '2018_IEEE_GRSS_DFC_HSI_TR.HDR')[:,:,:-2]
        gt = open_file(folder + '2018_IEEE_GRSS_DFC_GT_TR.tif')
        gt = gt.astype('uint8')

        rgb_bands = (70, 53, 19)

        label_values = ["rice1",
                        "rice2",
                        "rice3",
                        "rice4"]
        ignored_labels = [0]
        palette = None
        return img, gt, rgb_bands, ignored_labels, label_values, palette

# img = open_file("/data/code/Hyperspectral-Classification/Datasets/rice/rice.mat")
# label = open_file("/data/code/Hyperspectral-Classification/Datasets/rice/rice_gt.mat")
#
# print(img)
# print(img["rice"].shape)  # (842, 704, 204)
# print(label['rice_label'].shape)  # (842, 704)
#
#
# img2 = open_file("/data/code/Hyperspectral-Classification/Datasets/PaviaU/PaviaU.mat")
# label2 = open_file("/data/code/Hyperspectral-Classification/Datasets/PaviaU/PaviaU_gt.mat")
#
# print(img2["paviaU"].shape)  # (610, 340, 103)
# print(label2["paviaU_gt"].shape)  # (610, 340)
#
# img3 = open_file("/data/code/Hyperspectral-Classification/Datasets/KSC/KSC.mat")
# label3 = open_file("/data/code/Hyperspectral-Classification/Datasets/KSC/KSC_gt.mat")
#
# print(img3["KSC"].shape)  # (512, 614, 176)
# print(label3["KSC_gt"].shape)  # (512, 614)
#
# img4 = open_file("/data/code/Hyperspectral-Classification/Datasets/IndianPines/Indian_pines_corrected.mat")["indian_pines_corrected"]
# label3 = open_file("/data/code/Hyperspectral-Classification/Datasets/IndianPines/Indian_pines_gt.mat")["indian_pines_gt"]
# print(img3.shape)  # (145, 145, 200)
# print(label3.shape)  # (145, 145)