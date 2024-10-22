import requests
import pandas as pd
import matplotlib.pyplot as plt
import datetime

API_Key = '64f8aac6bd6cca475f38082e33ab7949'
CITY = 'Pune'
BASE_URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_Key}&units=metric'

# OpenAQ API endpoint for fetching air quality data
AIR_QUALITY_API = 'https://api.openaq.org/v1/latest'

def fetch_aqi_data(api_key, city, start, end):
    # Get latitude and longitude for the city
    geo_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}'
    geo_response = requests.get(geo_url)
    geo_data = geo_response.json()
    if len(geo_data) == 0:
        raise ValueError(f"City {city} not found")
    
    lat = geo_data[0]['lat']
    lon = geo_data[0]['lon']
    
    url = f'http://api.openweathermap.org/data/2.5/air_pollution/history?lat={lat}&lon={lon}&start={start}&end={end}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

# Define the start and end timestamps for historical data (example: last 7 days)
end_time = int(datetime.datetime.now().timestamp())
start_time = end_time - (7 * 24 * 60 * 60)  # 7 days aga


def process_aqi_data(data):
    records = []
    for item in data['list']:
        dt = datetime.datetime.fromtimestamp(item['dt'])
        aqi = item['main']['aqi']
        components = item['components']
        record = {
            'datetime': dt,
            'aqi': aqi,
            **components
        }
        records.append(record)
    return pd.DataFrame(records)

aqi_df = process_aqi_data(aqi_data)

# Plot AQI over time
plt.figure(figsize=(12, 6))
plt.plot(aqi_df['datetime'], aqi_df['aqi'], marker='o', linestyle='-')
plt.title(f'Air Quality Index (AQI) in {CITY}')
plt.xlabel('Date')
plt.ylabel('AQI')
plt.grid(True)
plt.show()





# # Fetch AQI data
# aqi_data = fetch_aqi_data(API_KEY, CITY, start_time, end_time)


# # Fetching the weather data
# response = requests.get(BASE_URL)
# data = response.json()

# # Extracting relevant information
# if response.status_code == 200:
#     temperature = data['main']['temp']
#     humidity = data['main']['humidity']
#     description = data['weather'][0]['description']
#     timestamp = datetime.now()

#     print(f"Temperature: {temperature}°C")
#     print(f"Humidity: {humidity}%")
#     print(f"Weather Description: {description}")
# else:
#     print("Error fetching data from OpenWeather API")

# # Creating a simple plot (example: temperature and humidity)
# # For demonstration, we will create a simple static plot with the fetched data.
# plt.figure(figsize=(10, 5))
# plt.bar(['Temperature (°C)', 'Humidity (%)'], [temperature, humidity], color=['blue', 'orange'])
# plt.title(f'Current Weather in {CITY}')
# plt.ylabel('Value')
# plt.xticks(rotation=45)
# plt.grid(axis='y')
# plt.show()

# def get_air_quality_data(city, days):
#     air_quality_data = []
#     for i in range(days):
#         date = (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d')
#         params = {
#             'city': city,
#             'date': date
#         }
#         response = requests.get(AIR_QUALITY_API, params=params)
#         data = response.json()
#         if data['results']:
#             pm25 = data['results'][0]['measurements'][0]['value']
#             air_quality_data.append((date, pm25))
#     return air_quality_data

# def plot_air_quality_data(air_quality_data):
#     dates = [x[0] for x in air_quality_data]
#     pm25_values = [x[1] for x in air_quality_data]
#     plt.figure(figsize=(10, 5))
#     plt.plot(dates, pm25_values, marker='o')
#     plt.title(f'Air Quality (PM2.5) in {CITY} over the last {len(dates)} days')
#     plt.xlabel('Date')
#     plt.ylabel('PM2.5 (μg/m³)')
#     plt.grid(True)
#     plt.show()

# air_quality_data = get_air_quality_data(CITY, 5)
# plot_air_quality_data(air_quality_data)