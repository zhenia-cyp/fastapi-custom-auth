import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from main import app
from httpx import AsyncClient, ASGITransport


@pytest.mark.asyncio
async def test_refresh_token_flow():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as client:
        response = await client.post("/auth/login", data={
            "username": "",
            "password": ""
        })
        assert response.status_code == 200
        refresh_token_cookie = response.cookies.get("refresh_token")
        assert refresh_token_cookie is not None
        client.cookies.set("refresh_token", refresh_token_cookie)
        refresh_response = await client.post("/auth/refresh")
        assert refresh_response.status_code == 200
        assert "access_token" in refresh_response.json()
