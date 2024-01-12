import random
import json
import urllib.request
import googletrans
import requests
import config


def markdown_code_block(code, language):
    return f'```{language}\n{code}\n```'


def translate_description(description):
    translator = googletrans.Translator()
    return translator.translate(description, dest='de', src='en').text


def random_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return 'rgb({}, {}, {})'.format(r, g, b)


def random_hex():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return '#{0:02x}{1:02x}{2:02x}'.format(r, g, b)


def decimal_to_hex(decimal_number):
    hex_number = hex(decimal_number).replace("0x", "")
    return markdown_code_block(f"hex({hex_number}", "")


def decimal_to_binary(decimal):
    return markdown_code_block(bin(decimal).replace("0b", ""), "")


def iss():
    try:

        url = "http://api.open-notify.org/iss-now.json"
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())
    except:
        return "Fehler"

    try:

        url2 = "http://api.open-notify.org/astros.json"
        response2 = urllib.request.urlopen(url2)
        result2 = json.loads(response2.read())
    except:
        return "Fehler"

    asto = result2["number"]
    people = result2["people"]

    location = result["iss_position"]
    lat = location['latitude']
    lon = location['longitude']

    mess = f"ISS:\n   Position:\n   {lat},  {lon}\n \nAstronouts({asto}):\n"

    for name in people:
        mess += ("    " + name["name"] + " on: " + name["craft"] + "\n")
    return markdown_code_block(mess, "")


def fetch_weather_data():
    try:
        url = "https://api.openweathermap.org/data/2.5/weather?lat=49.94075694090485&lon=11.598245891210388&appid={}".format(
            config.getOpenWeatherKey())
        response = urllib.request.urlopen(url)
        return json.loads(response.read())

    except:
        return ""


def wether():
    weather_data = fetch_weather_data()

    try:

        if weather_data["cod"] == 200:
            temp_in_kelvin = (weather_data['main']['temp'])
            temp_in_celsius = round(temp_in_kelvin - 273.15, 2)
            pressure = weather_data['main']['pressure']
            humidity = weather_data['main']['humidity']
            description = weather_data['weather'][0]['description']
            translated_description = translate_description(description)
            wind_speed = weather_data['wind']['speed']
            visibility = weather_data["visibility"]

            return (f"Das Wetter:\n\n"
                    f"Die Wetterlage ist {translated_description} (keine Garantie auf richtige übersetzung)\n"
                    f"Die Temperatur beträgt {temp_in_celsius} °C\n"
                    f"Der Luftdruck beträgt {pressure} hPa\n"
                    f"Die Luftfeuchtigkeit beträgt {humidity}  %\n"
                    f"Die Windgeschwindigkeit beträgt momentan {wind_speed} m/s\n"
                    f"Du kannst {visibility}m weit aus dem fenster schuen")

        else:
            return "Fehler biem lesen der Wetterlange"
    except:
        return "Fehler"


def joke():
    url = "https://dad-jokes.p.rapidapi.com/random/joke"

    headers = {
        "X-RapidAPI-Host": "dad-jokes.p.rapidapi.com",
        "X-RapidAPI-Key": config.getJokeKey()
    }

    try:
        response = requests.request("GET", url, headers=headers)
        data = json.loads(response.content)

    except:
        return "Fehler API no resoponse"

    mess1 = data['body'][0]['setup']
    mess2 = data['body'][0]['punchline']

    return mess1 + "\n\n" + mess2
