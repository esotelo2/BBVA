import speech_recognition as sr
import appscript 

# Define a function to handle opening apps
def open_app(app_name):
    appscript.app(app_name).activate()

# Define a function to handle closing apps
def close_app(app_name):
    appscript.app(app_name).quit()

# Initialize the speech recognition engine
r = sr.Recognizer()

# Define the microphone as the audio source
mic = sr.Microphone()

# Start listening for voice commands
with mic as source:
    r.adjust_for_ambient_noise(source)  # Reduce background noise
    while True:
        print("I'm listening...")
        audio = r.listen(source)
        print("Recognizing...")
        try:
            # Use Google's speech recognition service to convert audio to text
            command = r.recognize_google(audio)
            print("Command:", command)

            # Parse the command and perform the corresponding action
            if "open" in command:
                app_name = command.split("open ")[1]
                open_app(app_name)
            elif "close" in command:
                app_name = command.split("close ")[1]
                close_app(app_name)

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
