# Interpretable Ultrasound Breast Cancer Lesion Recognition Based on Temporal Memory

## Introduction


## Training and Inference

You can train or infer with UltraDet by running the following code:

```shell
# Training
python train_net.py --num-gpus {GPU_NUM} \
--config-file {CONFIG_FILES}

# Validation
python train_net.py --num-gpus {GPU_NUM} --eval-only --resume \
--config-file {CONFIG_FILES}

# Test
python train_net.py --num-gpus {GPU_NUM} --eval-only  --resume \
--config-file {CONFIG_FILES} \
DATASETS.SPLIT "test" \
DATASETS.NUM_FOLDS 1 \
# MODEL.WEIGHTS 'pretrained_models/ultradet.pth' # If you wish to load the pre-trained weights of UltraDet that we have released, please include this line of code
```

python train_net.py --num-gpus 1 --eval-only  --resume \
--config-file /home/lenovo/zrl_science_project/UltraDet/configs/Base-UltraDet_R34_C4.yaml \
DATASETS.SPLIT "test" \
DATASETS.NUM_FOLDS 1 