from fastapi import APIRouter
from app.models.repository import RepositoryRequest
from app.services.git_service import clone_repository

router = APIRouter()


@router.post("/repository")
def register_repository(repository: RepositoryRequest):

    result = clone_repository(repository.github_url)

    return result