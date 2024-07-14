import requests
from dotenv import load_dotenv
import os
from .cleanData import clean_response

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str):
    """
    scrape information from linkedin profile.
    manually scrape linkedin profile

    """
    url = "https://linkedin-data-api.p.rapidapi.com/get-profile-data-by-url"

    querystring = {"url": linkedin_profile_url}

    headers = {
        "x-rapidapi-key": os.getenv("RAPID_API_KEY"),
        "x-rapidapi-host": "linkedin-data-api.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)
    response = clean_response(response.json())
    print(response)

