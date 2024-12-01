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
    

def extract_concerts_improved(url):
    """Extracts concert information from a given URL."""
    html_content = get_html(url)
    now = datetime.now()

    prompt = f"""
    You are a sophisticated AI assistant tasked with extracting and structuring concert information from webpage content. Your goal is to analyze the provided HTML and create a structured list of concert data.

    Here's the webpage content to analyze:

    <html_content>
    {html_content}
    </html_content>

    Now, here's the schema for each concert object you'll need to create:

    <concert_schema>
    {concert_schema}
    </concert_schema>

    Please follow these instructions carefully:

    1. Analyze the webpage content and identify individual concerts.

    2. For each concert, extract the following information:
        a. All musical works (composer and title)
        b. All performers and their roles
        c. Concert date, time, and venue

    3. Format the extracted information according to these rules:
        - Use correct case for names (capitalized first letters)
        - Put dates in the format DD.MM.YYYY
        - Give only the start time, using 12-hour format
        - Capitalize the first letter of the performer role
        - Use the current date ({now.strftime('%d.%m.%Y')}) for the scrape_info date
        - Use the current time ({now.strftime('%-I:%M %p')}) for the scrape_info time
        - Use {url} for the scrape_info url

    4. Structure each concert's data as a JSON object following the provided schema.

    5. Compile all concert objects into a list.

    6. Wrap the list of concerts inside <extracted_concert_list> tags.

    Before providing the final list of concerts, wrap your analysis inside <extraction_process> tags to show your thought process for extracting and structuring the information. This will help ensure accuracy and completeness. In this analysis:

        1. Identify and list all concert-related sections in the HTML content.
        2. Extract and list all dates, times, venues, performers, and works mentioned.
        3. Match these elements to create individual concert objects.
        4. Verify each concert object against the schema.

    It's OK for this section to be quite long.

    Now, please analyze the webpage content and extract the required concert information.
    """
    
    return claude_query(prompt)