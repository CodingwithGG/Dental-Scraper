from fastapi import FastAPI as FastAPIMain
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.cors import CORSMiddleware
# from core.middleware.jwt_middleware import JWTAuthenticationBackend
from fastapi_healthcheck import healthCheckRoute
from fastapi_restful import Api
from apis.v1.health_check.health_check import _healthChecks
from core.url_framework.process_urls import register_url
from endpoint import urls
from endpoint.functional_api_urls import api_router

from core.config import settings


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
        # self.add_middleware(AuthenticationMiddleware, backend=JWTAuthenticationBackend(secret_key=settings.SECRET_KEY,
        #                                                                                algorithm=settings.ALGORITHM))

    def start(self):
        """"""
        self.set_middleware()
        api = Api(self)
        # register_url(api, urls.urls)
        self._include_router()
