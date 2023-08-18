import streamlit as st
from dotenv import load_dotenv
from helpers.getPdf import get_pdf_text
from helpers.getchunktext import get_chunk_text
from helpers.getVectorStore import get_vector_store
from helpers.getConversationChain import get_conversation_chain
from htmlTemplates import css,bot_template,user_template

def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']
  
    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 != 0:
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                message_placeholder.markdown(message.content + "▌")
            message_placeholder.markdown(message.content)  # Moved this line inside the 'with' block
            st.session_state.messages.append({"role": "assistant", "content": message.content})  # Moved this line inside the 'with'         
  


def main():
  load_dotenv()
  st.set_page_config(
    page_title="DocAssist",
    page_icon=":Book:"
  )
  
  st.header('📖 DocAssist')
  st.subheader('Chat with multiple DOCs')
  
  if "conversation" not in st.session_state:
    st.session_state.conversation = None
  
  if "messages" not in st.session_state:
    st.session_state.messages = []

  for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


  
  if prompt := st.chat_input("What is up?"):
      st.session_state.messages.append({"role": "user", "content": prompt})          
      with st.chat_message("user"):
        st.markdown(prompt)
      handle_userinput(prompt)
  #     with st.chat_message("assistant"):
  #       response = st.session_state.conversation({'question': prompt})
  #       st.session_state.chat_history = response['chat_history']
  #       with st.chat_message("assistant"):
  #           message_placeholder = st.empty()
  #           message_placeholder.markdown(message.content + "▌")
  #       message_placeholder.markdown(message.content)  # Moved this line inside the 'with' block
  # st.session_state.messages.append({"role": "assistant", "content": message.content})  # Moved this line inside the 'with'           
  
  
  with st.sidebar:
    st.subheader('Your Documents')
    docs = st.file_uploader('Upload your DOCs and click to process'
                     ,accept_multiple_files=True
                     )
    if st.button('Process'):
      with st.spinner('Processing'):
        # get the docs
        raw_text = get_pdf_text(docs)
        # get the text chunks 
        chunk_text = get_chunk_text(raw_text)      
        # create vector store 
        vector_store = get_vector_store(chunk_text)
        # create conversation chain
        st.session_state.conversation = get_conversation_chain(vector_store)
        
if __name__ == '__main__':
    main()    