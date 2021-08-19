# *****************************
# By: Tim Metzger
# *****************************


import json
import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


def data_analysis(client_name):

    working_dir = os.getcwd()
    client_info_path = f'{working_dir}/{client_name}/client_info.json'
    client_workouts_path = f'{working_dir}/{client_name}/client_workouts.json'

    with open (client_info_path,'r') as file:
        client_info = json.loads(file.read())

    file.close()

    with open (client_workouts_path,'r') as file:
        client_workouts = json.loads(file.read())

    file.close()

    print(json.dumps(client_info,indent=4,sort_keys=True))
    print(json.dumps(client_workouts, indent=4, sort_keys=True))






data_analysis('MetzgerTimothy')