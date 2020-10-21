import cv2 
import pytesseract
import os
from gtts import gTTS
from picamera.array import PiRGBArray
from picamera import PiCamera

VFSADcamera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30

rawCapture = PiRGBArray(camera, size=(640, 480))

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	image = frame.array
	cv2.imshow("Frame", image)
	key = cv2.waitKey(1) & 0xFF
	
	rawCapture.truncate(0)

	if key == ord("s"): /* If S key is pressed image will be captured */
		content = pytesseract.image_to_string(image)
		print(content)
		cv2.imshow("Frame", image)
		cv2.waitKey(0)
                gttsobject= gTTS(text=content, lang="en-us", slow=False)
                gttsobject.save("voice.mp3") 
                os.system("mpg321 voice.mp3")
		break

cv2.destroyAllWindows()
