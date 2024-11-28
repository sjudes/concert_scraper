from concerts.scraper import extract_concert_info

# url = "https://www.verbierfestival.com/en/programme/?"
# url = "https://www.verbierfestival.com/en/show/vf25-07-17-1100-150e-anniversaire-de-ravel-partie-1/"
# url = "https://www.barbican.org.uk/whats-on/2025/event/simon-bolivar-symphony-orchestradudamel-mahler-3"

url = "https://www.barbican.org.uk/whats-on/2025/event/shostakovich-quartets-intimate-portraits-part-1"
concerts = extract_concert_info(url)
tb = concerts[0]
print(tb.dict()['text'])