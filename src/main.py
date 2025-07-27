import time
import pyttsx3
import speech_recognition as sr
from assistant.recognizer import Recognizer
from assistant.responder import Responder
from assistant.commands import CommandHandler

def main():
    recognizer = Recognizer()
    voice_engine = pyttsx3.init()  # Initialize your voice engine here
    responder = Responder(voice_engine)
    command_handler = CommandHandler()

    responder.respond("Voice Assistant is now active. How can I assist you?")

    while True:
        try:
            command = recognizer.listen()
            if command:
                print(f"Recognized command: {command}")  # Debug statement
                if command.lower() == "exit":
                    responder.respond("Shutting down. Goodbye!")
                    break
                response = command_handler.handle_command(command)
                print(f"Generated response: {response}")  # Debug statement
                responder.respond(response)
        except Exception as e:
            print(f"An error occurred: {e}")
            responder.respond("Sorry, I didn't catch that. Could you please repeat?")

        time.sleep(1)

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)
        print("Audio captured!")
    main()