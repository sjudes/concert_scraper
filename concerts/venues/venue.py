class _Venue:
    """Base class for a concert venue."""
    def __init__(self, name, url, town):
        self.name = name
        self.url = url
        self.town = town
    
    def __repr__(self):
        return f"{self.name}, {self.town}\n{self.url}"
    
    def get_listing_urls(self):
        """Return a list of URLs for the concerts at this venue."""
        raise NotImplementedError


