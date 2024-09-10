#!/bin/bash
#SBATCH --qos=deadline
#SBATCH --mem=4G
#SBATCH --time=0-5:00:00
#SBATCH --partition=cpu
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=6
#SBATCH --array=1-20
#SBTACH --output=logs/%x-%A-%a.out
#SBTACH --error=logs/%x-%A-%a.err

config=config_combo.txt

name=$(awk -v ArrayTaskID=$SLURM_ARRAY_TASK_ID '$1==ArrayTaskID {print $2}' $config)

config_path=$(awk -v ArrayTaskID=$SLURM_ARRAY_TASK_ID '$1==ArrayTaskID {print $3}' $config)

echo "Running $name with config $config_path"

python runner.py --config_path $config_path --name $name