#!/usr/bin/env python
from scapy.all import *
import urllib.request, urllib.parse, json

# IP Address of your Hue Bridge
bridgeIP = ""

# Username you generated for Hue API
user = ""

# MAC Address of Dash button
livingRoomDashMAC = ""

# MAC Address of Dash button
bedroomDashMAC = ""

# Group ID of living room
livingRoomGroupID = "1"

# Group ID of bedroom
bedroomGroupID = "2"


def toggle_lights(group_id):
    # check state of group
    request = urllib.request.Request("http://" + bridgeIP + "/api/" + user + "/groups/" + group_id)
    response = urllib.request.urlopen(request)
    response_body = response.read()

    group_response = json.loads(response_body.decode("utf-8"))

    if group_response["action"]["on"]:
        # set action to false
        values = {"on": False}
    else:
        # set action to true
        values = {"on": True}

    # build request for state change
    action_data = json.dumps(values).encode("utf-8")
    json_headers = {'Content-Type': 'application/json'}
    state_change_request = urllib.request.Request(
        url="http://" + bridgeIP + "/api/" + user + "/groups/" + group_id + "/action", data=action_data,
        headers=json_headers, method="PUT")
    state_change_response = urllib.request.urlopen(state_change_request)


# callback to check when dash button comes online
def arp_display(pkt):
    if scapy.all.ARP in pkt and pkt[scapy.all.ARP].op in (1, 2):
        if pkt[scapy.all.ARP].hwsrc == livingRoomDashMAC:
            toggle_lights(livingRoomGroupID)
        elif pkt[scapy.all.ARP].hwsrc == bedroomDashMAC:
            toggle_lights(bedroomGroupID)


scapy.all.sniff(prn=arp_display, filter="arp", store=0, count=0)
