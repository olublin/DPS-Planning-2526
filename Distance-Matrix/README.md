# Distance Matrix Details and Methodology

The distance matrix folder contains two scripts, 'get_distances.py' for processing driving distances using isochrone branching courtesy of the openrouteservice API, and 'construct_matrix.py' for preprocessing the distances matrix to be used in the CFLP model.

---
## Construct Distance Matrix

### Dependencies:


The get_distances.py script batches the matrix in 10 planning units at a time, and the output files should be named as following (intervals can also be increased as preferred considering daily quota allowed by your current plan):

dist_matrix_0_9.csv

dist_matrix_10_19.csv

...

dist_matrix_840_849.csv

dist_matrix_850_850.csv

The additional single planning unit file at the end is due to there being 851 planning units in total. The script will need to be adjusted slightly to obtain the final file.

---

## Preprocess Matrix for Model
