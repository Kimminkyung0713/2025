import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go

st.set_page_config(page_title="실시간 날씨&미세먼지", layout="wide")

st.title("🌤 오늘과 내일의 실시간 날씨·미세먼지 대시보드")

# OpenWeatherMap API 설정 (본인의 API 키로 교체)
API_KEY = "여기에_본인_API_키_입력하세요"
BASE_URL = "https://api.openweathermap.org/data/2.5/onecall"

# 서울 좌표
lat, lon = 37.5665, 126.9780

params = {
    "lat": lat,
    "lon": lon,
    "exclude": "minutely,hourly,alerts",
    "units": "metric",
    "appid": API_KEY,
    "lang": "kr"
}

res = requests.get(BASE_URL, params=params)
data = res.json()

def parse_daily(day):
    return {
        "날짜": datetime.fromtimestamp(day["dt"]).strftime("%Y-%m-%d"),
        "최고기온": day["temp"]["max"],
        "최저기온": day["temp"]["min"],
        "날씨": day["weather"][0]["description"],
        "습도": day["humidity"],
        "바람": day["wind_speed"],
    }

today = parse_daily(data["daily"][0])
tomorrow = parse_daily(data["daily"][1])

col1, col2 = st.columns(2)
with col1:
    st.subheader("오늘 날씨")
    for k,v in today.items():
        st.write(f"{k}: {v}")
with col2:
    st.subheader("내일 날씨")
    for k,v in tomorrow.items():
        st.write(f"{k}: {v}")

st.markdown("---")

# 미세먼지 예시 데이터 (실제 API 연동 또는 공공데이터 사용 권장)
pm10 = 55  # PM10 농도
pm25 = 30  # PM2.5 농도

st.subheader("서울 미세먼지 정보")
pm10_level = "좋음" if pm10 <= 30 else "보통" if pm10 <= 80 else "나쁨" if pm10 <= 150 else "매우 나쁨"
st.write(f"미세먼지 PM10: {pm10} µg/m³ ({pm10_level})")
st.write(f"초미세먼지 PM2.5: {pm25} µg/m³")

# 미세먼지 변화 그래프
dates = [today["날짜"], tomorrow["날짜"]]
pm10_vals = [pm10, pm10+10]
pm25_vals = [pm25, pm25+5]

fig = go.Figure()
fig.add_trace(go.Bar(name="PM10", x=dates, y=pm10_vals))
fig.add_trace(go.Bar(name="PM2.5", x=dates, y=pm25_vals))
fig.update_layout(barmode='group', yaxis_title='농도 (µg/m³)')
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# 생활 팁 자동 추천
st.subheader("🌟 오늘의 생활 팁")
tips = []
if pm10 > 80:
    tips.append("미세먼지가 나쁠 것으로 예상됩니다. 외출 시 마스크 착용을 권장합니다.")
else:
    tips.append("오늘은 미세먼지가 보통 수준입니다. 야외 활동에 무리가 없습니다.")

if today["최고기온"] > 30:
    tips.append("무더운 날씨이니 물을 충분히 섭취하세요.")
elif today["최고기온"] < 10:
    tips.append("기온이 낮으니 따뜻하게 옷를 입으세요.")

for tip in tips:
    st.write("- " + tip)

st.markdown("---")

# 지도에 서울 위치 표시
st.subheader("서울 위치 지도")
map_df = pd.DataFrame({'lat': [lat], 'lon': [lon]})
st.map(map_df, zoom=11)

st.markdown("""
---
⚠️ OpenWeatherMap API 키는 반드시 본인의 것으로 교체해서 사용하세요.  
미세먼지 데이터는 예시이며 실제 공공 데이터 API를 연동하는 것이 좋습니다.
""")
