from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import WebBaseLoader
import bs4
from langchain_community.document_loaders import WikipediaLoader

#loadnig text data form txt file
text_loader = TextLoader('note.txt', encoding='utf-8')
text = text_loader.load()
content = text[0].page_content


#loading data from pdf file
pdf_loader = PyPDFLoader('Davood_Kalami (2).pdf')
pdf_text = pdf_loader.load()
pdf_content = pdf_text[0].page_content

#loading data from web url
web_loader = WebBaseLoader(
    web_paths=("https://archkonnect.ca/about-us",),
    bs_kwargs=dict(parse_only=bs4.SoupStrainer(
        class_=()
    ))
)
web_text = web_loader.load()
web_content = web_text[0].page_content


#loading data from wikipedia
wiki_loader = WikipediaLoader(query='Alvir',load_max_docs=1)
wiki_text = wiki_loader.load()
wiki_content = wiki_text[0].page_content
