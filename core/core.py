from langchain import hub
from langchain_openai import ChatOpenAI
from typing import Dict, Any
from dotenv import load_dotenv
load_dotenv()
import os

os.environ["HTTP_PROXY"] = os.environ['PROXY_URL']
os.environ["HTTPS_PROXY"] = os.environ['PROXY_URL']

def agent(question: str, context : str) -> Dict:
    llm= ChatOpenAI(temperature=0, model = "gpt-4-turbo")
    prompt = hub.pull("rlm/rag-prompt")
    chain = prompt | llm
    res = chain.invoke(input = {
        "question" : question,
        "context" : context
    })

    return res.content

if __name__ == "__main__":
    question = "Who is Elon Musk?"
    context = ""
    print(agent(question= question, context= context))