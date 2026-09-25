from fastapi import APIRouter

from app.models.repository import RepositoryRequest
from app.models.scan import ScanRequest
from app.models.parse import ParseRequest, RepositoryParseRequest
from app.services.complexity_service import calculate_repository_complexity

from app.services.git_service import clone_repository
from app.services.scanner_service import scan_repository
from app.services.analysis_service import analyze_repository
from app.services.parser_service import (
    parse_python_file,
    parse_repository,
)
from app.services.dependency_service import build_dependency_graph
from app.services.summary_service import generate_repository_summary

router = APIRouter()


@router.post("/repository")
def register_repository(repository: RepositoryRequest):

    return clone_repository(repository.github_url)


@router.post("/repository/scan")
def scan_repository_endpoint(request: ScanRequest):

    return scan_repository(request.repository_path)


@router.post("/repository/parse")
def parse_python_file_endpoint(request: ParseRequest):

    return parse_python_file(request.file_path)


from app.services.analysis_service import analyze_repository


@router.post("/repository/analyze")
def analyze_repository_endpoint(request: RepositoryParseRequest):

    return analyze_repository(request.repository_path)


@router.post("/repository/dependencies")
def dependency_graph_endpoint(request: RepositoryParseRequest):

    analysis = parse_repository(request.repository_path)

    return build_dependency_graph(analysis)


@router.post("/repository/summary")
def repository_summary_endpoint(request: RepositoryParseRequest):

    analysis = parse_repository(request.repository_path)

    return generate_repository_summary(analysis)

@router.post("/repository/complexity")
def repository_complexity_endpoint(request: RepositoryParseRequest):

    return calculate_repository_complexity(
        request.repository_path
    )