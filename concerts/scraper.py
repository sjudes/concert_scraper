from datetime import datetime
import re
import json

from concerts.schemas import concert_schema
from concerts.html import get_html
from concerts.claude import claude_query


def extract_concert_info(url):
    """Extracts concert information from a given URL."""
    html_content = get_html(url)
    now = datetime.now()
    # Create the prompt
    prompt = f"""
    You are an expert at extracting information about classical music concerts from 
    websites of concert venues and festivals.

    Below in <html_content> tags is some html extracted from a concert website.
    <html_content>
    {html_content}
    </html_content>

    Please analyse the page, and extract the following information for each concert:

    1. All musical works (composer and title)
    2. All performers and their roles
    3. Concert date, time, and venue

    Output Specification:
    1. Return the data in json format as a list of concerts.
    2. Wrap the list with <extracted_concert_json> tags.
    3. For each individual concert, use the following schema:
    {concert_schema}

    Some further instructions:
    - If there are multiple concerts please return the information for all of them in the
      response to this query.  Please don't return just a sample and ask if further 
      concerts are desired.
    - Please use the correct case for names, i.e. capitalized first letters.
    - Please put dates in the format DD.MM.YYYY
    - Please just give the start time, not the end time, and use 12-hour format.
    - Please capitalize the first letter of the performer role.
    - For the scrape_info date, please use {now.strftime('%d.%m.%Y')} 
    - For the scrape_info time, please use {now.strftime('%-I:%M %p')}
    - For the scrape_info url, please use {url}
    """

    # Get response from Claude
    claude_response = claude_query(prompt)[0].text
    concert_info = re.findall("<extracted_concert_json>(.+?)</extracted_concert_json>", 
                      claude_response, re.DOTALL)
    return [json.loads(c) for c in concert_info]
    