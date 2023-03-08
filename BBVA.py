import speech_recognition as sr
import subprocess
import sys

# Initialize speech recognition
r = sr.Recognizer()


# Define a function to listen for voice commands
def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Im listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print("Command:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        print("Sorry, I could not connect to the service.")
        return ""

# Define a function to open applications based on voice commands
def open_app(command):
    if "open safari" in command:
        subprocess.call(["open", "-a", "Safari"])
    elif "open chrome" in command:
        subprocess.call(["open", "-a", "Google Chrome"])
    elif "open outlook" in command:
        subprocess.call(["open", "-a", "Outlook"])
    elif "open teams" in command:
        subprocess.call(["open", "-a", "Teams"])
    elif "open spotify" in command:
        subprocess.call(["open", "-a", "Spotify"])
    elif "open discord"in command:
        subprocess.call(["open", "-a", "Discord"])
    else:
        print("Command not recognized.")
# Define a function to close applications based on voice commands
def close_app(app_name):
    script = f'close"{app_name}" '
    subprocess.run(['osascript', '-e', script])

close_app("Spotify")
close_app("Google Chrome")
close_app("Outlook")
close_app("Discord")
close_app("Teams")

def end_task(command):
    if "shut down" in command:
        subprocess.call([sys.exit()])

# Continuously listen for commands and open/closes applications
while True:
    command = listen()
    open_app(command)
