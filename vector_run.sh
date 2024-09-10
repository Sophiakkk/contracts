#!/bin/bash
#SBATCH --qos=deadline
#SBATCH --mem=4G
#SBATCH --time=0-5:00:00
#SBATCH --ntasks=4
#SBATCH --partition=cpu
#SBATCH --cpus-per-task=1
#SBATCH --array=1-20
#SBTACH --output=logs/array_%A_%a.out

config=config_combo.txt

name=$(awk -v ArrayTaskID=$SLURM_ARRAY_TASK_ID '$1==ArrayTaskID {print $2}' $config)

config_path=$(awk -v ArrayTaskID=$SLURM_ARRAY_TASK_ID '$1==ArrayTaskID {print $3}' $config)

python runner.py --config_path $config_path --name $name  --seeds $SLURM_ARRAY_TASK_ID