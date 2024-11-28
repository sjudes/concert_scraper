import os
import requests
from anthropic import Anthropic
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()

from concerts.schemas import concert_schema
from concerts.html import get_html
from concerts.claude import claude_query


def extract_concert_info(url):
    """Extracts concert information from a given URL."""
    html_content = get_html(url)
    # Create the prompt
    prompt = f"""
    Please analyze this concert webpage and extract:
    1. All musical works (composer and title)
    2. All performers and their roles
    3. Concert date, time, and venue

    Some further instructions:
    - Please use the correct case for names, i.e. capitalized first letters.
    - Please put dates in the format DD.MM.YYYY
    - Please just give the start time, not the end time, and use 12-hour format.
    - Please capitalize the first letter of the performer role.
    
    Return the data in JSON format, using the following schema:
    {concert_schema}

    Webpage content:
    {html_content}
    """
    return claude_query(prompt)

