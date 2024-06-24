from fastapi import FastAPI as FastAPIMain
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi_healthcheck import healthCheckRoute

from apis.v1.health_check import _healthChecks
from endpoint.functional_api_urls import api_router


class FastAPI(FastAPIMain):
    """
    Customized FastAPI class inheriting from FastAPIMain to extend functionality.
    """

    ORIGINS = ["*"]

    def __init__(self, title, version, **kwargs):
        """
        Initialize the FastAPI instance with custom parameters.
        """
        super().__init__(title=title, version=version, openapi_url="/flash/openapi.json")

    def _include_router(self):
        """
        Include additional routers and routes into the FastAPI application.
        """
        # Add health-check route using fastapi_healthcheck extension
        self.add_api_route('/health-check', endpoint=healthCheckRoute(factory=_healthChecks))

        # Include the custom API router defined in `api_router`
        self.include_router(api_router)

    def set_middleware(self):
        """
        Set up middleware components for the FastAPI application.
        """
        # Add CORS middleware to handle Cross-Origin Resource Sharing
        self.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"]
        )

        # Add GZip middleware for response compression
        self.add_middleware(GZipMiddleware)

    def start(self):
        """
        Start the FastAPI application by setting middleware and including routers.
        """
        self.set_middleware()  # Set up middleware components
        self._include_router()  # Include additional routers and routes
