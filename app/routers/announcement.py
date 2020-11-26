from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services import announcement_service
from app.utils import work_with_avito_api
from app.crawler import work_with_crawler

router = APIRouter()


class CreateSearchObject(BaseModel):
    text: str
    region: str


class GetCounterObject(BaseModel):
    id: int
    start: int
    end: int


@router.post("/add")
async def add_request(obj: CreateSearchObject):
    db_obj = await announcement_service.get_request_by_text_and_region(obj.text, obj.region)
    if db_obj:
        raise HTTPException(status_code=400,
                            detail=f'this request and region are already registered, id:{db_obj["id"]}')

    count, timestamp = work_with_avito_api.get_count(text=obj.text, region=obj.region)
    obj_id = await announcement_service.create_object(obj.text, obj.region)
    await announcement_service.add_count(obj_id, count, timestamp)
    work_with_crawler.add_count_in_queue(obj_id, timestamp, obj.text, obj.region)
    return {"id": obj_id}


@router.get("/stat")
async def get_stat(obj: GetCounterObject):
    counters = await announcement_service.get_counters(obj.id, obj.start, obj.end)
    return {"counters": counters}
