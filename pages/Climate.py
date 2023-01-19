import streamlit as st
import pandas as pd 
import requests
import datetime as dt
from PIL import Image
from matplotlib import pyplot as plt
from matplotlib.dates import DayLocator, MonthLocator, YearLocator, WeekdayLocator

st.title("Climate and weather")


st.subheader("Overview")

st.markdown(
    """
    The following Dashboard contains:

    Current weather conditions: temperature, precipitation, wind speed, and humidity.

    Forecasts for the next several days: Expected high and low temperatures, precipitation

    Historical climate data: Average temperatures and precipitation levels, to help the company plan for seasonal variations.

    - Information on extreme weather events, such as heat waves, droughts, and bushfires, to help the company prepare for and respond to potential hazards.
    - Information on water levels, tides, and storms to help the company plan for potential flooding or other hazards.
    - Information on air quality and UV radiation to help the company advise guests on health and safety concerns.
    - Information on local weather conditions such as bushfire, storm, cyclone, to give a heads up to the company and guests to take necessary precautions.
    - Information on climate change, such as long-term temperature and precipitation trends, to help the company plan for potential changes in weather patterns and impacts on the tourism industry.""")

st.info("Note current version uses the freetier of the Open weather API and thus some functionality like live weather alerts are not present future plans include building out this functionality so that UV, bad weather and National weather warnings can be automatically sent out to staff and guests ")

"""Secret file would usualy apply to the api key or any other keys used in making a program for these demonstration purposes this has been left here for ease of access"""
API_KEY = "1869b839201edabd6a70fbd15da79d1f"
data_air = pd.read_csv('./Notebooks/data_air.csv',index_col="date")

def plot_figure():
    interval = st.selectbox("Select Climate Visual", ["Rainfall", "Temparature", "Sea level"])
    if interval == 'Rainfall':
        st.subheader("Rainfall")
        st.image(image="https://www.researchgate.net/profile/Sophie-Zhang-12/publication/287176779/figure/fig1/AS:613880682258432@1523371968011/Trend-in-annual-total-rainfall-in-Australia-19502012-Source.png",output_format='JPEG')
    elif interval == 'Temparature':
        st.subheader("Temperature")
        img=Image.open('./pages/temp_change.jpg')
        st.image(image=img,output_format='JPEG')
    elif interval == 'Sea level':
        st.subheader("Sea level")
        st.image(image="https://www.researchgate.net/profile/Duncan-Rouch/publication/356161201/figure/fig3/AS:1089221557264386@1636702064932/Map-of-Australia-showing-sea-level-change-and-archaeological-sites-for-selected-periods.png",output_format='JPEG')

st.subheader("Climate")
st.markdown("### Climate change over time ")
plot_figure()   

st.subheader("Current temparature")
st.cache()
def find_current_weather(city):
    base_url  = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    weather_data = requests.get(base_url).json()
    try:

        general = weather_data['weather'][0]['main']
        icon_id = weather_data['weather'][0]['icon']
        temperature = round(weather_data['main']['temp'])
        temperature_min = round(weather_data['main']['temp_min'])
        icon = f"http://openweathermap.org/img/wn/{icon_id}@2x.png" 
        description = weather_data['weather'][0]['description']
        wind = weather_data['wind']
        humidity = weather_data['main']['humidity']

    except KeyError:
        st.error("City Not Found")
        st.stop()
    return general,temperature,temperature_min,icon,description,wind,humidity

def weather_forcast(city):
    base_url  = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    weather_data = requests.get(base_url).json()

    lon = weather_data['coord']['lon']
    lat = weather_data['coord']['lat']

    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

    #Let's now parse the JSON
    req = requests.get(url)
    data = req.json()

    return data['list']
 
def main():
    city = st.text_input("Enter the City").lower()
    if st.button("Find"):
        general,temperature,temperature_min,icon, description,wind,humidity = find_current_weather(city)
        col_1,col_2,col_3,col_4 = st.columns(4)
        with col_1:
            st.metric(label = "Temperature",value=f"{temperature}°C")
            st.metric(label = "Night temperature",value=f"{temperature_min}°C")
        with col_2:
            st.write(general)
            st.image(icon)
            st.write(description)
        with col_3:
            st.metric(label = "Wind Speed",value =f"{wind['speed']} km/h")
            st.metric(label = "Wind direction",value =f"{wind['deg']}°")

        with col_4:
            st.metric(label="Humidity", value=humidity)

        
        st.subheader("5 Day Forcasts")
        #5 day forcast 
        data = weather_forcast(city)
        day_1,day_2,day_3,day_4,day_5 = st.columns(5)

        with day_1:
            st.subheader(data[7]["dt_txt"])
            st.write(data[7]['weather'][0]['main'])
            st.metric(label = "Temperature",value=f"{data[7]['main']['temp_max']}°C")
            st.metric(label = "Night temperature",value=f"{data[7]['main']['temp_min']}°C")
            st.image(f"http://openweathermap.org/img/wn/{data[7]['weather'][0]['icon']}@2x.png")
            st.write(data[7]['weather'][0]['description'])
        with day_2:
            st.subheader(data[15]["dt_txt"])
            st.write(data[15]['weather'][0]['main'])
            st.metric(label = "Temperature",value=f"{data[15]['main']['temp_max']}°C")
            st.metric(label = "Night temperature",value=f"{data[15]['main']['temp_min']}°C")
            st.image(f"http://openweathermap.org/img/wn/{data[15]['weather'][0]['icon']}@2x.png")
            st.write(data[15]['weather'][0]['description'])
        with day_3:
            st.subheader(data[23]["dt_txt"])
            st.write(data[23]['weather'][0]['main'])
            st.metric(label = "Temperature",value=f"{data[23]['main']['temp_max']}°C")
            st.metric(label = "Night temperature",value=f"{data[23]['main']['temp_min']}°C")
            st.image(f"http://openweathermap.org/img/wn/{data[23]['weather'][0]['icon']}@2x.png")
            st.write(data[23]['weather'][0]['description'])
        with day_4:
            st.subheader(data[31]["dt_txt"])
            st.write(data[31]['weather'][0]['main'])
            st.metric(label = "Temperature",value=f"{data[31]['main']['temp_max']}°C")
            st.metric(label = "Night temperature",value=f"{data[31]['main']['temp_min']}°C")
            st.image(f"http://openweathermap.org/img/wn/{data[31]['weather'][0]['icon']}@2x.png")
            st.write(data[31]['weather'][0]['description'])
        with day_5:
            st.subheader(data[-1]["dt_txt"])
            st.write(data[-1]['weather'][0]['main'])
            st.metric(label = "Temperature",value=f"{data[-1]['main']['temp_max']}°C")
            st.metric(label = "Night temperature",value=f"{data[-1]['main']['temp_min']}°C")
            st.image(f"http://openweathermap.org/img/wn/{data[-1]['weather'][0]['icon']}@2x.png")
            st.write(data[-1]['weather'][0]['description'])





if __name__ == '__main__':
    main()