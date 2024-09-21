#!/bin/bash
#SBATCH --job-name="ipc-contract"
#SBATCH --account=deadline
#SBATCH --qos=deadline
#SBATCH --mem=4G
#SBATCH --time=0-24:00:00
#SBATCH --partition=t4v1,t4v2,a40,rtx6000
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=6
#SBATCH --array=1
#SBATCH --output=logs/%x-%A-%a.out
#SBATCH --error=logs/%x-%A-%a.err

# Initialize Conda
source /scratch/ssd004/scratch/shuhui//miniconda3/etc/profile.d/conda.sh 
conda activate contracting

config=config_combo.txt

name=$(awk -v ArrayTaskID=$SLURM_ARRAY_TASK_ID '$1==ArrayTaskID {print $2}' $config)

config_path=$(awk -v ArrayTaskID=$SLURM_ARRAY_TASK_ID '$1==ArrayTaskID {print $3}' $config)

echo "Running $name with config $config_path"

python runner.py --config_path $config_path --name $name --task_id $SLURM_ARRAY_TASK_ID