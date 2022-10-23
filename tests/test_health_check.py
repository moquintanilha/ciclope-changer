import pytest
import requests


@pytest.mark.asyncio
async def test_health_check():
    response = requests.get('http://localhost:8000/api/health-check')
    status_code = response.status_code
    message = response.json()
    assert status_code == 200
    assert message == {'message': 'UP'}
