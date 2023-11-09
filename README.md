# Depth Estimation Extended Essay - CS
Completed as part of my IB Diploma, during the November 2023 session.

**The majority of the code used in the EE is from:** \
https://github.com/savnani5/Depth-Estimation-using-Stereovision \
https://github.com/magicleap/SuperPointPretrainedNetwork

**NOTE - The extended essay only makes up ~25 pages of the actual document. It was a requirement for the code used to be placed at the end in the Appendices, as well as any pertinent results of the code itself.**

# Datasets
The **'Berlin'** Evaluation and Training dataset from the **Cityscapes Dataset** were used for the 'experimental procedure'. \
\
This can be found at: https://www.cityscapes-dataset.com/downloads/ \
The following files were downloaded: \
leftImg8bit_trainvaltest.zip, rightImg8bit_trainvaltest.zip, and disparity_trainvaltest.zip

# Results
Mean Absolute Error            |  Root Mean Square Error
:-------------------------:|:-------------------------:
<img width="500" alt="MAE Graph" src="https://github.com/Johno0nt/IBCS_EE_depthEstTask/blob/main/Git Images/MAE.png?raw=true"> |  <img width="500" alt="RMSE Graph" src="https://github.com/Johno0nt/IBCS_EE_depthEstTask/blob/main/Git Images/RMSE.png?raw=true">
**Structural Similiarity Index**            |  **Run-Time Graph**
<img width="500" alt="SSIM Graph" src="https://github.com/Johno0nt/IBCS_EE_depthEstTask/blob/main/Git Images/SSIM.png?raw=true">  |  <img width="500" alt="Runtime Graph" src="https://github.com/Johno0nt/IBCS_EE_depthEstTask/blob/main/Git Images/Complexity.png?raw=true">
