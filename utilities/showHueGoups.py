#!/usr/bin/env python
import urllib.request, json

# IP Address of your Hue Bridge
bridgeIP = ""

# Username you generated for Hue API
user = ""

# request light group ids
request = urllib.request.Request("http://" + bridgeIP + "/api/" + user + "/groups/")
response = urllib.request.urlopen(request)

# response body
responseBody = response.read()

jsonResponse = json.loads(responseBody.decode("utf-8"))

for i in jsonResponse:
    print(jsonResponse[i]["name"] + " has light ID: " + i)
    print(jsonResponse[i]["name"] + " state is set to: " + str(jsonResponse[i]["action"]["on"]))
