import openai
import speech_recognition as sr
import pyttsx3

openai.api_key = "YOUR-API-KEY"

def get_api_response(prompt: str) -> str:
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        temperature=0.9,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=None
    )
    return response.choices[0].text.strip()

def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Say something!")
        while True:
            try:
                audio = recognizer.listen(source)
                user_input = recognizer.recognize_google(audio)
                print(f"You: {user_input}")

                prompt = f"You: {user_input}\nBot:"
                bot_response = get_api_response(prompt)
                print(f"Bot: {bot_response}")

                engine = pyttsx3.init()
                voices = engine.getProperty('voices')
                engine.setProperty('voice', voices[1].id)  # Index 1 represents a female voice
                engine.say(bot_response)
                engine.runAndWait()

            except sr.UnknownValueError:
                print("Sorry, I didn't understand. Could you please repeat?")
            except sr.RequestError:
                print("Sorry, there was an issue with the speech recognition service.")

if __name__ == '__main__':
    main()
