from fastapi import Query,APIRouter
from app.services.vector_search import find_similar_items

router=APIRouter()

@router.get('/search')
async def search(q:str=Query(...,description="Search Query")):
    return {"Results":find_similar_items(q)}
