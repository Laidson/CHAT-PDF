import warnings
import hydra
import os
from omegaconf import DictConfig
from dotenv import load_dotenv
import streamlit as st

from src.text_process import PdfProcess
from src.chunck_processor import ChunkProcess
from src.conversation_process import ChatChain

from htmlTemplates import css, bot_template, user_template

warnings.filterwarnings("ignore")

def get_image_path(image_filename):
    current_directory = os.getcwd()
    image_path = os.path.join(current_directory, 'image_chat', image_filename)
    return image_path

def handle_userinput(user_question):
        response = st.session_state.conversation({'question': user_question})
        #st.write(response)
        st.session_state.chat_history = response['chat_history']

        for i, message in enumerate(st.session_state.chat_history):
            if i % 2 == 0:
                st.write(user_template.replace(
                    "{{MSG}}", message.content), unsafe_allow_html=True)
            else:
                st.write(bot_template.replace(
                    "{{MSG}}", message.content), unsafe_allow_html=True)


def main():


    load_dotenv()    
    st.set_page_config(page_title="Chat with multiple PDFs",
                       page_icon=":robot_face:")
    
    # ADD CSS
    st.write(css, unsafe_allow_html=True)
    
    # conversation check
    if 'conversation' not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    
    st.header("Chat with multiple PDFs :books:")
    user_question = st.text_input("Ask a question about your documents:")
    if user_question:
        handle_userinput(user_question=user_question)

    
    #st.write(user_template.replace('{{MSG}}', 'Hellow, 1'), unsafe_allow_html=True)
    #st.write(bot_template.replace('{{MSG}}', 'Hellow, 2'), unsafe_allow_html=True)

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload your PDFs here and click on 'Process'"
                         , accept_multiple_files=True)
        
        if st.button("Process"):
            with st.spinner('Processing...'):
                # step 1 - get_pdf text
                pdf_process = PdfProcess(pdf_docs=pdf_docs)
                raw_text = pdf_process.get_pdf_text()
                st.write(raw_text)
                
                # step 2 - get text chunks
                chunk_process = ChunkProcess(raw_text)
                txt_chunks = chunk_process.get_text_chunks()
                st.write(txt_chunks)

                # step 3 -create vector store
                vectorestore = chunk_process.get_embeddings_vectorstore()

                # step 4 - create conversation chain
                chat = ChatChain(vectorstore=vectorestore)
                st.session_state.conversation = chat.get_conversation_chain() 
    
            
            
    

if __name__ == '__main__':
    main()