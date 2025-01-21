import random
import string
from datetime import datetime

from app.core.database import get_db

db = get_db()


def generate_short_id(length=8):
    """Generate a random short ID."""
    characters = string.ascii_letters + string.digits
    return "".join(random.choices(characters, k=length))


async def create_short_url(long_url: str):
    """Create a new short URL."""
    short_id = generate_short_id()
    data = {
        "long_url": long_url,
        "short_id": short_id,
        "created_at": datetime.now().isoformat(),
    }
    db.short_urls.insert_one(data)

    return short_id


async def get_long_url(short_id: str):
    """Retrieve the original URL for a given short ID."""
    data = db.short_urls.find_one({"short_id": short_id})
    return data["long_url"] if data else None


async def get_stats():
    return {"totalVisits":20789,"orphanVisits":2045,"shortUrls":db.short_urls.count_documents({})}
