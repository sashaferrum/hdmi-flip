import RPi.GPIO as GPIO
import picamera
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
        hdmi_init = False
        while not hdmi_init:
                try:
                        print ("Trying to initialize HDMI input")
                        hdmi_in = picamera.PiCamera()
                        hdmi_init = True

                except KeyboardInterrupt:
                        break

                except Exception:
                        print ("Initializing has gone wrong. Trying again...")
                        #GPIO.wait_for_edge(16, GPIO.FALLING, bouncetime=300)
                        #print ("Reset has been  pressed")

        hdmi_in.hflip = True

        print ("input HDMI interface initialized")

        try:
                print ("Trying to connect")
                hdmi_in.start_preview()
                print ("It's working!")
                #Ждем нажатия кнопки
                GPIO.wait_for_edge(16, GPIO.FALLING, bouncetime=300)
                print ("Reset button has been pressed")
                hdmi_in.close()
                print ("Closing HDMI IN")

        except KeyboardInterrupt:
                break

        except Exception:
                print ("Preview has gone wrong. Waiting for reset...")
                #GPIO.wait_for_edge(16, GPIO.FALLING, bouncetime=300)
                #print ("Reset has been pressed")
                hdmi_in.close()
                print ("Closing HDMI IN")