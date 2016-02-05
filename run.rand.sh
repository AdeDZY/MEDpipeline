#!/bin/bash
export PATH=$opensmile_path:$speech_tools_path:$ffmpeg_path:$map_path:$PATH
export LD_LIBRARY_PATH=$ffmpeg_path/libs:$opensmile_path/lib:$LD_LIBRARY_PATH

for i in {1..30}
do
    python scripts/randpred.py rand_pred/rand_pred${i}
done

for i in {1..3}
do
    for j in {1..30}
    do
        ./mAP/ap list/P00${i}_test_label rand_pred/rand_pred${j} >> rand_pred_P00${i}.res
    done
done
