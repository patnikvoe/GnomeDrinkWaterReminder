# pyGDWR - Python: Gnome Drink Water Reminder
Use the Gnome notifications to send reminders to drink something

## Download the files
First clone the repository in the directory that you want it to be:
```
git clone https://github.com/patnikvoe/pyGDWR.git
```
## Configuration
For automatic repetition of the reminder, I used crontab. For generating a crontab string, refer to https://crontab.guru/

**Example:** every 30 minutes from 8-21
```
*/30 8-21 * * * python3 /path/to/your/clone/pyGDWR.py
```
**Example:** every 1 hour from 10-20
```
0 10-21 * * * python3 /path/to/your/clone/pyGDWR.py
```
If you are still running Python2 use `python` instead of `python3`

## Credits
The icon used for the notifications was found here:
http://www.iconarchive.com/show/food-drink-icons-by-graphicloads/drink-icon.html
