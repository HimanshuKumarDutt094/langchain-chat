from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser  # default output from llm
import os
from dotenv import load_dotenv

load_dotenv("../.env")
os.environ["GEMINI_API_KEY"] = os.getenv("GMINI_API_KEY")  # type: ignore
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHANIN_API_KEY")  # type:ignore
# Prompt template
prpmt = ChatPromptTemplate.from_messages(
    [
        ("system", "you are a helpful assistant, response to use queries"),
        ("user", "Question:{question}"),
    ]
)
