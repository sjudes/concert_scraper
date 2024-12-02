from concerts.scraper import extract_concert_info
from concerts.venues import wigmore_hall

# url = "https://www.verbierfestival.com/en/programme/?"
# url = "https://www.verbierfestival.com/en/show/vf25-07-17-1100-150e-anniversaire-de-ravel-partie-1/"
# url = "https://www.barbican.org.uk/whats-on/2025/event/simon-bolivar-symphony-orchestradudamel-mahler-3"
# url = "https://www.barbican.org.uk/whats-on/2025/event/shostakovich-quartets-intimate-portraits-part-1"
# url = "https://www.wigmore-hall.org.uk/whats-on/202412021930"

# TODO: Parallelise this
listings = wigmore_hall.get_listing_urls()
concerts = [extract_concert_info(listing) for listing in listings[:3]]
from IPython import embed; embed()