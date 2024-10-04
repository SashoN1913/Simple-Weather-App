import openai
import requests

openai.api_key = 'For test put your api key'

weather_api_key = 'For test put your weather api key'
weather_url = "http://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        'q': city,
        'appid': weather_api_key,
        'units': 'metric'
    }
    response = requests.get(weather_url, params=params)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        return temperature
    else:
        return None

def get_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].message['content'].strip()


def main():
    print("Welcome to the weather chatBot!")
    print("Enter a city name. Type exit to finish the program")

    while True:
        user_input = input("You:  ")
        if user_input.lower() == 'exit':
            print("ChatBot: Bye!")
            break

        temperature = get_weather(user_input)
        if temperature is not None:
            print(f"ChatBot: Temperature in {user_input} е {temperature}°C.")
        else:
            print("ChatBot: I couldn't find information for this city. Please try again.")


if __name__ == "__main__":
    main()
