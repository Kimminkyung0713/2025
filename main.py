import streamlit as st

# 매력적인 CSS 스타일 적용
def local_css(css_text):
    st.markdown(f'<style>{css_text}</style>', unsafe_allow_html=True)

custom_css = """
body {
    background: linear-gradient(135deg, #f4f0ff 0%, #e1f7fa 100%);
}
.stApp {
    background: transparent !important;
}
.header {
    font-weight:bold;
    font-size:2.3em;
    background: -webkit-linear-gradient(#6a81f7, #2ec9db);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.2em;
}
.card {
    background: white;
    border-radius: 18px;
    padding: 24px 18px;
    box-shadow: 0 4px 20px rgba(90,92,207,0.07);
    margin-bottom: 1em;
    transition: 0.25s;
}
.card:hover {
    box-shadow: 0 8px 32px rgba(46,201,219,0.18);
}
.mbti-title {
    font-size: 1.3em;
    font-weight: bold;
    margin-bottom: 0.15em;
}
.mbti-emoji {
    font-size: 2em;
    vertical-align: middle;
    margin-right: 0.3em;
}
.mbti-detail {
    font-size:1.1em;
    color:#555;
}
"""

local_css(custom_css)

# MBTI 특성 데이터 (간단 핵심, emoji 포함)
mbti_traits = {
    "ISTJ": ("🧭", "신중하고 책임감 있는 관리자형", "믿음직하며 체계적인 현실주의자. 안정과 질서, 꼼꼼함을 중시."),
    "ISFJ": ("🛡️", "조용하고 헌신적인 수호자형", "따뜻하고 온정적인 배려자. 주변을 잘 챙기고 헌신적."),
    "INFJ": ("🌱", "통찰력 있고 이상주의적인 조언자형", "깊은 직관과 통찰, 다른 사람을 돕는 데 큰 관심."),
    "INTJ": ("🕵️", "전략적이고 독립적인 설계자형", "논리적이고 분석적인 계획가. 혁신과 미래지향적 판단."),
    "ISTP": ("🛠️", "현실적이고 분석적인 장인형", "문제해결에 탁월, 실용적이고 자유로운 성향."),
    "ISFP": ("🎨", "따뜻하고 조용한 예술가형", "감성적이고 겸손, 예술적 소질이 뛰어난 타입."),
    "INFP": ("🧚‍♂️", "이상을 좇는 중재자형", "창의적이고 내향적, 가치를 중시하며 감정이 풍부."),
    "INTP": ("🧠", "논리적이고 창의적인 사색가형", "호기심 많고 논리적. 새로운 아이디어를 좋아함."),
    "ESTP": ("🏃‍♂️", "에너지 넘치고 즉흥적인 활동가형", "스릴을 추구, 현실적이고 활동적이며 도전적."),
    "ESFP": ("🎉", "사교적이고 감각적인 연예인형", "즉흥적이며 에너지가 넘치고 사회적. 분위기 메이커."),
    "ENFP": ("🔥", "열정적이고 자유로운 활동가형", "창의적, 호기심이 많고 사람들과 쉽게 친해짐."),
    "ENTP": ("💡", "재치 있고 창의적인 발명가형", "변화와 새로운 아이디어를 즐기며 토론을 좋아함."),
    "ESTJ": ("🏅", "현실적이고 조직적인 관리자형", "계획적이고 단호함, 지도력이 강함."),
    "ESFJ": ("🤗", "친절하고 사교적인 보호자형", "화합을 중시하며 협력적이고 친절한 성향."),
    "ENFJ": ("🌟", "타인을 이끄는 외향적인 조언자형", "분위기 리더, 공감과 소통에 능함."),
    "ENTJ": ("🚀", "리더십 강한 전략가형", "목표 지향적이며 추진력이 뛰어난 리더."),
}

st.markdown('<div class="header">🌈 오늘의 MBTI 성격특성 카탈로그</div>', unsafe_allow_html=True)
st.write("16가지 MBTI 유형 중 하나를 선택하면 주요 특성을 카드로 보여줍니다.")

chosen = st.selectbox(
    "MBTI 유형을 선택해 주세요",
    options=list(mbti_traits.keys()),
    index=0
)

if chosen:
    emoji, title, detail = mbti_traits[chosen]
    st.markdown(
        f"""
        <div class="card">
            <span class="mbti-emoji">{emoji}</span>
            <span class="mbti-title">{chosen} - {title}</span>
            <div class="mbti-detail">{detail}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# 하단에 귀여운 설명 박스 추가
st.markdown(
    """
    <div style="padding:0.7em; background:#edf5ff; border-radius:14px; margin-top:2em; text-align:center; color:#535c65;">
        📝 MBTI는 자기 이해와 인간관계에 도움을 주는 참고 도구입니다.<br>
        여러 유형이 있지만 모두 고유한 매력이 있습니다!
    </div>
    """,
    unsafe_allow_html=True
)

# 깔끔한 앱 레이아웃 팁
st.caption("본 코드는 커스텀 CSS, emoji, HTML, Streamlit 기본 레이아웃을 모두 활용하였습니다.")

