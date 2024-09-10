#!/bin/bash
#SBATCH --qos=deadline
#SBATCH --mem=4G
#SBATCH --time=0-5:00:00
#SBATCH --partition=cpu
#SBATCH --cpus-per-task=4
#SBATCH --array=1-20
#SBATCH --output=logs/%x-%A-%a.out
#SBATCH --error=logs/%x-%A-%a.err

# Introduce a delay based on the task ID
sleep_time=$SLURM_ARRAY_TASK_ID  # 10 seconds delay for each task
echo "Sleeping for ${sleep_time} seconds before starting job ${SLURM_ARRAY_TASK_ID}"
sleep ${sleep_time}

config=config_combo.txt

name=$(awk -v ArrayTaskID=$SLURM_ARRAY_TASK_ID '$1==ArrayTaskID {print $2}' $config)

config_path=$(awk -v ArrayTaskID=$SLURM_ARRAY_TASK_ID '$1==ArrayTaskID {print $3}' $config)

echo "Running $name with config $config_path"

python runner.py --config_path $config_path --name $name