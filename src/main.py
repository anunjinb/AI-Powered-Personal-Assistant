import speech_recognition as sr  # For speech recognition
import pyttsx3  # For text-to-speech
import datetime  # For getting current date and time

# Initialize the recognizer for speech recognition
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speed of speech
engine.setProperty('volume', 1)  # Adjust volume level (0.0 to 1.0)

def listen_to_user():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjusts for ambient noise
        audio = recognizer.listen(source)
    
    try:
        # Recognize speech using Google Speech Recognition
        print("Recognizing...")
        user_input = recognizer.recognize_google(audio)
        print(f"User said: {user_input}")
        return user_input
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        print("Sorry, there was an issue with the speech service.")
        return None

def speak_to_user(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def perform_task(user_input):
    if user_input is None:
        return

def perform_task(user_input):
    if user_input is None:
        return

    # Convert the input to lowercase to handle case insensitivity
    user_input = user_input.lower()

    # Check if the user asked for the time
    if "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak_to_user(f"The current time is {current_time}")
    
    # You can add more tasks here
    elif "hello" in user_input:
        speak_to_user("Hello! How can I assist you today?")
    
    else:
        speak_to_user("Sorry, I don't understand that command.")

def main():
    speak_to_user("Hello, I am your assistant. How can I help you today?")
    
    while True:
        user_input = listen_to_user()
        perform_task(user_input)

if __name__ == "__main__":
    main()
