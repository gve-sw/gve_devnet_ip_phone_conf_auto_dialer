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
from bs4 import BeautifulSoup
from calling_functions import phone_ip_address, ring_phone, mute_phone
import time

# Variables for the Beautiful Soup package, It scraps the calling phone's web page & searches for the
# "Active" or "Not Ready" keywords
# URL from  the calling phone
url = "http://" + phone_ip_address + "/CGI/Java/Serviceability?adapter=device.statistics.streaming.0"  # URL from  the calling phone
h = {"Cache-Control": "no-cache","Pragma": "no-cache"}  # un-caches the data from the get request


# Web page Scrap function
def status_connected():
    page = requests.get(url, headers=h)  # makes the get request - include the headers to un-cache the request
    soup = BeautifulSoup(page.content, 'html.parser')
    phone_status = soup.find_all('b', string=' Active')
    if phone_status:
        print("Active")
    else:
        print("Not Ready")
    return phone_status


# While loop that keeps the phone dialing. If the state is Not Ready it will ring the phone (even if the called line
# if busy) until the called phone answers. Once the call is connected, the calling phone will automatically be put on
# mute. If it is in the Active state, it sleeps for 5 seconds before trying the loop again.
#
while True:
    if not status_connected():
        ring_phone()
        time.sleep(5)
        mute_phone()
    time.sleep(5)

