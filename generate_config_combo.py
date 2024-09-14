# experiment name
exp_dics = {
    'PD_separate':{
    'name':'pd_separate',
    'config_path': "experiment_configs/pd-separate.json"
        },
    'PD_contract':{
    'name':'pd_contract',
    'config_path': "experiment_configs/pd-contract.json"}
}

id=1
with open("config_combo.txt", "w") as f:
    f.write("ArrayTaskID"+" "+"name"+" "+"config_path")
    for key in exp_dics:
        for num in range(10):
            exp = exp_dics[key]  # Get the dictionary for the current key
            f.write("\n"+str(id)+" "+exp['name']+" "+exp['config_path'])
            id+=1