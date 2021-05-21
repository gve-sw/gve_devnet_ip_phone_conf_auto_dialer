"""
Copyright (c) 2020 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

import requests
from requests.auth import HTTPBasicAuth
from credentials_and_variables import *


# Ring the phone
def ring_phone():
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = 'XML=<CiscoIPPhoneExecute><ExecuteItem Priority="0" URL="Dial:{0}"/></CiscoIPPhoneExecute>'.format(phone_number)
    r = requests.post(base_url, headers=headers, data=data, auth=HTTPBasicAuth(username, password))
    print(r)
    return r.status_code


# Mute the phone
def mute_phone():
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = 'XML=<CiscoIPPhoneExecute><ExecuteItem Priority="0" URL="Key:Mute"/></CiscoIPPhoneExecute>'
    r = requests.post(base_url, headers=headers, data=data, auth=HTTPBasicAuth(username, password))
    print(r)
    return r.status_code
