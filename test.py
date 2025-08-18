import streamlit as st
import random

st.set_page_config(page_title="감성 상담 챗봇", page_icon="🌱")

# 위로 메시지 리스트(간단 예시, 마음에 드는 문장 추가 가능)
comfort_messages = [
    "당신의 감정은 소중해요. 오늘을 잘 견디는 것만으로도 충분히 잘하고 있습니다.",
    "힘든 순간이 오면 스스로를 꼭 안아주세요. 당신은 혼자가 아닙니다.",
    "마음이 지칠 때 잠시 숨을 쉬어도 괜찮아요.",
    "누군가에게 털어놓고 싶은 생각이 있다면 용기 내어 표현해보세요.",
    "지금 느끼는 감정은 언젠가 지나가요. 당신의 하루가 더 따스해지길 바라요.",
    "오늘도 수고했어요! 잠깐이라도 자신을 칭찬하고 힘내세요.",
    "모든 존재는 소중하니까, 당신도 분명히 소중해요.",
    "마음이 아프다면 잠시 쉴 자격이 충분해요.",
    "어떤 선택도 옳을 수 있고, 실수해도 괜찮아요.",
    "지금의 당신, 충분히 사랑받을 가치가 있어요."
]

st.title("🌱 감성 상담 챗봇")
st.write("마음이 힘들거나, 위로가 필요할 때 기분이나 고민을 편하게 입력해보세요.")

user_input = st.text_area("지금 고민이나 기분을 자유롭게 적어주세요.", "")

if user_input:
    st.markdown("---")
    st.subheader("상담 도우미의 메시지")
    msg = random.choice(comfort_messages)
    st.write(f"💌 {msg}")

st.markdown("""
---
<div style='text-align:center; color:gray; margin-top:2em; font-size:small;'>
이 앱은 따뜻한 위로와 감성적 상담을 위해 만들어졌으며, 전문적인 의료 상담은 아닙니다.<br>진심으로 힘든 경우에는 주변 전문가와도 상담해보세요.
</div>
""", unsafe_allow_html=True)
