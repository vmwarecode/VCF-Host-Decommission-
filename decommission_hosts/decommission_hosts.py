#Decommission hosts.
#Decommissions hosts gives as parametres.
import requests
import json
import sys
import time

def get_help():
    help_description = '''\n\t\t----Decommission hosts----
    Usage:
    python decommission_hosts.py <hostname> <username> <password> <fqdn1> <fqdn2> ..\n Refer to documentation for more detais\n'''
    print (help_description)

def decommission_hosts():
    arguments = sys.argv
    if(len(arguments) < 4):
        get_help()
        return
    hostname = 'https://'+arguments[1]
    username = arguments[2]
    password = arguments[3]
    headers = {'Content-Type': 'application/json'}
    url = hostname+'/v1/hosts'
    data = []
    for fqdn in range(3,len(arguments)):
        data.append({'fqdn':arguments[fqdn]})
    response = requests.delete(url, headers=headers,json = data,auth=(username, password))
    if(response.status_code == 202):
        data = json.loads(response.text)
        task_id = data['id']
        status = data['status']
        url = hostname+'/v1/tasks/'+task_id
        print ('Decommissioning hosts...')
        while(status == 'In Progress'):
            status = json.loads(requests.get(url, headers=headers,auth=(username, password)).text)['status']
            time.sleep(5)
        print ('Decommissioning of hosts is ' + status)
    else:
        print ('Error decommissioning hosts.')
        response = json.loads(response.text)
        print (json.dumps(response,indent=4, sort_keys=True))
        exit(1)
decommission_hosts()

