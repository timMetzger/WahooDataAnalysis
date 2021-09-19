# *****************************
# By: Tim Metzger
# *****************************


import json
import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import fitdecode
import urllib.request



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

    print(client_workouts['workouts'][0]['workout_summary']['heart_rate_avg'])

    workout_fit_file_url = client_workouts['workouts'][0]['workout_summary']['file']['url']
    urllib.request.urlretrieve(workout_fit_file_url, "workout1.fit")

    with fitdecode.FitReader('workout1.fit') as fit:
        for frame in fit:
            if isinstance(frame,fitdecode.FitDataMessage):
                print(fitdecode.records.FitDataMessage)







data_analysis('MetzgerTimothy')

