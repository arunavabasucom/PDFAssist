import streamlit as st
from dotenv import load_dotenv
from helpers.getPdf import get_pdf_text
from helpers.getchunktext import get_chunk_text
from helpers.getVectorStore import get_vector_store
from helpers.handleUserInput import handle_userInput
from helpers.getConversationChain import get_conversation_chain


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
  
  if "activate_chat" not in st.session_state:
    st.session_state.activate_chat = False
  
  if "messages" not in st.session_state:
    st.session_state.messages = []
    
  for message in st.session_state.messages:
    with st.chat_message(message["role"],avatar=message['avatar']):
        st.markdown(message["content"])
      
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
        st.session_state.activate_chat = True

  if st.session_state.activate_chat == True:  
   if prompt := st.chat_input("What is up?"):
      with st.chat_message("user",avatar='👨🏽'):
        st.markdown(prompt)
      st.session_state.messages.append({"role": "user", "avatar" :'👨🏽',"content": prompt})                
      handle_userInput(prompt)
  else:
     st.write(
       'Pls Upload your file to chat 💬 with those'
     )
  

if __name__ == '__main__':
    main()    
