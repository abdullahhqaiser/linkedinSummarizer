from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint
from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    response = scrape_linkedin_profile(
        linkedin_profile_url="https://www.linkedin.com/in/johnrmarty/"
    )

    print(response)
    