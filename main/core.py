from langchain import hub
from langchain_openai import ChatOpenAI
from typing import Dict, Any
from dotenv import load_dotenv
load_dotenv()
import os

os.environ["HTTP_PROXY"] = os.environ['PROXY_URL']
os.environ["HTTPS_PROXY"] = os.environ['PROXY_URL']
Xuan added in 
Xuan added from offline