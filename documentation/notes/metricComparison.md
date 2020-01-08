# Metric Comparison

The below shows 4 app signatures for the top 80 apps normalised over the global average usage of that specific app (rounded to 2 decimal places). Different similarity metrics are then run on these app signatures to provide a distance or similarity measure between each, the results are shown below.


### User 2
0.00	0.0	0.26	0.00	0.00	0.0	0.00	0.16	0.0	0.05	0.00	0.09	0.00	0.01	0.0	0.00	0.07	0.36	0.10	0.00	0.13	0.90	0.00	0.08	0.0	0.21	0.00	0.0	0.29	0.00	0.13	0.00	0.00	2.31	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.0	0.0	0.03	0.00	0.00	0.0	0.0	0.00	0.00	0.00	0.0	0.00	0.04	0.0	0.0	0.0	0.00	0.07	0.00	0.0	0.00	0.00	0.00	0.15	0.00	0.00	0.00	0.00	0.00	0.0	0.0	0.0	0.00	0.0	0.00	0.00

### User 4
0.00	0.0	0.00	0.00	0.00	0.0	0.00	0.00	0.0	0.00	0.00	0.00	0.00	0.01	0.0	0.00	0.03	0.00	0.00	0.02	0.02	0.00	0.00	0.02	0.0	0.00	0.00	0.0	0.03	0.00	0.00	0.00	0.08	0.00	0.01	0.00	0.04	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.0	0.0	0.00	0.00	0.00	0.0	0.0	0.00	0.00	0.00	0.0	0.00	0.00	0.0	0.0	0.0	0.00	0.00	0.00	0.0	0.00	0.00	0.00	1.65	0.00	0.00	0.00	0.00	0.00	0.0	0.0	0.0	0.00	0.0	0.00	0.00


### User 7
0.00	0.0	0.05	0.00	0.00	0.0	0.00	0.00	0.0	0.00	0.00	0.00	0.00	0.00	0.0	0.00	0.00	0.01	0.00	0.00	0.00	0.00	0.00	0.00	0.0	0.00	0.00	0.0	0.01	0.00	0.00	0.00	0.00	0.37	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.0	0.0	0.00	0.00	0.00	0.0	0.0	0.00	0.00	0.00	0.0	0.00	0.00	0.0	0.0	0.0	0.00	0.00	0.00	0.0	0.00	0.00	0.00	0.15	0.00	0.00	0.00	0.00	0.00	0.0	0.0	0.0	0.00	0.0	0.00	0.00


### User 10
0.00	0.0	0.00	0.00	0.00	0.0	0.00	0.00	0.0	0.00	0.00	0.00	0.00	0.00	0.0	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.0	0.00	0.00	0.0	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.0	0.0	0.00	0.00	0.00	0.0	0.0	0.00	0.00	0.00	0.0	0.00	0.00	0.0	0.0	0.0	0.00	0.00	0.00	0.0	0.00	0.00	0.00	0.15	0.00	0.00	0.00	0.00	0.00	0.0	0.0	0.0	0.00	0.0	0.00	0.00


## Visual Comparisons
2 and 4 = Least similar
2 and 7 = Not very similar (worse than 2 and 10 tho)
2 and 10 = Not very similar
4 and 7 = Pretty similar
7 and 10 = Most similar


## Similarity Metrics
### Hamming - Not very representative
2 and 4 = 22
2 and 7 = 18
2 and 10 = 18
4 and 7 = 13
7 and 10 = 4

### Cosine - Useless
2 and 4 = 0.938144
2 and 7 = 0.132597
2 and 10 = 0.941581
4 and 7 = 0.627750
7 and 10 = 0.627437

### Jaccard - Also Useless
2 and 4 = 0.956522
2 and 7 = 0.947368
2 and 10 = 0.947368
4 and 7 = 1.0
7 and 10 = 0.800000

### Euclidean
2 and 4 = 2.966699
2 and 7 = 2.227442
2 and 10 = 2.563260	
4 and 7 = 1.549258
7 and 10 = 0.373631

### Manhatten
2 and 4 = 6.83
2 and 7 = 4.85
2 and 10 = 5.29	
4 and 7 = 2.18
7 and 10 = 0.44

### Minkowski
2 and 4 = 2.966699
2 and 7 = 2.227442
2 and 10 = 2.563260
4 and 7 = 1.549258
7 and 10 = 0.373631

## Discussion
Euclidean and Minkowski give the same distance value for every comparison. Manhattan shows same pattern as Euclidean so could be a possibility however Euclidean more accurate. Hamming shows the same pattern however not the best due to it not taking into account the actual value when comparing each row. Cosine and Jaccard are not appropriate.





