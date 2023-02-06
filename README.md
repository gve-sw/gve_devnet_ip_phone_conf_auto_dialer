# GVE DevNet IP Phone Conf Auto Dialer 

Script that instructs an IP phone to dial a pre-established conference. The phone reconnects if either the remote or local party hangs up.


## Contacts
* Max Acquatella (macquate@cisco.com)

## Solution Components
*  CUCM
*  Cisco IP Phone
*  Python3

## Prerequisites
Collect the following information from the CUCM and/or Cisco IP phone. This information will be the input for the credentials_and_variables.py script:
* phone_ip_address: Ip address of the calling phone. This will be the phone that places the call and keeps dialing if disconnected.
* username: The script requires a valid CUCM User (We recommend create a specific user for this purpose). Eg: "conference_dialer".
* password: Password of the User, provided by CUCM.
* phone_number: The destination phone number. 

Please make sure to activate the auto answer feature on the destination directory number. This is done directly in CUCM:

![/IMAGES/cucm_auto_answer.png](/IMAGES/cucm_auto_answer.png)

The phone_ip_address can be obtained from CUCM or directly from the phone:

![/IMAGES/phone_ip.png](/IMAGES/phone_ip.png)

## Installation/Configuration

Clone this repo folder:

```git clone (folder)```

Create Virtual Environment (recommended), and install requirements.txt:

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Make sure that the machine where the script is installed can reach the IP address of the dialing phone. 
Do this by trying a ping from the command line of your machine. 


## Usage

From your command line, launch scrap_and_dial.py:

    $python scrap_and_dial.py

The Calling phone should dial the destination directory number automatically, and once connected, mute itself and stay in the call indefinitely. 
Your console will output the following messages as the script detects the states of the dialing phone, either Active or Not Ready: 

![/IMAGES/scrap_and_call.png](/IMAGES/scrap_and_call.png)

You will have to stop the script via command line (ctr+C) to stop the dialing phone from calling. 


### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
