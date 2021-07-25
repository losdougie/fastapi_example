import httpx
from models.data import TimeRequest

async def get_current_time(TimeRequest):
    url = f"http://worldclockapi.com/api/json/{TimeRequest.location}/now"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()

        data = resp.json()
    return data