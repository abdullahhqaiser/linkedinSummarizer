from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
import os

if __name__ == "__main__":
    load_dotenv()
    prompt_text = """
    given {username} for a person, provide me the following information, with the following headings:

    1. Biography
    2. Current life status

    """

    username = input("Please enter a username: ")
    prompt = PromptTemplate(template=prompt_text, input_variables=["username"])

    llm = HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2",
        task="text-generation",
        max_new_tokens=512,
        do_sample=False,
        repetition_penalty=1.03,
        huggingfacehub_api_token=os.getenv("HUGGING_FACE_API_KEY"),
    )

    chain = prompt | llm

    print(chain.invoke({"username": username}))
