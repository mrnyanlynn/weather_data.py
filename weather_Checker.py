
import customtkinter as ctk
import requests


def get_weather():
    city = entry.get()
    api_key = '9fd856f2f1a34c8976bf638c86d42ae7'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city},&appid={api_key}'

    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()

        temperature = weather_data['main']['temp']
        temp_in_C = round(temperature - 273.15, 2)
        temp_in_F = round((temp_in_C * 9 / 5) + 32, 2)

        description = weather_data['weather'][0]['description']
        result_label.configure(
            text=f"Current weather in {city}: {description}, Temperature={temp_in_C}°C or {temp_in_F}°F ")
    elif response.status_code == 400:
        result_label.configure(text="City not found, please check the name.")
    else:
        result_label.configure(text="Error fetching weather data")


window = ctk.CTk()
window.geometry("600x400")
ctk.set_appearance_mode("dark")
window.title("Weather Checker")

title_label = ctk.CTkLabel(window, text="Enter City",font=ctk.CTkFont(size=20, weight="bold"))
title_label.pack(pady=20)

entry = ctk.CTkEntry(window, width=200)
entry.pack(pady=10)

get_button = ctk.CTkButton(window, text="Get Weather Data",command=get_weather)
get_button.pack(pady=20)

result_frame = ctk.CTkFrame(window, width=800, height=100)
result_frame.pack(pady=10)

result_label = ctk.CTkLabel(result_frame, text="",font=ctk.CTkFont(size=13))
result_label.pack(pady=20)

window.mainloop()

