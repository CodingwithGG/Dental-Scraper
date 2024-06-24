import uvicorn
from core.config import settings
from main import FastAPI

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
app.start()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)