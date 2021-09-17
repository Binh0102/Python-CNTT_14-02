import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

while True:
	with speech_recognition.Microphone() as mic:
		print("Robot: I'm Listening")
		audio = robot_ear.listen(mic)

	print("Robot:...")

	try:
		you = robot_ear.recognize_google(audio)
	except:
		you = ""
	print("You:" +you)

	if you =="":
		robot_brain = "I can't hear, try again"
	elif "Hello" in you:
		robot_brain = "Hello Bình"
	elif "today" in you:
		today = date.today()
		d2 = today.strftime("%B %d, %Y")
	elif "english" in you:
		robot_brain = ""
	elif "time" in you:
		now = datetime.now()
		robot_brain = now.strftime("%H hours %M minutes %S seconds")
	elif "bye" in you:
		robot_brain = "bye Bình"
		print("Robot:" + robot_brain)
		robot_mouth.say("hello")
		robot_mouth.runAndWait()
		break
	else:
		robot_brain = "I'm fine thank you and you"

	print("Robot:" + robot_brain)
	robot_mouth.say("hello")
	robot_mouth.runAndWait()