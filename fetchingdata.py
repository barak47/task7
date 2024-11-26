import requests
import pandas as pd
from datetime import datetime

api_key = "your_api_key"
url = f"http://api.openweathermap.org/data/2.5/weather?q=YourCity&appid={api_key}"

response = requests.get(url).json()
data = {
    'Temperature': response['main']['temp'],
    'Humidity': response['main']['humidity'],
    'Wind Speed': response['wind']['speed'],
    'Weather Condition': response['weather'][0]['description'],
    'Date': datetime.now().date(),
    'Time': datetime.now().time()
}
weather_df = pd.DataFrame([data])
weather_df.to_csv('raw_data.csv', index=False)
