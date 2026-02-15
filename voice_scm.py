import speech_recognition as sr
import subprocess
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Voice recognition
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Say a command:")
    audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print(f"You said: {command}")

        # Handle commands one by one
        if command.lower() == "commit changes":
            # Stage all files
            subprocess.run(["git", "add", "."], shell=True)
            # Commit with proper message
            subprocess.run(["git", "commit", "-m", "Auto commit via voice"], shell=True)
            print("Commit executed successfully")
            engine.say("Commit executed successfully")
            engine.runAndWait()

        elif command.lower() == "show status":
            subprocess.run(["git", "status"], shell=True)
            engine.say("Status shown successfully")
            engine.runAndWait()

        elif command.lower() == "create branch":
            subprocess.run(["git", "branch", "voice_branch"], shell=True)
            print("Branch 'voice_branch' created")
            engine.say("Branch created successfully")
            engine.runAndWait()

        elif command.lower() == "push changes":
            subprocess.run(["git", "push"], shell=True)
            print("Changes pushed to remote")
            engine.say("Changes pushed successfully")
            engine.runAndWait()

        else:
            print("Command not recognized")
            engine.say("Command not recognized")
            engine.runAndWait()

    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
        engine.say("Sorry, I could not understand")
        engine.runAndWait()
    except sr.RequestError:
        print("Check your internet connection.")
        engine.say("Check your internet connection")
        engine.runAndWait()

