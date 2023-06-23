import warnings
import hydra
from omegaconf import  OmegaConf
from PyPDF2 import PdfReader


class PdfProcess:

    def __init__(self,  pdf_docs) -> None:
        self.cfg = OmegaConf.load('./config/main.yaml')
        self.pdf_docs = pdf_docs

    def get_pdf_text(self):
        text = ''
        for pdf in self.pdf_docs:
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                text += page.extract_text()
        return text
    


