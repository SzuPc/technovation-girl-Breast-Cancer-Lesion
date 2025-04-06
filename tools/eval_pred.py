import torch
from detectron2.evaluation import print_csv_format
from detectron2.utils.logger import setup_logger

from ultrasound_vid.evaluation.evaluator import UltrasoundVideoDetectionEvaluator

setup_logger(name="ultrasound_vid")
setup_logger(name="detectron2")

from path import Path

dump_dirs = [
    "/home/lenovo/zrl_science_project/UltraDet/output",
]

datasets = [
    "breast_cva_test",
]

for dataset, dump_dir in zip(datasets, dump_dirs):
    evaluator = UltrasoundVideoDetectionEvaluator(dataset_name=dataset)
    evaluator.load_predictions(dump_dir=dump_dir)
    results = evaluator.evaluate(dump_dir=dump_dir)
    print_csv_format(results)

    print("EOF")
