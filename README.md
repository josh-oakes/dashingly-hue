# dashingly-hue
Python project that repurposes Amazon Dash buttons to control Philips Hue lights.

### Intro
Inspired by a blog post I read by Josh Prewitt, [here](http://joshprewitt.com/2016/03/24/using-an-amazon-dash-button-to-control-philips-hue-lights/), I decided to take my first stab at some python3 work to automate my Philips Hue lights. I currently have two dash buttons controlling two different groups of lights (not individual like the blog post). One for my living room and one for my bedroom. The hueLightSwitch.py script is running on an extra raspberry pi I had laying around.

### Setup
The blog post is a good starting point for getting your Dash Buttons setup properly (so you aren't ordering 5000 containers of Quaker Oats!) and also has a good explanation on the Scapy python library used for recognizing the dash button network traffic.

In the utilities directory I have two scripts that will be useful in determining the MAC address of your dash button and also a script that will list any groups you have setup on your Hue Bridge.

### Useful Links
Here are some links that I found to be useful while working on this project:
* [Scapy Documentation](https://scapy.readthedocs.io/en/latest/introduction.html)
* [Philips Hue Development Documentation](https://developers.meethue.com/documentation/getting-started)
* [Python 3.7.0 Documentation](https://docs.python.org/3/)
