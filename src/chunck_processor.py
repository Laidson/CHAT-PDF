import warnings
import hydra
from omegaconf import  OmegaConf

from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS


class ChunkProcess:

    def __init__(self, raw_text) -> None:
        self.cfg = OmegaConf.load('./config/main.yaml')
        self.raw_text = raw_text
        self.txt_chunks = None


    def get_text_chunks(self):
        txt_splitter = CharacterTextSplitter(separator= self.cfg.chunks_spliter.separator,
                                            chunk_size= self.cfg.chunks_spliter.chunk_size,
                                            chunk_overlap= self.cfg.chunks_spliter.chunk_overlap,
                                            length_function= len
                                            )
        self.txt_chunks = txt_splitter.split_text(self.raw_text)

        return self.txt_chunks
    
    def get_embeddings_vectorstore(self):

        model_supplier = self.cfg.vector_store.vector_supplier

        if model_supplier == 'OPENAI':
            embeddings = OpenAIEmbeddings()
        
        if model_supplier == 'HUGGINGFACE':
            embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
                
        else:
            print('ERROR - Embedding supplier not supported')
            
        vectorstore = FAISS.from_texts(texts=self.txt_chunks, embedding=embeddings)
        return vectorstore
                    
    
# if __name__ == '__main__':
#     raw_text = 'KKKKKKKKKKKK'
#     process = ChunkProcess(raw_text)
#     process.get_text_chunks()
#     process.get_embeddings_vectorstore()