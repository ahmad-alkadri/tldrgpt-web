import streamlit as st
import time
from src.textgetter import get_markdown_from_url
from src.query import DocumentQuery

st.set_page_config(page_title="TL;DR, GPT?", page_icon="random")

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.markdown(
    "<h1 style='text-align: center; line-height: 1.5; color: #0D8266'>TL;DR?</h1>", 
    unsafe_allow_html=True)

MAX_MESSAGES = 11
MAX_WORDS_SUMMARY = 50
TIME_DELAY_STREAM = 0.025

# Initiate the text, messages, and user prompts count in session state
if "text" not in st.session_state:
    st.session_state["text"] = ""
if "messages" not in st.session_state:
    st.session_state.messages = []

with st.form("sum-submit-url", clear_on_submit=False):
    _url = st.text_input("URL input", placeholder="https://example.com/")
    _sub = st.form_submit_button("Query")

if _sub and len(_url) > 0:
    st.session_state.messages = []  # Reset the chats
    st.session_state["text"] = get_markdown_from_url(_url)
    if len(st.session_state["text"]) > 0:
        st.session_state["docQuery"] = DocumentQuery(st.session_state["text"])

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == "assistant" and message.get("is_summary", False):
            st.warning(message["content"])
        elif message["role"] == "assistant" and message.get("is_end", False):
            st.info(message["content"])
        else:
            st.markdown(message["content"])
placeInput = st.empty()

if "docQuery" in st.session_state and len(st.session_state["text"]) > 0:
    if len(st.session_state.messages) == 0:
        # Generate and display summary
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            assistant_response = str(
                st.session_state["docQuery"].generate_summary(MAX_WORDS_SUMMARY)
            )
            for chunk in assistant_response.split():
                full_response += chunk + " "
                time.sleep(TIME_DELAY_STREAM)
                message_placeholder.warning(full_response + "▌")
            message_placeholder.warning(full_response)
            st.session_state.messages.append(
                {"role": "assistant", "content": full_response, "is_summary": True}
            )

    
    prompt = placeInput.chat_input(
        "What else do you want to know?"
    )
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Reply to the query
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            if len(st.session_state.messages) < MAX_MESSAGES:
                assistant_response = str(
                    st.session_state["docQuery"].generate_reply(prompt)
                )
                for chunk in assistant_response.split():
                    full_response += chunk + " "
                    time.sleep(TIME_DELAY_STREAM)
                    message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)
                st.session_state.messages.append(
                    {"role": "assistant", "content": full_response}
                )
            else:
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": "You've reached the maximum number of messages for this session. Please refresh the page or input another URL to start a new session.",
                        "is_end": True,
                    }
                )
    if len(st.session_state.messages) >= MAX_MESSAGES:
        placeInput.empty()
        st.info("You've reached the maximum number of messages for this session. Please refresh the page or input another URL to start a new session.")
    