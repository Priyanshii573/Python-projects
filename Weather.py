import tkinter as tk
from tkinter import ttk
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")

        self.api_key = "ab5e37bf56a894b3eaa7fd1424d6d84b"  # Replace with your OpenWeatherMap API key

        self.city_label = ttk.Label(root, text="Enter city name:")
        self.city_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.city_entry = ttk.Entry(root, width=30)
        self.city_entry.grid(row=0, column=1, padx=10, pady=5)
        self.get_weather_button = ttk.Button(root, text="Get Weather", command=self.get_weather)
        self.get_weather_button.grid(row=0, column=2, padx=10, pady=5)

        self.weather_info_label = ttk.Label(root, text="")
        self.weather_info_label.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

    def get_weather(self):
        city = self.city_entry.get()
        if not city:
            self.weather_info_label.config(text="Please enter a city name.")
            return

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather_info = f"Weather in {city}:\n"
            weather_info += f"Temperature: {data['main']['temp']}°C\n"
            weather_info += f"Description: {data['weather'][0]['description']}\n"
            weather_info += f"Humidity: {data['main']['humidity']}%\n"
            weather_info += f"Wind Speed: {data['wind']['speed']} m/s"

            self.weather_info_label.config(text=weather_info)
        else:
            self.weather_info_label.config(text="City not found. Please enter a valid city name.")

def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
