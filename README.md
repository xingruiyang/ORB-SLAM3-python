ORB-SLAM3-PYTHON
===

Python bindings generated using [pybind11](https://pybind11.readthedocs.io/en/stable/). We use a modified version of ORB-SLAM3 (included as a submodule) to exntend interfaces. It might not be the most up-to-date with the original ORB-SLAM3.

## Update

+ Oct. 3rd, 2023: Added demo code.
+ Feb. 7th, 2023: First working version. 

## Dependancy

+ OpenCV >= 4.4
+ Pangolin
+ Eigen >= 3.1
+ C++11 or C++0x Compiler

## Installation

1. Clone the repo with `--recursive`
2. Install `Eigen`, `Pangolin` and `OpenCV` if you havn't already.
3. `ORB-SLAM3` requires `openssl` to be installed: `sudo apt-get install libssl-dev`
4. Run `python setup install` or `pip install .`.
5. Please raise an issue if you run into any.

## Demo

Please see the demo at `demo/run_rgb.py` for how to use this code. For example, you can run this demo with (by substituting the appropriate arguments):

```bash
python demo/run_rgbd.py \
    --vocab_file=third_party/ORB_SLAM3/Vocabulary/ORBvoc.txt \
    --settings_file=third_party/ORB_SLAM3/Examples/RGB-D/TUM1.yaml \
    --dataset_path=/mnt/dataset2/TUM/rgbd_dataset_freiburg1_xyz
```