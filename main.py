import streamlit as st

# MBTI 특성 데이터 예시 (각 유형마다 대표적인 특성 3~4개 제공)
mbti_traits = {
    "INTJ": [
        "전략적이고 계획적",
        "독립적이며 분석적",
        "혁신적이고 미래지향적"
    ],
    "INFP": [
        "이상주의적이고 감성적",
        "공감 능력이 뛰어남",
        "창의적이고 독창적"
    ],
    "ENFP": [
        "열정적이고 창의적",
        "사람들과 금방 친해짐",
        "적응력이 뛰어남"
    ],
    "ESTJ": [
        "실용적이고 조직적",
        "책임감이 강함",
        "지도력이 뛰어남"
    ],
    # 필요한 만큼 추가해주세요
}

st.title("MBTI 특성 안내 앱")

mbti_list = list(mbti_traits.keys())
selected_mbti = st.selectbox("당신의 MBTI 유형을 선택하세요", mbti_list)

if selected_mbti:
    st.subheader(f"{selected_mbti} 유형의 주요 특성")
    for trait in mbti_traits[selected_mbti]:
        st.write("- " + trait)

