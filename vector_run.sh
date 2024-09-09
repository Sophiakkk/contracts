#!/bin/bash
#SBATCH --qos=deadline
#SBATCH --mem=4G
#SBATCH --time=0-24:00:00
#SBATCH --ntasks=1
#SBATCH --partition=cpu
#SBATCH --cpus-per-task=1
#SBATCH --array=1-20
#SBTACH --output=logs/array_%A_%a.out




python runner.py --name "cleanup-complete" --config_path "experiment_configs/cleanup-contracting.json" 