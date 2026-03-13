from http import client
from langchain_openai  import ChatOpenAI
from langchain_openai  import OpenAIEmbeddings
import openai

from backend import app


# Set your OpenAI API key here or use environment variable
base_url="https://platform.openai.com/docs/api-reference/cha"
api_key = "sk-xcC3RS-FbPCheSCR1AY0BA"
headers={"Content-Type":"application/json" ,
"Authorization": "Bearer {sk-hpIfTuJBNlRhyw1_L5vD4Q}" }
{
    "model": "gpt-4o",
    "messages": [
        {
            "role": "user",
            "content": "Hello!"
        }
    ]
}
# DON'T EDIT THIS FILE - COPY to your local and start working

llm = ChatOpenAI(
    base_url="https://platform.openai.com/docs/api-reference/cha",
    model="genailab-maas-gpt-35-turbo",
    api_key="sk-xcC3RS-FbPCheSCR1AY0BA",
    http_client=client
)


print(llm.invoke("""what is gen ai""").content)

