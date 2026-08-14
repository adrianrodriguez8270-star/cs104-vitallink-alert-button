import time
import RPi.GPIO as GPIO
import requests

BOT_TOKEN = "8605158447:AAGf6hGoySsYWVEig0PLWjXDGcoVifTZgH8"
CHAT_ID = "8692995709"

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
print("Alert button monitoring system is now active. Press Ctrl+C to exit.")
button_pressed = False
try:
    while True:
        if GPIO.input(7) == GPIO.HIGH and not button_pressed:
            print("Someone pressed the alert button!")
            response = requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                data={"chat_id": CHAT_ID, "text": "Someone pressed the alert button!"}
            )
            print("Status code:", response.status_code)
            print("Response:", response.text)
            button_pressed = True
        elif GPIO.input(7) == GPIO.LOW:
            button_pressed = False
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nMonitoring stopped.")
    GPIO.cleanup()

