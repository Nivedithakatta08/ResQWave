import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import argparse
from src.train_cnn import train
from src.detector import run_detector

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ResQWave - Smart Traffic Management")
    parser.add_argument('--mode', choices=['train', 'detect'], required=True,
                        help="'train' to train CNN, 'detect' to run detector")
    parser.add_argument('--arduino', action='store_true',
                        help="Enable Arduino serial communication")
    args = parser.parse_args()

    if args.mode == 'train':
        print("Starting CNN training...")
        train()
    elif args.mode == 'detect':
        print("Starting real-time detector...")
        run_detector(use_arduino=args.arduino)