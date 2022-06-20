import json

import yaml
import requests

# importing API from config.yml file
yaml_file = open('config.yml', 'r')
config = yaml.load(yaml_file, Loader=yaml.SafeLoader)
api_key = (config["jc_key"])
temp_pass = (config["temp_jc_pass"])

headers = {
        'Content-Type': 'application/json',
        'x-api-key': api_key
    }

payload = {}

jump_url = "https://console.jumpcloud.com/api/systemusers"  # JumpCloud users url to gather user file
jump_response = requests.request("GET", jump_url, headers=headers, data=payload)

jump_dump = json.loads(jump_response.text)
jump_users_count = jump_dump['totalCount'] # Total number of users in Jumpcloud
jump_result = []

total_loop_cycle = round(jump_users_count/100)*100
print(total_loop_cycle)
i = 0
while i <= total_loop_cycle:
    skip = str(i)
    query_string = {"limit":"100","skip":skip}
    jump_response = requests.request("GET",jump_url,headers = headers,params=query_string)
    print(jump_response)
    jump_dump_add = json.loads(jump_response.text)
    jump_dump_add.pop("totalCount")
    jump_dump_result = jump_dump_add['results']
    jump_result.extend(jump_dump_result)
    i+=100

json_obj = json.dumps(jump_result,indent=4)

