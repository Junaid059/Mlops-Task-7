import requests
import pandas as pd

# Replace with your actual OpenWeatherMap API key
API_KEY = "318c23524b8fe1635e254ff75b285015"  # Replace this with your key

# API endpoint for current weather data (v2.5)
URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather_data(lat=51.5074, lon=-0.1278):  # Default to London coordinates
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric"  # To get temperature in Celsius
    }
    
    # Send request to the OpenWeatherMap API
    response = requests.get(URL, params=params).json()
    
    # Print the response for debugging
    print(response)
    
    # Check if there was an error in the response
    if 'cod' in response and response['cod'] != 200:
        print(f"Error: {response.get('message', 'Unknown error')}")
        return
    
    # Extract the relevant weather data
    weather_data = {
        "date_time": pd.to_datetime("now").strftime('%Y-%m-%d %H:%M:%S'),
        "temperature": response['main']['temp'],
        "humidity": response['main']['humidity'],
        "wind_speed": response['wind']['speed'],
        "weather_condition": response['weather'][0]['description']
    }
    
    # Convert the data to a DataFrame
    df = pd.DataFrame([weather_data])
    
    # Save data to CSV
    df.to_csv("data/raw_data.csv", index=False)
    print("Weather data saved to data/raw_data.csv")

if __name__ == "__main__":
    # Example: Fetch weather for a specific latitude and longitude (e.g., London)
    fetch_weather_data(lat=51.5074, lon=-0.1278)
