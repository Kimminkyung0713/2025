import streamlit as st
import pandas as pd

st.set_page_config(page_title="윤리적 딜레마 체험", page_icon="🤔")

# 딜레마 상황 리스트
dilemmas = [
    {
        "title": "트롤리 딜레마",
        "question": "무인 트롤리 열차가 5명을 향해 달리고 있습니다. 당신은 선로를 바꿀 수 있는 위치에 있습니다. 선로를 바꾸면 1명을 희생시켜 5명을 구할 수 있습니다. 어떻게 하시겠습니까?",
        "choices": [
            "선로를 바꿔 1명을 희생하고 5명을 구한다",
            "선로를 그냥 두고 5명이 희생되는 것을 본다"
        ],
    },
    {
        "title": "익명 고발",
        "question": "직장 동료가 회사 규칙을 어기는 것을 발견했습니다. 익명으로 신고할 수 있지만, 동료에게 상처가 될 수 있습니다. 어떻게 하시겠습니까?",
        "choices": [
            "익명으로 신고한다",
            "무시하고 넘어간다"
        ],
    },
]

# 세션 초기화: 결과 저장소
if "result_data" not in st.session_state:
    st.session_state.result_data = []

st.title("💡 윤리적 딜레마 체험 앱")
st.write("현실과 비슷한 딜레마 상황에서 자신의 선택을 하고, 다른 사람들의 선택 비율도 확인해보세요.")

# 딜레마 선택
dilemma_titles = [d["title"] for d in dilemmas]
selected_idx = st.selectbox("관심 있는 상황을 선택하세요", options=range(len(dilemma_titles)), format_func=lambda x: dilemma_titles[x])

current_dilemma = dilemmas[selected_idx]

st.header(f"🚦 {current_dilemma['title']}")
st.write(current_dilemma["question"])

user_choice = st.radio("당신의 선택은?", options=current_dilemma["choices"])

user_feedback = st.text_area("이 선택을 한 이유나 느낌을 적어주세요 (선택사항)", "")

if st.button("제출"):
    if user_choice:
        # 결과 저장 (딜레마 제목, 선택, 피드백)
        st.session_state.result_data.append({
            "dilemma": current_dilemma["title"],
            "choice": user_choice,
            "feedback": user_feedback,
        })
        st.success("응답이 기록되었습니다!")

# 선택 결과 시각화
import pandas as pd

results_df = pd.DataFrame(st.session_state.result_data)
filtered_df = results_df[results_df["dilemma"] == current_dilemma["title"]]

if not filtered_df.empty:
    choice_counts = filtered_df['choice'].value_counts()
    st.bar_chart(choice_counts)
else:
    st.info("아직 결과가 없습니다. 첫 번째 응답자가 되어주세요!")

st.markdown("""
---
<div style='text-align:center; color:gray; font-size:small; margin-top:2em;'>
⚖️ 윤리적 딜레마에는 정답이 없으며, 다양한 의견이 존중받아야 합니다.
</div>
""", unsafe_allow_html=True)
