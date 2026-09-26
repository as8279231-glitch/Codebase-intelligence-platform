from app.services.parser_service import parse_repository
from app.services.summary_service import generate_repository_summary
from app.services.dependency_service import build_dependency_graph
from app.services.metrics_service import calculate_repository_metrics
from app.services.complexity_service import calculate_repository_complexity
from app.services.call_graph_service import build_repository_call_graph
from app.services.dead_code_service import detect_dead_code

def analyze_repository(repository_path: str):

    analysis = parse_repository(repository_path)

    summary = generate_repository_summary(analysis)

    dependencies = build_dependency_graph(analysis)

    metrics = calculate_repository_metrics(
        repository_path,
        analysis
    )

    complexity = calculate_repository_complexity(
        repository_path
    )

    call_graph = build_repository_call_graph(
        repository_path
    )
    dead_code = detect_dead_code(
    repository_path
   )

    return {
        "repository": analysis["repository"],
        "summary": summary,
        "metrics": metrics,
        "dependencies": dependencies,
        "complexity": complexity,
        "call_graph": call_graph,
        "parsed_files": analysis["parsed_files"]
    }