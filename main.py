import streamlit as st
import random
from datetime import date

# ⭐️ 화려한 CSS
def local_css(css):
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

custom_css = """
body {
    background: linear-gradient(120deg, #9fd2f6 0%, #f6a2c0 100%);
}
.stApp {
    background: transparent !important;
}
.header {
    font-family: 'Segoe UI', 'Pretendard', sans-serif;
    font-weight: bold;
    font-size: 2.3em;
    letter-spacing: 0.04em;
    text-align: center;
    background: linear-gradient(90deg, #f6a2c0, #9fd2f6, #fffbbc, #a3fdbb);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.2em;
    animation: gradient 3s ease-in-out infinite;
}
@keyframes gradient {
    0% {background-position:0%; }
    100% {background-position:100%;}
}
.zodiac-card {
    background: linear-gradient(120deg, #fffbbc 0%, #a3fdbb 100%);
    border-radius: 18px;
    padding: 24px 20px;
    box-shadow: 0 6px 20px rgba(246,162,192,0.08);
    margin: 2em auto 1em auto;
    max-width: 420px;
    text-align: center;
    transition: box-shadow 0.3s;
}
.zodiac-card:hover {
    box-shadow: 0 12px 40px rgba(159,210,246,0.2);
}
.zodiac-name {
    font-size: 1.5em;
    font-weight: bold;
    margin: 0.2em 0;
}
.zodiac-emoji {
    font-size: 3em;
    margin-bottom: 0.2em;
    animation: twinkle 2.8s infinite;
}
@keyframes twinkle {
    5% { transform: scale(1.2); }
    10% { transform: scale(1); }
}
.zodiac-horoscope {
    font-size: 1.2em;
    margin-top: 0.7em;
    color: #444;
}
.footer {
    padding: 0.7em;
    background: #fff7fc;
    border-radius: 14px;
    margin: 2em auto 0 auto;
    color: #a45ca0;
    text-align: center;
    font-size:1em;
    box-shadow: 0 2px 18px rgba(170,70,160,0.06);
}
"""
local_css(custom_css)

# 별자리 정보 및 emoji
zodiac_info = {
    "물병자리": {"emoji":"♒️", "date":"1/20~2/18"},
    "물고기자리": {"emoji":"♓️", "date":"2/19~3/20"},
    "양자리": {"emoji":"♈️", "date":"3/21~4/19"},
    "황소자리": {"emoji":"♉️", "date":"4/20~5/20"},
    "쌍둥이자리": {"emoji":"♊️", "date":"5/21~6/21"},
    "게자리": {"emoji":"♋️", "date":"6/22~7/22"},
    "사자자리": {"emoji":"♌️", "date":"7/23~8/22"},
    "처녀자리": {"emoji":"♍️", "date":"8/23~9/22"},
    "천칭자리": {"emoji":"♎️", "date":"9/23~10/22"},
    "전갈자리": {"emoji":"♏️", "date":"10/23~11/22"},
    "사수자리": {"emoji":"♐️", "date":"11/23~12/24"},
    "염소자리": {"emoji":"♑️", "date":"12/25~1/19"},
}

# 예시 운세 메시지
horoscopes = {
    "물병자리": [
        "새로운 아이디어가 빛나는 하루! 창의력을 적극적으로 발휘하세요.",
        "예상치 못한 행운이 찾아올 수 있으니 열린 마음을 가져보세요.",
        "친구와의 소통에서 기쁨을 얻는 하루가 되겠습니다."
    ],
    "물고기자리": [
        "감정이 풍부해지는 날, 예술적 활동에 도전해 보세요.",
        "작은 친절이 큰 행운으로 돌아옵니다.",
        "평소보다 직감을 믿어보면 좋은 소식을 들을 수 있어요."
    ],
    "양자리": [
        "에너지가 넘치는 하루! 목표를 적극적으로 추진해보세요.",
        "도전적인 과제가 행운으로 이어집니다.",
        "주변을 밝게 비추는 리더십이 빛나요."
    ],
    "황소자리": [
        "안정과 여유를 느낄 수 있는 시간입니다.",
        "재정적으로 작은 행운이 있을 수 있어요.",
        "잔잔한 하루지만 한 번의 변화가 기회를 줍니다."
    ],
    "쌍둥이자리": [
        "새로운 만남과 소통이 활발해지는 날!",
        "좋은 소식이 예상보다 빨리 찾아옵니다.",
        "호기심이 큰 성과로 이어집니다."
    ],
    "게자리": [
        "가족사랑이 크게 느껴지는 하루입니다.",
        "감성적인 대화에 운이 따릅니다.",
        "자신을 믿고 나아가면 기대 이상의 결과가 찾아옵니다."
    ],
    "사자자리": [
        "자신감이 최고조! 무엇이든 앞장서보세요.",
        "주변에서 주목받는 날, 멋진 인상을 남길 수 있습니다.",
        "작은 선물이나 칭찬이 행운이 됩니다."
    ],
    "처녀자리": [
        "정리정돈이나 계획이 빛나는 시간입니다.",
        "작은 세부사항을 신경 쓰면 운이 따라옵니다.",
        "나눔과 봉사로 좋은 인연을 만날 수 있어요."
    ],
    "천칭자리": [
        "균형 잡힌 판단력으로 인기가 오르는 하루입니다.",
        "주변 사람들과의 협업이 큰 발전을 가져옵니다.",
        "기쁜 소식이나 제안이 들어올 수 있습니다."
    ],
    "전갈자리": [
        "집중력이 빛나며 원하는 목표를 이룰 수 있습니다.",
        "용감한 선택이 행운을 불러옵니다.",
        "내면을 들여다보면 긍정적인 변화를 맞이합니다."
    ],
    "사수자리": [
        "모험심이 샘솟는 하루! 새로운 시도를 하면 행운이 따라옵니다.",
        "여행이나 야외 활동이 기쁜 추억이 됩니다.",
        "재치있는 대화에서 좋은 인상을 남길 수 있습니다."
    ],
    "염소자리": [
        "성실한 노력에 실질적 보상이 따르는 날입니다.",
        "책임감 있게 처리하면 예상 이상의 성과!",
        "목표에 한 걸음 더 다가가는 하루가 될 것입니다."
    ]
}

st.markdown('<div class="header">✨ 별자리별 오늘의 운세 ✨</div>', unsafe_allow_html=True)
st.write("궁금한 별자리를 선택해보세요. 아름다운 카드와 함께 오늘의 운세를 안내합니다!")

zodiac = st.selectbox(
    "별자리를 선택하세요",
    list(zodiac_info.keys()),
    index=random.randint(0,11)
)

# 오늘 날짜 정보
today_str = date.today().strftime("%Y년 %m월 %d일")

if zodiac:
    info = zodiac_info[zodiac]
    emoji = info["emoji"]
    period = info["date"]
    horoscope_str = random.choice(horoscopes[zodiac])
    st.markdown(
        f"""
        <div class="zodiac-card">
            <div class="zodiac-emoji">{emoji}</div>
            <div class="zodiac-name">{zodiac} ({period})</div>
            <div style="color:#888; margin-bottom:0.6em;">{today_str}</div>
            <div class="zodiac-horoscope">{horoscope_str}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    '<div class="footer">💡 별자리 운세는 재미로 보는 콘텐츠입니다. 당신의 하루가 더욱 반짝이길 기원합니다!</div>',
    unsafe_allow_html=True
)
