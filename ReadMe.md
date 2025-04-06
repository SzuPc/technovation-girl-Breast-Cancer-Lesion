# Interpretable Ultrasound Breast Cancer Lesion Recognition Based on Temporal Memory

### [Project Page]([https://cotracker3.github.io/](https://szupc.github.io/Breast-Lesion-Detection/))

## Introduction

We are committed to protecting the healthy development of women and have developed an algorithm for rapid detection of breast cancer. It simulates the characteristics of doctors when making diagnoses and can quickly review lesions from previous periods to see if there are any false positive cases. It can also provide auxiliary guidance to young doctors and remote areas with unbalanced medical resources.

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
