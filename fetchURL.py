import aiohttp
import asyncio

async def fetch_urls(query, base_url="http://localhost:8080"):
    async with aiohttp.ClientSession() as session:
        params = {
            "q": query,
            "format": "json",
            "language": "en",
        }
        async with session.get(f"{base_url}/search", params=params) as response:
            if response.status == 200:
                data = await response.json()
                # Extract URLs from the search results
                urls = [result["url"] for result in data.get("results", [])]
                return urls
            else:
                raise Exception(f"Failed to fetch results: {response.status} {response.reason}")