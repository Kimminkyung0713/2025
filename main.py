import streamlit as st
import requests
import pandas as pd
import plotly.express as px 
from datetime import datetime, timedelta

st.set_page_config(page_title="실시간 날씨 & 미세먼지 대시보드 🎈", layout="wide")

st.title("🌤 오늘 & 내일의 실시간 날씨·미세먼지 정보")

# ====================
# API 키 및 기본 설정 (본인의 API 키로 교체하세요)
API_KEY = "여기에_본인_API_키_입력하세요"
BASE_URL = "https://api.openweathermap.org/data/2.5/onecall"

lat = 37.5665
lon = 126.9780

params = {
    "lat": lat,
    "lon": lon,
    "exclude": "minutely,hourly,alerts",
    "units": "metric",
    "appid": API_KEY,
    "lang": "kr"
}

weather_res = requests.get(BASE_URL, params=params)
weather_data = weather_res.json()

# 미세먼지 데이터 예시 (실제 API 연동 필요)
pm10 = 45  # 미세먼지 (PM10)
pm25 = 28  # 초미세먼지 (PM2.5)

def parse_daily_data(day_data):
    return {
        "날짜": datetime.fromtimestamp(day_data['dt']).strftime('%Y-%m-%d'),
        "최저기온(°C)": day_data['temp']['min'],
        "최고기온(°C)": day_data['temp']['max'],
        "날씨": day_data['weather'][0]['description'],
        "습도(%)": day_data['humidity'],
        "바람속도(m/s)": day_data['wind_speed'],
    }

today_data = parse_daily_data(weather_data['daily'][0])
tomorrow_data = parse_daily_data(weather_data['daily'][1])

col1, col2 = st.columns(2)
with col1:
    st.subheader("오늘의 날씨")
    st.write(f"날짜: {today_data['날짜']}")
    st.write(f"최저기온: {today_data['최저기온(°C)']} °C")
    st.write(f"최고기온: {today_data['최고기온(°C)']} °C")
    st.write(f"날씨: {today_data['날씨']}")
    st.write(f"습도: {today_data['습도(%)']} %")
    st.write(f"바람: {today_data['바람속도(m/s)']} m/s")

with col2:
    st.subheader("내일의 날씨")
    st.write(f"날짜: {tomorrow_data['날짜']}")
    st.write(f"최저기온: {tomorrow_data['최저기온(°C)']} °C")
    st.write(f"최고기온: {tomorrow_data['최고기온(°C)']} °C")
    st.write(f"날씨: {tomorrow_data['날씨']}")
    st.write(f"습도: {tomorrow_data['습도(%)']} %")
    st.write(f"바람: {tomorrow_data['바람속도(m/s)']} m/s")

st.markdown("---")

st.subheader("현재 미세먼지 정보 (서울)")
aqi_level = ""
if pm10 <= 30:
    aqi_level = "좋음"
elif pm10 <= 80:
    aqi_level = "보통"
elif pm10 <= 150:
    aqi_level = "나쁨"
else:
    aqi_level = "매우 나쁨"

st.write(f"미세먼지 (PM10): {pm10} µg/m³ - {aqi_level}")
st.write(f"초미세먼지 (PM2.5): {pm25} µg/m³")

df_pm = pd.DataFrame({
    "날짜": [today_data["날짜"], tomorrow_data["날짜"]],
    "미세먼지(PM10)": [pm10, pm10 + 10],
    "초미세먼지(PM2.5)": [pm25, pm25 + 5],
})

df_temp = pd.DataFrame({
    "날짜": [today_data["날짜"], tomorrow_data["날짜"]],
    "최고기온(°C)": [today_data["최고기온(°C)"], tomorrow_data["최고기온(°C)"]],
    "최저기온(°C)": [today_data["최저기온(°C)"], tomorrow_data["최저기온(°C)"]],
})

st.subheader("미세먼지 농도 변화 그래프")
fig_pm = px.bar(df_pm, x="날짜", y=["미세먼지(PM10)", "초미세먼지(PM2.5)"], barmode='group', labels={"value": "농도(μg/m³)"})
st.plotly_chart(fig_pm)

st.subheader("기온 변화 그래프")
fig_temp = px.line(df_temp, x="날짜", y=["최고기온(°C)", "최저기온(°C)"], markers=True)
st.plotly_chart(fig_temp)

st.markdown("---")

if st.button("생활 팁 보기 🎈"):
    st.balloons()  # 여기에 풍선 터지는 효과
    st.subheader("🌟 오늘의 생활 꿀팁 🌟")
    tips = []
    if aqi_level in ["나쁨", "매우 나쁨"]:
        tips.append("외출 시 마스크를 꼭 착용하세요.")
        tips.append("환기는 자주 하지만, 실내 공기 질 관리에 신경 쓰세요.")
    else:
        tips.append("외출하기 좋은 날씨입니다. 가벼운 산책을 추천해요!")

    if today_data["최고기온(°C)"] >= 30:
        tips.append("더운 날씨이니 충분한 수분을 섭취하세요.")
    elif today_data["최고기온(°C)"] <= 10:
        tips.append("날씨가 쌀쌀하니 따뜻하게 입으세요.")

    for tip in tips:
        st.write(f"- {tip}")

st.subheader("서울 위치 지도")
seoul_map = pd.DataFrame({'lat': [lat], 'lon': [lon]})
st.map(seoul_map, zoom=10)

st.markdown("""
---
⚠️ 본 서비스는 OpenWeatherMap 및 공공 미세먼지 API를 활용합니다.  
실제 API 키와 URL을 반드시 대체하여 사용하세요.
""")
