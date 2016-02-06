# MEDpipeline hw1

## run.feature.sh
Generate MFCC Bag-of-Words Features and ASR Bag-of-Words feature.

MFCC Bag-of-Words features in ./kmeans/all.vectors. By default K=500.

ASR Bag-of-Words features in ./asrfeat/all.vectors. 

## run.med.sh

Train and test classifiers 

MFCC BOW models in ./mfcc_pred/svm.P00i.model. By default, using RBF-kernel SVM with gamma = 0.00005.

ASR BOW models in ./asr_pred/svm.P00i.model. By default, using RBF-kernel SVM with gamma = 0.00001.

## run.mfccavg.sh

Create avg-MFCC features, and train SVM based on these features.

Features in ./mfccavg_feat/
Models and predictions in ./mfccavg_pred/

## run.rand.sh

Create and test random predictions

Results writtein in ./rand_pred/avg_rand.res



