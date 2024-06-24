from fastapi import FastAPI as FastAPIMain
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi_healthcheck import healthCheckRoute

from apis.v1.health_check import _healthChecks
from endpoint.functional_api_urls import api_router


class FastAPI(FastAPIMain):
    """"""
    ORIGINS = ["*"]

    def __init__(self, title, version, **kwargs):
        """"""
        super().__init__(title=title, version=version, openapi_url="/flash/openapi.json")

    def _include_router(self):
        self.add_api_route('/health-check', endpoint=healthCheckRoute(factory=_healthChecks))
        self.include_router(api_router)

    def set_middleware(self):
        self.add_middleware(
            CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
        self.add_middleware(GZipMiddleware)

    def start(self):
        """"""
        self.set_middleware()
        self._include_router()

