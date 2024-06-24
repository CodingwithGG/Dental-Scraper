from fastapi import APIRouter
from fastapi_healthcheck import HealthCheckFactory

router = APIRouter()

# Add Health Checks
_healthChecks = HealthCheckFactory()
