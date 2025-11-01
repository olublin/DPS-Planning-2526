# Distance Matrix Details and Methodology

The distance matrix folder contains two scripts, 'get_distances.py' for processing driving distances using isochrone branching courtesy of the openrouteservice API, and 'construct_matrix.py' for preprocessing the distances matrix to be used in the CFLP model.

---
## Construct Distance Matrix

### Purpose:

**Construct a realistic and accurate distance matrix between all 851 DPS planning units based on driving time**. Previous versions of this model used the built in .distance function in GeoPandas to compute a planning-unit-wide distance matrix. We aim to further refine our model by including real-life approximate driving times using the method of **isochrone branching** to get accurate driving times between planning units (more realistic than previous cartesian distances).

### Requirements:

This script uses the **openroutesource** library to compute driving isochrones. A basic plan can be made at [openrouteservice.com](openrouteservice.com). We ***strongly recommend*** requesting an upgraded plan, which can be granted for free for academic purposes. While the basic plan offers a quota of 500 isochrones/day and 20 isochrones/second, the upgraded plan quota includes 2500 isochrones/day and 40 isochrones/second. If the quota is maxed out each day, the basic plan can complete 20 planning units per day, versus 100 per day for the upgraded plan. For all 851 planning units, this makes a significance difference of over a month (9 days vs 43 days). A personal API key is required to run the script.

### Input File:

The input file is available in the `data` folder of the repository, and is named `pu_split_start_0`. This file contains the following necessary attributes:

- `pu_2324_84`: Unique planning unit ID ranging from 0 to 850. Matches dataframe index. Indexing for the return matrix is based on the indexing in this dataframe.
- `geometry`: Polygon geometry for each planning unit.

### Parameters:

Since the isochrone quota limits the number of planning units that can be computed per day, it is required to batch the matrix. For the purpose of customizing the batching, the script accepts the following parameters:

- `lower_bound`: Lower bound of planning unit index.
- `upper_bound`: Upper bound of planning unit index (noninclusive).
- `interval`: Interval between lower end of batch and upper end of batch. We recommend using the preset interval of 10, which will result in the output files (see *Output File(s)*) being batched in intervals of 10 as shown. The API is prone to breaking at times, so an interval of 10 is optimal to ensure progress is not lost.

For example, running the script with a `lower_bound` of 0, an `upper_bound` of 100, and an `interval` of 10 will result in output files giving the distance from planning units 0 to 99 to all 851 planning units according to the methodology in the following section, and the output will be 10 files batched with 10 planning units each. Since each planning unit requires 25 isochrones to make the full distance array, 100 planning units can be run per day under the upgraded openrouteservice plan. On following days, the process can be iterated up to planning unit 850 (Note: for the last planning unit, the interval will need to be changed to 1, since there are 851 total planning units.)

Running the `get_distances.py` file 100 planning units at a time is expected to take roughly **3 hours**. As such, we recommend using a compute cluster to run the script remotely.

### Assumptions:



### Output File(s):

The `get_distances.py` script batches the matrix in 10 planning units at a time, and the output files should be named as following (intervals can also be increased as preferred considering daily quota allowed by your current plan):

`dist_matrix_0_9.csv`

`dist_matrix_10_19.csv`

...

`dist_matrix_840_849.csv`

`dist_matrix_850_850.csv`

The additional single planning unit file at the end is due to there being 851 planning units in total. The script will need to be adjusted slightly to obtain the final file.

// Zip files together

---

## Preprocess Matrix for Model
