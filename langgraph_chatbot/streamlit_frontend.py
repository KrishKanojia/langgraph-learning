import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage

CONFIG = {"configurable" : {"thread_id" : "thread_1"}}

# st.session state -> dict -> which store convo message after re execution of this page 
if 'message_history' not in st.session_state:
    st.session_state["message_history"]  = []


# loading history message
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message["content"])

user_input = st.chat_input("Type here")

if user_input:
    # First add user message
    st.session_state['message_history'].append({"role" : "user", "content" : user_input})
    with st.chat_message("user"):
        st.text(user_input)
       
    # Add AI message
    response = chatbot.invoke({"messages":  [HumanMessage(content=user_input)]}, config=CONFIG)
    message = response["messages"][-1].content
    print("AI MESSAGES", response)
    st.session_state['message_history'].append({"role" : "assistant", "content" : message})
    with st.chat_message("assistant"):
        st.text(message)