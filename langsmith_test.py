from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
langsmith_api_key = os.getenv("LANGSMITH_API_KEY")
langsmith_tracing = os.getenv("LANGSMITH_TRACING")
langsmith_project = os.getenv("LANGSMITH_PROJECT")

print("langsmith is connected successfully.")

prompt = ChatPromptTemplate.from_template("tell me the fun fact about {state}?")
model = ChatOpenAI(model_name="gpt-4o-mini")
chain = prompt | model | StrOutputParser()

print(chain.invoke({"state": "Tamil Nadu"}))
