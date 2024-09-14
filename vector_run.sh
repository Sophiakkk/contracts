#!/bin/bash
#SBATCH --account=deadline
#SBATCH --qos=deadline

#SBATCH --job-name="pd-all"
#SBATCH --gres=gpu:1
#SBATCH --partition=cpu
#SBATCH --time=100:00:00
#SBATCH -c 6
#SBATCH --mem=4G

#SBATCH --array=1-20
#SBATCH --output=logs/%x-%A-%a.out
#SBATCH --error=logs/%x-%A-%a.err

config=config_combo.txt

name=$(awk -v ArrayTaskID=$SLURM_ARRAY_TASK_ID '$1==ArrayTaskID {print $2}' $config)

config_path=$(awk -v ArrayTaskID=$SLURM_ARRAY_TASK_ID '$1==ArrayTaskID {print $3}' $config)

echo "Running $name with config $config_path"

python runner.py --config_path $config_path --name $name --task_id $SLURM_ARRAY_TASK_ID