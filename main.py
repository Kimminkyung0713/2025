import streamlit as st
import requests
from datetime import datetime

st.title("👗 날씨 기반 옷차림 추천기")

# OpenWeatherMap API 키 입력 (자신의 키로 교체)
API_KEY = "여기에_본인_API_키_입력하세요"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# 서울 좌표
lat, lon = 37.5665, 126.9780

params = {
    "lat": lat,
    "lon": lon,
    "appid": API_KEY,
    "units": "metric",
    "lang": "kr"
}

res = requests.get(BASE_URL, params=params)
data = res.json()

if res.status_code == 200:
    temp = data["main"]["temp"]
    weather_desc = data["weather"][0]["description"]
    st.write(f"현재 서울 날씨: {weather_desc}, 온도: {temp}°C")

    st.subheader("오늘의 옷차림 추천")
    if temp >= 28:
        st.write("가볍고 시원한 반팔이나 반바지를 추천해요. 모자와 선글라스도 챙기세요!")
    elif 20 <= temp < 28:
        st.write("긴팔셔츠나 얇은 가디건이 적당해요.")
    elif 10 <= temp < 20:
        st.write("가벼운 자켓이나 니트가 좋습니다.")
    elif 0 <= temp < 10:
        st.write("두꺼운 코트나 패딩을 입는 것이 좋아요.")
    else:
        st.write("무척 춥습니다. 두꺼운 패딩에 목도리, 장갑 꼭 챙기세요!")

else:
    st.write("날씨 정보를 불러오는 데 실패했습니다. API 키를 확인해주세요.")
