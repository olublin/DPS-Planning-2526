# DPS-Planning-2526
Collaborators: Leah Wallihan, Oliver Lublin, Kevan Wang

Advised by Vitaly Radsky and Cameron Moore

---
## Construct Distance Matrix

The get_distances.py file constructs a 851 by 851 distance matrix giving the driving distance between each of the planning units. The get_distances.py file requires a single file input:

- pu_split_start_0.geojson: This file gives the geometry of all 851 planning units, with an index column "pu_2324_84" that matches the dataframe index and a geometry column "geometry" that gives the geometry of each planning unit.

The get_distances.py script batches the matrix in 10 planning units at a time, and the output files should be named as following:

dist_matrix_0_9.csv

dist_matrix_10_19.csv

...

dist_matrix_840_849.csv

dist_matrix_850_850.csv

The additional single planning unit file at the end is due to there being 851 planning units in total. The script will need to be adjusted slightly to obtain the final file.

After running the get_distances.py file in batches for all planning units, compress all files in a .zip format to use as the input to the next script:

---
## Preprocess Matrix for Model

