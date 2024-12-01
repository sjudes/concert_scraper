"""Find concerts at Wigmore Hall."""
import requests
import json
from concerts.venues.venue import Venue


class _Venue_WigmoreHall(Venue):
    """The Wigmore Hall has an undocumented API.
    You can only request one 'page' at a time, but the response includes the 
    total number of pages, so you can loop through them.  
    """
    def __init__(self):
        super().__init__("Wigmore Hall", "https://www.wigmore-hall.org.uk", "London")

    def get_single_page_of_listings(page, eventLocation='', startDate=''):
        params = {
            'eventLocation': eventLocation,
            'page': page,
            'startDate': startDate
        }
        url = "https://www.wigmore-hall.org.uk/api/v1/listings/whats-on?"
        url += "&".join([f"{k}={v}" for k, v in params.items()])
        listing = requests.get(url)
        return json.loads(listing.text)

    def get_all_listings(self):
        page = 1
        listings = []
        while True:
            page_listings = self.get_single_page_of_listings(page)
            listings.extend(page_listings['items'])
            page += 1
            if page > page_listings['totalPages']:
                break
        for listing in listings:
            listing['node']['fullUrl'] = f"https://www.wigmore-hall.org.uk{listing['node']['url']}" 
        return listings

    def get_listing_urls(self):
        listings = self.get_all_listings()
        return [l['node']['fullUrl'] for l in listings]
