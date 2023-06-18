from fastapi import FastAPI
from core.config import settings
from db.session import engine
#from db.base_class import Base
from db.base import Base
from apis.route_user import router
from apis.base import api_router


def create_tables():
    Base.metadata.create_all(bind=engine)

def include_router(app): 
    app.include_router(api_router)


def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_tables()
    include_router(app)
    return app

app = start_application()  # Call the function to get the FastAPI instance
print(settings.DATABASE_URL)

@app.get('/')
def hello_api():
    return {"detail": settings.DATABASE_URL}
