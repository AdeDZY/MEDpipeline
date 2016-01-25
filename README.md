# MEDpipeline hw1

## train Kmeans
Train with smapled MFCC features, the model will be written by cPickle

###Inputs:

For help information:
```
~/hw1/scripts/train_kmeans.py -h
```

1. mfcc_csv_file:   input MFCC file
2. num_cluster:   number of clusters
3. output_file:   file to write the kmeans model

###Example:

```
~/hw1/scripts/train_kmeans.py select.mfcc.csv 50 kmeans.50.model
```
