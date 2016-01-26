# MEDpipeline hw1

## Train Kmeans
Train Kmeans centroids with smapled MFCC features, the model will be written by cPickle

#####Inputs:

1. mfcc_csv_file --  input MFCC file
2. num_cluster -- number of clusters
3. output_file -- file to write the kmeans model

#####Example:

```
./scripts/train_kmeans.py select.mfcc.csv 200 kmeans.200.model
```

## Create kmeans
Create MFCC BOW feature vectors with traned Kmeans model

#####Inputs:

1. kmeans_model -- path to the kmeans model
2. cluster_num -- type=int, number of cluster
3. file_list -- the list of videos
4. --output_file_path, -o -- output features file, default="/home/ubuntu/hw1/kmeans/all.vectors

#####Output:
The features by default will be written into ./kmeans/all.vectors

#####Example:

```
./scripts/create_kmeans.py kmeans.200.model 200 list/all.video
```

## Create ASR Bag-Of-Words features
Create BOW ASR features

#####Inputs:
1. vocab_file -- path to the vocabulary file
2. file_list -- the list of videos
3. stopwords_file -- stopwords file path

#####Output:
The features will be written into ./asrfeat/all.vectors

#####Example:

```
./scripts/create_asrfeat.py vocab list/all.video stoplist.dft
```
