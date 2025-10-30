# DPS-Planning-2526
Collaborators: Leah Wallihan, Oliver Lublin, Kevan Wang
Advised by Vitaly Radsky and Cameron Moore

---
## Construct Distance Matrix

The get_distances.py file constructs a 851 by 851 distance matrix giving the driving distance between each of the planning units. The get_distances.py file requires a single file input:

- pu_split_start_0.geojson: This file gives the geometry of all 851 planning units, with an index column "pu_2324_84" that matches the dataframe index and a geometry column "geometry" that gives the geometry of each planning unit.

