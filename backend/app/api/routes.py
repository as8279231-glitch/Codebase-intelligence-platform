from fastapi import APIRouter

from app.models.repository import RepositoryRequest
from app.models.scan import ScanRequest
from app.models.parse import ParseRequest

from app.services.git_service import clone_repository
from app.services.scanner_service import scan_repository
from app.services.parser_service import parse_python_file

router = APIRouter()


@router.post("/repository")
def register_repository(repository: RepositoryRequest):

    result = clone_repository(repository.github_url)

    return result


@router.post("/repository/scan")
def scan_repository_endpoint(request: ScanRequest):

    result = scan_repository(request.repository_path)

    return result


@router.post("/repository/parse")
def parse_python_file_endpoint(request: ParseRequest):

    result = parse_python_file(request.file_path)

    return result