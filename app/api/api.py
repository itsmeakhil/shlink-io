from fastapi import HTTPException, Request, APIRouter
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from app.api.services import create_short_url, get_long_url


router = APIRouter()


# Request schema for URL shortening
class URLRequest(BaseModel):
    long_url: str


# Route to shorten a URL
@router.post("/shorten")
async def shorten_url(request: URLRequest):
    short_id = await create_short_url(request.long_url)
    return {"short_url": f"http://localhost:8090/{short_id}"}


# Route to redirect a short URL
@router.get("/{short_id}")
async def redirect_to_long_url(short_id: str):
    long_url = await get_long_url(short_id)
    if not long_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url=long_url)
