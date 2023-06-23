import warnings
import hydra
from omegaconf import  OmegaConf

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.llms import HuggingFaceHub
from langchain.llms import GPT4All


class ChatChain:

    def __init__(self, vectorstore) -> None:
        self.cfg = OmegaConf.load('./config/main.yaml')
        self.vectorstore = vectorstore

    def get_conversation_chain(self):
        model_supplier = self.cfg.model_supplier

        if model_supplier == 'OPENAI':
            llm = ChatOpenAI(model_name="gpt-3.5-turbo")

        if model_supplier == 'HUGGINGFACE':
            parms = self.cfg.HuggingFaceHub
            llm = HuggingFaceHub(repo_id=parms.repo_id, 
                                 model_kwargs={"temperature":parms.model_temperature, 
                                               "max_length":parms.model_length})
        if model_supplier == 'GPT4All':
            parms = self.cfg.gpt4all
            llm = GPT4All(model=parms.model,
                          n_ctx=parms.n_ctx,
                          backend=parms.backend,
                          verbose=parms.verbose)

        memory = ConversationBufferMemory(memory_key=self.cfg.memory.memory_key, 
                                          return_messages=self.cfg.memory.return_messages)
        
        conversational_chain = ConversationalRetrievalChain.from_llm(llm=llm,
                                                                     retriever=self.vectorstore.as_retriever(),
                                                                     memory=memory)
        
        return conversational_chain
    