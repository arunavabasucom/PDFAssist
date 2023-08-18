from langchain.text_splitter import CharacterTextSplitter

def get_chunk_text(text):
    text_spliter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_spliter.split_text(text)
    return chunks