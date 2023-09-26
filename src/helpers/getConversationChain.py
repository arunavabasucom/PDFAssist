from langchain.llms import HuggingFaceHub
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

def get_conversation_chain(vector_store, model_option):

    """ 
    Creates conversation chain and returns that 

    Parameters:
    vector_store  (vector) : takes vector store

    Returns:
    Object  : returns the conversation chain with chat history 

    """
    
    
    if model_option == 'gpt-3.5-turbo':
        LLM = ChatOpenAI(model='gpt-3.5-turbo')
    elif model_option == 'flan-t5-xxl':
        LLM = HuggingFaceHub(
            repo_id="google/flan-t5-xxl",
            model_kwargs={"temperature": 0.5, "max_length": 512}
        )
    elif model_option == 'Llama-2-7b':
        LLM = HuggingFaceHub(
            repo_id="meta-llama/Llama-2-70b-chat-hf",
            model_kwargs={"temperature": 0.5, "max_length": 512}
        )
    else:
        raise ValueError("Invalid model_option. Choose from 'gpt-3.5-turbo', 'flant5xxl', or 'llama2'.")
    
    memory = ConversationBufferMemory(
    memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm= LLM,
        retriever=vector_store.as_retriever(),
        memory=memory
    )
    return conversation_chain