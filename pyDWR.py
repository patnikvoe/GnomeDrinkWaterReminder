#!/usr/bin/python3

import notify2

# icon Path
ICON_PATH = "/home/patnikvoe/pyGDWR/icon.png"

# initialise the d-bus connection
notify2.init("Python Drink Water Reminder")

# create Notification object
n = notify2.Notification("Drink some water", message = "Your daily goal is 2 liters", icon = ICON_PATH)

# Set the urgency level
n.set_urgency(notify2.URGENCY_NORMAL)

# Set the timeout
n.set_timeout(1000)

# show Notification
n.show()
