import os, sys
# import specific version of Notify to remove Warning
import gi
gi.require_version('Notify', '0.7')
# This time import the GdkPixbuf module
from gi.repository import Notify, GdkPixbuf

# Initialise
Notify.init("GDWR")

# Set Reminder Text here
notification = Notify.Notification.new("Drink some water!")

# Add icon
file = os.path.join(sys.path[0], 'icon.png')
image = GdkPixbuf.Pixbuf.new_from_file(file)

# Use the GdkPixbuf image
notification.set_icon_from_pixbuf(image)
notification.set_image_from_pixbuf(image)

# Print Notification
notification.show()
