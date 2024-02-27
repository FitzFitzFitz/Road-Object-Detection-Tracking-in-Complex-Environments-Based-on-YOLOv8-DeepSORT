# Road-Object-Detection-Tracking-in-Complex-Environments-Based-on-YOLOv8-DeepSORT

## Abstract
This project focuses on advancing multi-object tracking (MOT) techniques, crucial for autonomous driving and other applications, especially in challenging urban scenes. By enhancing target detection and tracking algorithms, we aim to improve MOT's performance and robustness significantly.

## Introduction
Multi-object tracking in complex environments faces numerous challenges. This work reviews existing technologies in MOT, emphasizing target detection algorithms, and proposes improvements. We specifically explore the advancements in YOLOv8, including its network structure, loss function, and data augmentation techniques, and how these enhancements can be leveraged for better detection results.

## Methodology
Our approach involves fine-tuning a model based on YOLOv8 tailored to our specific dataset requirements. We also improve the Re-ID model in DeepSORT by adopting a convolutional neural network with a local maximum pooling neural network (LMBN), enhancing feature extraction and target matching. The proposed DeepOC-SORT algorithm combines these advancements with Kalman filtering, observation center re-update, and momentum techniques for increased robustness.

## Results
Testing on the MOT17 dataset demonstrated notable improvements: a 4.6% increase in the HOTA index and a 5% overall performance boost. Additionally, the frame rate on test videos rose by 18.7%, exceeding 40 frames per second, meeting real-time video analysis requirements. The algorithm's robustness in adverse conditions, such as rain or densely populated scenes, was also confirmed.

## Keywords
Multi-object Tracking, DeepSORT, YOLOv8


## Contact
fitzfitzfitz.xia@gmail.com
