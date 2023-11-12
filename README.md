# Depth Estimation Extended Essay - CS
**Research Question:** How do the ORB and SuperPoint feature-extracting algorithms compare in terms of accuracy and computational efficiency in stereo block-matching depth estimation?

Completed as part of my IB Diploma, during the November 2023 session. \
This essay looked at comparing traditional feature-extractors in ORB (Orientated FAST and Rotated BRIEF) and deep-learning feature-extractors in SuperPoint with an image rectification task alongside a depth estimation application. Essentially, key-points from each image sensor were determined with the 8-Point algorithm being used for each frame in the rectification process. From these rectified frames, the disparity maps were then computed which were evaluated against a ground-truth map alongside the run-time.


**The majority of the code used is from:** \
https://github.com/savnani5/Depth-Estimation-using-Stereovision \
https://github.com/magicleap/SuperPointPretrainedNetwork

**NOTE - The extended essay only makes up ~25 pages of the actual document. It was a requirement for the code used to be placed at the end in the Appendices, as well as any pertinent results of the code itself.**
### Image Rectification from Matching Features (Eight-Point Algorithm) ###
<img width="1000" alt="Left and Right Images Across a Common Image Plane" src="https://github.com/Johno0nt/IBCS_EE_depthEstTask/blob/main/Git Images/leftAndRightRectif.png?raw=true">

### SGBM Disparity Map with WLS Filtering ###
<img width="500" alt="Disparity Map" src="https://github.com/Johno0nt/IBCS_EE_depthEstTask/blob/main/Git Images/disparity_filtered.png?raw=true">

# Dependencies
* OpenCV Python
* PyTorch
* NumPy
* Matplotlib

These can be installed via:
```
pip install opencv-python
pip install torch
pip install numpy
pip install matplotlib
```

or with any other Python package manager e.g. Anaconda.

# Datasets
The **'Berlin'** evaluation and training dataset from the **Cityscapes Dataset** were used for the 'experimental procedure'. \
This can be found at: https://www.cityscapes-dataset.com/downloads/ \
\
**Specific Files Needed:**
* leftImg8bit_trainvaltest.zip
* rightImg8bit_trainvaltest.zip
* disparity_trainvaltest.zip

# Results
Mean Absolute Error            |  Root Mean Square Error
:-------------------------:|:-------------------------:
<img width="500" alt="MAE Graph" src="https://github.com/Johno0nt/IBCS_EE_depthEstTask/blob/main/Git Images/MAE.png?raw=true"> |  <img width="500" alt="RMSE Graph" src="https://github.com/Johno0nt/IBCS_EE_depthEstTask/blob/main/Git Images/RMSE.png?raw=true">
**Structural Similiarity Index**            |  **Run-Time Graph**
<img width="500" alt="SSIM Graph" src="https://github.com/Johno0nt/IBCS_EE_depthEstTask/blob/main/Git Images/SSIM.png?raw=true">  |  <img width="500" alt="Runtime Graph" src="https://github.com/Johno0nt/IBCS_EE_depthEstTask/blob/main/Git Images/Complexity.png?raw=true">
