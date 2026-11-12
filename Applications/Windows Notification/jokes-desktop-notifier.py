import pyjokes
import time
from win10toast import ToastNotifier

# Show a random joke as a desktop notification every 30 minutes.
JOKE_INTERVAL_SECONDS = 1800
TOAST_DURATION_SECONDS = 20
TOAST_TITLE = "Time to laugh!"

while 1:
    notify = ToastNotifier()
    notify.show_toast(TOAST_TITLE, pyjokes.get_joke(), duration=TOAST_DURATION_SECONDS)
    time.sleep(JOKE_INTERVAL_SECONDS)
