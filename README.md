# DPS-Planning-2526

![alt text](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSm6QwtUnefiWRafxJEMVU0DHZuwVuumvxCsA&s)

Collaborators: [Leah Wallihan](https://github.com/LtheWall00), [Oliver Lublin](https://github.com/olublin), [Kevan Wang](https://github.com/KevanWang05)

Advised by Vitaly Radsky and Cameron Moore

---
## Construct Distance Matrix

The `get_distances.py` file constructs a **851 by 851 distance matrix** giving the driving distance between each of the planning units. The `get_distances.py` file requires a single file input:

**Input File:**

- `pu_split_start_0.geojson`

This file gives the geometry of all 851 planning units, with an index column `pu_2324_84` that matches the dataframe index and a geometry column `geometry` that gives the geometry of each planning unit. The outputs should be named as following:

**Output Files:**

- `dist_matrix_0_9.csv`

- `dist_matrix_10_19.csv`

...

- `dist_matrix_840_849.csv`

- `dist_matrix_850_850.csv`

The intervals can differ, as the arguments `lower_bound`, `upper_bound`, and `interval` can be set by the user on line 98.

Dependencies, details and more information about running the `get_distances.py` script can be found in the `Distance-Matrix` folder.

---
## Preprocess Matrix for Model

The matrix processing file `construct_matrix.py` takes as an argument a zip file containing the batched distance matrices. At the moment, this zipfile must be constructed by the user. The only argument for the `construct_matrix.py` file is this zipfile, called in the buildMatrix call on line 56. This zipfile can be named whatever as long as the argument on line 56 is changed. 

**Input File:**

- `isochron_results.zip` (or anything)

The script unpacks the zip file, sorts the files by name (which will correctly sort the planning units in sequential order if the names of the individual `.csv` files match the format described in the `Distance-Matrix` README). The script then processes the matrix, as described in more depth in the 'Distance-Matrix' README, to produce a full approximate driving distance matrix for all 851 planning units. Note: if the files were batched incorrectly in the previous section such that there are less than or fewer than 851 columns in all of the zipfile, an error will be thrown. A `.csv` file containing the full 851 by 851 distance matrix will be outputted as the following:

**Output File:**

- `dist_matrix_final.csv`

Dependencies, details and more information about running the `get_distances.py` script can be found in the `Distance-Matrix` folder.

