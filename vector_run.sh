#!/bin/bash
#SBATCH --account=deadline
#SBATCH --qos=deadline

#SBATCH --job-name="pdcontract"
#SBATCH --gres=gpu:1
#SBATCH --partition=rtx6000
#SBATCH --time=5:00:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G

#SBATCH --array=1-20%5
#SBATCH --output=logs/%x-%A-%a.out
#SBATCH --error=logs/%x-%A-%a.err

config=config_combo.txt

name=$(awk -v ArrayTaskID=$SLURM_ARRAY_TASK_ID '$1==ArrayTaskID {print $2}' $config)

config_path=$(awk -v ArrayTaskID=$SLURM_ARRAY_TASK_ID '$1==ArrayTaskID {print $3}' $config)

echo "Running $name with config $config_path"

python runner.py --config_path $config_path --name $name  --seed $SLURM_ARRAY_TASK_ID