import time 
import streamlit as st 

def handle_userInput(user_question):
    """ 
    Handling user input 

    Parameters:
    user question  (string) : user prompt to the model 

    Returns:
    Full response  : returns the Full response

    """
    
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']
    
    with st.chat_message("assistant",avatar='🤖'):
        message_placeholder = st.empty()
        full_response = ""
        assistant_response = response['answer']
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant","avatar" :'🤖',"content": full_response})

