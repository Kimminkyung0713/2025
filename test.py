import streamlit as st

st.set_page_config(page_title="이상형 연예인 월드컵", page_icon="🌟")

# 연예인 데이터: 이름과 이미지 URL (공식/위키피디아 사진 사용 예시)
celebrities = [
    {"name": "아이유", "img": "https://upload.wikimedia.org/wikipedia/commons/3/39/IU_-_LOVE_POEM_album_promo_2.png"},
    {"name": "수지", "img": "https://upload.wikimedia.org/wikipedia/commons/8/85/Suzy_at_a_fansigning_event_in_2019.png"},
    {"name": "박보검", "img": "https://upload.wikimedia.org/wikipedia/commons/6/67/Park_Bogum_TV_hosts.png"},
    {"name": "차은우", "img": "https://upload.wikimedia.org/wikipedia/commons/b/b9/Cha_Eun-woo_at_the_Bulgari_Aurora_Awards_2022_%281%29.png"},
    {"name": "뷔", "img": "https://upload.wikimedia.org/wikipedia/commons/e/e2/V_-_BTS_-_LOVE_YOURSELF_Speak_Yourself_in_London.png"},
    {"name": "임영웅", "img": "https://upload.wikimedia.org/wikipedia/commons/c/c4/Lim_Young-woong_in_2023.png"},
    {"name": "제니", "img": "https://upload.wikimedia.org/wikipedia/commons/b/b5/Jennie_at_LVMH_Awards_2023.png"},
    {"name": "한소희", "img": "https://upload.wikimedia.org/wikipedia/commons/6/69/Han_So_heea.png"},
]

def run_tournament(candidates):
    round = 1
    while len(candidates) > 1:
        st.markdown(f"### {len(candidates)}강 Round {round}")
        winners = []
        for i in range(0, len(candidates), 2):
            c1 = candidates[i]
            c2 = candidates[i+1]
            col1, col2 = st.columns(2)
            with col1:
                st.image(c1["img"], width=220)
                st.write(f"**{c1['name']}**")
            with col2:
                st.image(c2["img"], width=220)
                st.write(f"**{c2['name']}**")
            pick = st.radio("이상형으로 선택!", [c1["name"], c2["name"]], key=f"{round}-{i}")
            winners.append(c1 if pick == c1["name"] else c2)
            st.markdown("---")
        candidates = winners
        round += 1
    return candidates[0]

st.title("🌟 이상형 연예인 월드컵")
st.write("사진과 함께 연예인을 보며 토너먼트를 통해 나의 최종 이상형을 뽑아보세요!")

finalist = run_tournament(celebrities)

st.markdown(f"""
## 🎉 당신의 이상형은?
<div style='display:flex; align-items:center; justify-content:center; font-size:2em; color:#e69cb1; margin-top:0.5em;'>
  <img src="{finalist['img']}" width="180" style="border-radius:16px; margin-right:16px;" />
  <b>{finalist['name']}</b>
</div>
""", unsafe_allow_html=True)

st.markdown("""
---
<div style='text-align:center; color:gray; font-size:small; margin-top:2em;'>
※ 결과는 재미로 하는 개인 선호 투표입니다.
</div>
""", unsafe_allow_html=True)
