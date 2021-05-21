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

# IP Address of the Dialing phone
phone_ip_address = "DIALING_PHONE_IP_ADDRESS_HERE"


# CUCM - User's credential
username = "YOUR_USERNAME_HERE"  # source user
password = "YOUR_PASSWORD_HERE"  # source user password
base_url = "http://" + phone_ip_address + "/CGI/Execute"  # Ip address of source

# Destination Directory Number - This would be the number we are dialing to:
phone_number = 0000  # <---destination phone number

