# IDAO 2022 Qualifiers Solution

# Result
![](https://i.ibb.co/Pt0TJkz/Screenshot-2022-03-18-at-20-46-36-Results-IDAO-International-Data-Analysis-Olympiad.png)


# Problem Statement
![](https://i.ibb.co/RzWkkmN/image.png)

Two-dimensional transition metal dichalcogenides (TMDCs) are relatively new types of materials that have remarkable properties ranging from semiconducting, metallic, magnetic, superconducting to optical. The chemical composition of TMDCs is MX₂; where M is the group of transition elements most popular Molybdenum and Tungsten, and X is usually Sulfur or Selenium. Atomically thin TMDCs usually contain various defects, which enrich the lattice structure and give rise to many intriguing properties. Engineered point defects in two-dimensional (2D) materials offer an attractive platform for solid-state devices that exploit tailored optoelectronic, quantum emission, and resistive properties. Naturally occurring defects are also unavoidably important contributors to material properties and performance. The immense variety and complexity of possible defects make it challenging to experimentally control, probe, or understand atomic-scale defect-property relationships. In the figure above you can find vacancy and substitution defects in an 8x8 MoS₂ crystal lattice.


Band gap is one of the important physical attributes which describe certain characteristics of the material, that helps deriving material qualities including electric conductivity or catalytic power or photo-optical properties. Band gap is the energy difference between the valence band and conduction band and is closely related to the energy difference between highest occupied molecular orbital (HOMO) and lowest unoccupied molecular orbital (LUMO), materials with overlapping (between valence band and conduction band) or very small band gap are conductors and materials with small bandgap are semiconductors while materials with large bandgap are insulators.

## Objective 
The task is to predict band gap energy for each crystal structure.

## Data
The training dataset is in the `data` directory in the baseline and structured into a directory called `structures` containing 2967 crystal structures as a json file named with a unique identifier and is containing a special pymatgen structure (check pymatgen documentation for [reference](https://pymatgen.org/index.html)), that contains information about crystal parameters, cartesian coordinates of each atom, atom types, and other information. The targets are stored in a csv file named targets.csv containing two columns; the first is the unique identifier of the structure and the other is the band gap value for each structure. The train and test sets are constructed by sampling the corresponding subset without replacement.

## Quality Metric
Energy within Threshold (EwT) is designed to measure the practical usefulness of a model for replacing [DFT](https://en.wikipedia.org/wiki/Density_functional_theory) by evaluating whether the predicted energy is close to the ground truth (DFT energy). EwT is defined as the fraction of structures in which the predicted energy is within ε = 0.02 eV ([electronvolt](https://en.wikipedia.org/wiki/Electronvolt)) of the ground truth energy. 


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
