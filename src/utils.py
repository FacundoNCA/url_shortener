import string
import random
from models import URLS


def generate_short_url(length=6):
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(length))
    url = URLS.query.where(URLS.short_url == short_url ).first()
    if ( url != None ):
        return generate_short_url(length)
    return short_url
