from datetime import datetime, timedelta
import time
import webbrowser
running = True

period = timedelta(minutes=30)

next_time = datetime.now() + period

while running:
    if next_time > datetime.now():
        time.sleep(60)
    else:
        webbrowser.open('https://www.youtube.com/watch?v=pSGa0Ufo-1w', new='1')
        next_time = datetime.now() + period
