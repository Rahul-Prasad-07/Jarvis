import openai 
from dotenv import dotenv_values
# text to speach library
import pyttsx3  

# for speech recognition
import speech_recognition as sr

env_vars = dotenv_values(".env")
openai.api_key = env_vars['API_KEY']


# text to speach

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


# speech to text
def audioTOtext():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en_IN')   #Using google for voice recognition.
       # query=r.recognize_google(audio,language='hi-IN')  #Using google for voice recognition.hi-IN
        return query
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    


def askJarvis(question):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        temperature=0.3,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0.6,
       
    )
    data = response.choices[0].text
    return data.strip()


while True:
    inputText = audioTOtext()
    print(inputText)

    if inputText.lower() == "stop" or inputText.lower() == "exit":
        speak("Thank you for using Jarvis. Have a nice day! Mr Rahul")
        break
     
    
    outputText = askJarvis(inputText)
    print(outputText)
    speak(outputText)



# while True:
#     query = input(" Ask a question: from jarvis:")
#     Ans = askJarvis(query)
#     print(Ans + "\n")

# speak("Hello, I am Jarvis, your personal assistant. How can I help you?")
   
