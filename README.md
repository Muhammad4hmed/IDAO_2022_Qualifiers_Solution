# IDAO 2022 Qualifiers Solution

## Track 1
* ### To generate our submission
  Please run the `inference.ipynb` notebook from top to bottom

* ### To make everything from scratch
  Run the `data-split-5-folds.ipynb` notebook and it will generate `IDAO_Data_Folds.csv`
  Run the `train_fold0.ipynb train_fold1.ipynb train_fold2.ipynb train_fold3.ipynb train_fold4.ipynb` notebooks and each of them is going to take ALOT of time to train. Once the weights are generated, copy them to `Efermi_MP_2019_Weights` folder.
  Please note that, YOU MUST SAVE THE FOLLOWING WEIGHTS WHILE TRAINING
  ```
  'Efermi_MP_2019_Weights/val_mae_00011_0.009874_fold0.hdf5',
  'Efermi_MP_2019_Weights/val_mae_00025_0.005614_fold1.hdf5',
  'Efermi_MP_2019_Weights/val_mae_00013_0.007578_fold2.hdf5',
  'Efermi_MP_2019_Weights/val_mae_00016_0.007441_fold3.hdf5',
  'Efermi_MP_2019_Weights/val_mae_00007_0.007703_fold4.hdf5',
  'Efermi_MP_2019_Weights/val_mae_00007_0.010768_fold0.hdf5',
  'Efermi_MP_2019_Weights/val_mae_00023_0.005869_fold1.hdf5',
  'Efermi_MP_2019_Weights/val_mae_00014_0.008344_fold2.hdf5',
  'Efermi_MP_2019_Weights/val_mae_00019_0.007814_fold3.hdf5',
  'Efermi_MP_2019_Weights/val_mae_00007_0.008662_fold4.hdf5'
  ```
  We trained them in parts so you must keep close eye on the MAE errors
  Once its trained, run the `inference.ipynb` 


## Track 2
  Simply submit the `track2.zip` to reproduce our submission
  
  
 Please open an issue if you face any error...
