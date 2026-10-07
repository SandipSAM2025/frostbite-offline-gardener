ZONE_FROST_TABLE = {
    "zone 3": {"last_spring": "May 15", "first_fall": "September 15"},
    "zone 4": {"last_spring": "May 1", "first_fall": "October 1"},
    "zone 5": {"last_spring": "April 15", "first_fall": "October 15"},
    "zone 6": {"last_spring": "April 1", "first_fall": "November 1"},
    "zone 7": {"last_spring": "March 15", "first_fall": "November 15"},
    "zone 8": {"last_spring": "March 1", "first_fall": "December 1"},
    "zone 9": {"last_spring": "February 1", "first_fall": "December 15"},
    "zone 10": {"last_spring": "January 15", "first_fall": "None (frost-free)"},
}

def resolve_zone_data(query: str):
    query = query.strip().lower()
    for key, data in ZONE_FROST_TABLE.items():
        if key in query:
            return key.title(), data
    return "Zone 6", ZONE_FROST_TABLE["zone 6"]
