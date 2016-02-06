#!/bin/bash

# An example script for multimedia event detection (MED) of Homework 1
# Before running this script, you are supposed to have the features by running run.feature.sh 

# Note that this script gives you the very basic setup. Its configuration is by no means the optimal. 
# This is NOT the only solution by which you approach the problem. We highly encourage you to create
# your own setups. 

# Paths to different tools; 
export PATH=$opensmile_path:$speech_tools_path:$ffmpeg_path:$map_path:$PATH
export LD_LIBRARY_PATH=$ffmpeg_path/libs:$opensmile_path/lib:$LD_LIBRARY_PATH

echo "#####################################"
echo "#       MED with MFCC Features      #"
echo "#####################################"

# create avg mfcc features
python scripts/create_mfccavgfeat.py list/all.video
feat_dim_mfcc=39

for event in P001 P002 P003; do
  echo "=========  Event $event  ========="
  # now train a svm model
  python scripts/train_svm.py $event "mfccavg_feat/" $feat_dim_mfcc mfccavg_pred/svm.$event.model -k rbf -g 0.00001 || exit 1;
  # apply the svm model to *ALL* the testing videos;
  # output the score of each testing video to a file ${event}_pred 
  python scripts/test_svm.py mfccavg_pred/svm.$event.model "mfccavg_feat/" $feat_dim_mfcc mfccavg_pred/${event}_pred || exit 1;
  # compute the average precision by calling the mAP package
  ./mAP/ap list/${event}_test_label mfccavg_pred/${event}_pred >> log
done

