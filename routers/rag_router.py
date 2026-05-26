from fastapi import APIRouter
from schemas import SearchQuery
from rag import search_data

router = APIRouter(
    prefix="/rag"
)


@router.post("/search")
def search(query: SearchQuery):

    results = search_data(
        query.query
    )

    return {
        "results": results
    }