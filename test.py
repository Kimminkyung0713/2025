import streamlit as st
import pandas as pd

st.set_page_config(page_title="윤리적 딜레마 체험", page_icon="🤔")

# 딜레마 상황 예시
dilemmas = [
    {
        "title": "트롤리 딜레마",
        "question": "무인 트롤리 열차가 5명을 향해 달리고 있습니다. 당신은 선로를 바꿀 수 있는 위치에 있습니다. 선로를 바꾸면 1명을 희생시켜 5명을 구할 수 있습니다. 어떻게 하시겠습니까?",
        "choices": [
            "선로를 바꿔 1명을 희생하고 5명을 구한다",
            "선로를 그냥 두고 5명이 희생되는 것을 본다"
        ]
    },
    {
        "title": "익명 고발",
        "question": "직장 동료가 회사 규칙을 어기는 것을 발견했습니다. 익명으로 신고할 수 있지만, 동료에게 상처가 될 수 있습니다. 어떻게 하시겠습니까?",
        "choices": [
            "익명으로 신고한다",
            "무시하고 넘어간다"
        ]
    },
    # 필요한 만큼 추가 가능
]

if "result_df" not in st.session_state:
    st.session_state["result_df"] = pd.DataFrame(columns=["dilemma", "choice"])

st.markdown("<h1 style='text-align:center; color:#536dfe;'>💡 윤리적 딜레마 체험 앱</h1>", unsafe_allow_html=True)
st.write("실제와 비슷한 딜레마 상황 속에서 선택을 해보고, 모두의 선택 비율도 실시간으로 확인해보세요.")

# 딜레마 선택
dilemma_titles = [d["title"] for d in dilemmas]
selected_index = st.selectbox("궁금한 상황을 골라보세요.", range(len(dilemma_titles)), format_func=lambda x: dilemma_titles[x])
chosen = dilemmas[selected_index]

st.header(f"🚦 {chosen['title']}")
st.write(chosen["question"])
user_choice = st.radio("당신의 선택은?", chosen["choices"])

user_feedback = st.text_area("이 선택을 하게 된 이유나 소감을 간단히 남겨보세요 (선택사항).", "")

col1, col2 = st.columns([1,3])
with col1:
    if st.button("제출"):
        st.session_state["result_df"] = st.session_state["result_df"].append(
            {"dilemma": chosen["title"], "choice": user_choice}, ignore_index=True)
        st.success("의견이 기록되었습니다!")

with col2:
    df = st.session_state["result_df"]
    dilemma_df = df[df['dilemma'] == chosen['title']]
    if not dilemma_df.empty:
        chart_data = dilemma_df['choice'].value_counts()
        st.bar_chart(chart_data)
    else:
        st.info("아직 결과가 없습니다. 첫 번째로 응답해보세요!")

st.markdown(
    """
    <div style="margin-top:2em; text-align:center; color:#888;">
        ⚖️ 윤리적 딜레마는 정답이 없으며, 다양한 고민과 의견이 모두 존중받아야 합니다.
    </div>
    """,
    unsafe_allow_html=True
)

