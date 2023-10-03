import orbslam3
import argparse
from glob import glob
import os 
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("--vocab_file", required=True)
parser.add_argument("--settings_file", required=True)
parser.add_argument("--dataset_path", required=True)
args = parser.parse_args()

img_files = sorted(glob(os.path.join(args.dataset_path, 'rgb/*.png')))
slam = orbslam3.system(args.vocab_file, args.settings_file, orbslam3.Sensor.MONOCULAR)
slam.set_use_viewer(True)
slam.initialize()

for img in img_files:
    timestamp = img.split('/')[-1][:-4]
    img = cv2.imread(img, -1)
    pose = slam.process_image_mono(img, float(timestamp))
    print(pose)