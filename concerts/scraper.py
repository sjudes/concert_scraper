from datetime import datetime

from concerts.schemas import concert_schema
from concerts.html import get_html
from concerts.claude import claude_query


def extract_concert_info(url):
    """Extracts concert information from a given URL."""
    html_content = get_html(url)
    now = datetime.now()
    # Create the prompt
    prompt = f"""
    This is the webpage for one or more concerts.  Please analyse the page, and
    for each concert, extract:
    1. All musical works (composer and title)
    2. All performers and their roles
    3. Concert date, time, and venue

    Some further instructions:
    - Please use the correct case for names, i.e. capitalized first letters.
    - Please put dates in the format DD.MM.YYYY
    - Please just give the start time, not the end time, and use 12-hour format.
    - Please capitalize the first letter of the performer role.
    - For the scrape_info date, please use {now.strftime('%d.%m.%Y')} 
    - For the scrape_info time, please use {now.strftime('%-I:%M %p')}
    - For the scrape_info url, please use {url}
    
    Return the data as a list of concerts, with the data for each individual
    concert in JSON format, using the following schema:
    {concert_schema}

    Webpage content:
    {html_content}
    """

    # Get response from Claude
    return claude_query(prompt)
    