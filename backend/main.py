from fastapi import FastAPI, Form
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI  
from langchain.schema import HumanMessage
import os

load_dotenv()

app = FastAPI()

llm = ChatOpenAI(openai_api_key=os.getenv("openai_api_key"),
                model_name=os.getenv("model_name"),
                openai_api_base=os.getenv("openai_api_base"),
                default_headers={"HTTP-Referer": os.getenv("default_headers")})


@app.get("/")
def root():
    return {"message": "FastAPI running. Go to /docs."}

@app.post("/ask")
async def ask(question: str = Form(...), content: str = Form(...)):
    prompt = f"{content}\n\nQuestion: {question}"
    response = llm.invoke([HumanMessage(content=prompt)])
    return {"answer": response.content}