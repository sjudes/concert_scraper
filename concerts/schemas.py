concert_schema = {
    "type": "object",
    "properties": {
        "scrape_info": {
            "type": "object",
            "properties": {
                "scrape_date": {"type": "string"},
                "scrape_time": {"type": "string"},
                "url": {"type": "string"},
            },
        },
        "concert_info": {
            "type": "object",
            "properties": {
                "date": {"type": "string"},
                "time": {"type": "string"},
                "location": {"type": "string"},
                "performers": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "role": {"type": "string"},
                        },
                    },
                },
                "programme": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "composer": {"type": "string"},
                            "title": {"type": "string"},
                        },
                    },
                },
            },
        },
    },
}
