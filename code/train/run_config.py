import os

from azureml.core import ComputeTarget
from azureml.train.estimator import Estimator


def main(workspace):
    kernel = os.environ.get("KERNEL_TYPE", "linear")
    penalty = int(os.environ.get("PENALTY", 1.0))

    # Load compute target
    print("Loading compute target")
    compute_target = ComputeTarget(workspace=workspace, name="cpu-cluster")

    # Load script parameters
    print("Loading script parameters")
    script_params = {"--kernel": kernel, "--penalty": penalty}

    # Create experiment config
    print("Creating experiment config")
    estimator = Estimator(
        source_directory="code/train",
        entry_script="train.py",
        script_params=script_params,
        compute_target=compute_target,
        pip_packages=[
            "azureml-dataprep[pandas,fuse]",
            "scikit-learn",
            "pandas",
            "matplotlib",
        ],
    )
    return estimator
