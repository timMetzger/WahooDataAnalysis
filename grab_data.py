# *****************************
# By: Tim Metzger
# *****************************

import json
import os
import requests


# format for scopes --> {scope1}%20{scope2}%20{scope3}%20....
def get_tokens(base_url, client_id, client_secret, redirect_uri, scopes):
    # Getting OAuth2 response code
    oauth_url = f'https://{base_url}/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&scope={scopes}&response_type=code '

    print("Please go to the following link and enter the code in the return url")
    print(oauth_url)
    code = input("Code: ")

    # Getting Access/Refresh Tokens
    token_url = f'https://{base_url}/oauth/token?client_secret={client_secret}&code={code}&redirect_uri={redirect_uri}&grant_type=authorization_code&client_id={client_id} '
    data = {'grant_type': 'authorization_code', 'code': code, 'redirect_uri': redirect_uri}

    post_request = requests.post(url=token_url, data=data)
    print('Post Headers')
    print(post_request.headers)
    print('Post Text')
    print(post_request.text)

    tokens = json.loads(post_request.text)
    access_token = tokens['access_token']
    refresh_token = tokens['refresh_token']

    return access_token, refresh_token


def get_data():
    base_url = "api.wahooligan.com"
    client_id = "q9Yz4hl9KC46poOU9leIQZsAEz7ET3TJu3gG3jskWZs"
    client_secret = "Tf4I-4YftywUKHApAnUBcFD-DumJvXcimRvM-2EIt5g"
    redirect_uri = "https://github.com/timMetzger"
    scopes = "workouts_read%20user_read"
    # ACCESS_TOKEN,REFRESH_TOKEN = get_tokens(base_url,client_id,client_secret,redirect_uri,scopes)
    ACCESS_TOKEN = "vA0pr4azAVuwwQrwwdEjvINiFYgOOyli5zAg4yPHrBw"
    REFRESH_TOKEN = "6qlH7ceF_faTJ87qOPGaEdqgZypkDdzBUrn_E7fa6cs"
    refresh_token_url = f'https://{base_url}/oauth/token?client_secret={client_secret}&client_id={client_id}&grant_type=refresh_token&refresh_token={REFRESH_TOKEN} '
    api_header = {'Authorization': 'Bearer ' + ACCESS_TOKEN}
    api_url_main = "https://api.wahooligan.com/v1/user"
    api_url_workouts = "https://api.wahooligan.com/v1/workouts?180"  # number of workouts
    while True:
        try:
            # Getting clients information
            api_response_overview = requests.get(api_url_main, headers=api_header)
            print(api_response_overview.text)
            # Getting clients workouts
            api_response_workouts = requests.get(api_url_workouts, headers=api_header)
            print(api_response_workouts.text)
            break
        except: # not sure what type here
            new_token_request = requests.get(refresh_token_url)
            print(new_token_request.text)
            input("Waiting for user input")

    working_dir = os.getcwd()
    client = json.loads(api_response_overview.text)
    new_dir_name = client['last'] + client['first']
    if os.path.isfile(f'{working_dir}/{new_dir_name}'):
        os.mkdir(f'{working_dir}/{new_dir_name}')
    # Writing client information to json
    with open(f'{working_dir}/{new_dir_name}/client_info.json', 'w') as outfile:
        json.dump(api_response_overview.json(), outfile, indent=4)
    outfile.close()

    # Writing workouts to json
    with open(f'{working_dir}/{new_dir_name}/client_workouts.json', 'w') as outfile:
        json.dump(api_response_workouts.json(), outfile, indent=4)
    outfile.close()
    print('Jobs Done!')


get_data()
