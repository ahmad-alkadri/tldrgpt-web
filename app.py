import streamlit as st
from src.process import summarize_article

# from src.profiling import message_to_user
st.set_page_config(page_title="TL;DR, GPT?", page_icon="random")

st.title("TL;DR?")

col1, col2 = st.columns(2)
with col1:
    emoji = st.radio("", ["😒", "😊"], horizontal=True)
with col2:
    maxwords = st.number_input("Max. sentences", 20, 100, step=5)

with st.form("sum-submit-url", clear_on_submit=True):
    # st.info(message_to_user(emoji))
    _url = st.text_input(
        "URL input",
        placeholder="https://example.com/",
    )
    _sub = st.form_submit_button("Submit")

if _sub:
    stat_info = st.empty()
    stat_error = st.empty()
    stat_result = st.empty()
    try:
        sumart = summarize_article(_url, stat_info, maxwords, emotion=emoji)

        stat_result.success(sumart)

    except Exception as exce:
        stat_error.error(exce)
        stat_info.empty()
