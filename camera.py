from gpiozero import LED, Button
from signal import pause
from picamera import PiCamera
import datetime
import pytumblr

button = Button(22) 
camera = PiCamera()

camera.start_preview()
frame = 1

client = pytumblr.TumblrRestClient(
        '2azm9vXd5yUsCVAbPO7S9XrGPY944nurVzzDREwe8Kv3i2G7YY',
        'ewEPQ41ZnAzjAHOkn4uqvtMtxNQOLSpwLGWTg76TPW4FMiw7vX',
        'kTwa6fTO39qsyoqyUg5q4TrEJyLVlurzhc3gyeQx2K1HYNLT1o',
        'lb15Hi1o4lp6lHtlCkkYZ86HRoBNa40ezocajGUIDqMk0oHLHD'
)

while True:

        print("Program running.. Press button to take a photo.")
        button.wait_for_press()  

        client.create_photo(
        'emmasraspi',
        state="published",
        data="/home/pi/tweet/img/frame.jpg"
        )
