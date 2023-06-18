from fastapi import APIRouter

from apis import route_user
from apis import route_job

api_router = APIRouter()

api_router.include_router(route_user.router, prefix="/user")
api_router.include_router(route_job.router, prefix="/jobs")