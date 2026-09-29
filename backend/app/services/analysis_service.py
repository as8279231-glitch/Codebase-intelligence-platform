from app.services.parser_service import parse_repository
from app.services.summary_service import generate_repository_summary
from app.services.dependency_service import build_dependency_graph
from app.services.metrics_service import calculate_repository_metrics
from app.services.complexity_service import calculate_repository_complexity
from app.services.call_graph_service import build_repository_call_graph
from app.services.dead_code_service import detect_dead_code
from app.services.todo_service import scan_todos
from app.services.code_smell_service import detect_code_smells
from app.services.security_service import scan_security
from app.services.health_service import calculate_health_score
from app.services.recommendation_service import generate_recommendations
from app.services.graph_service import generate_dependency_graph
from app.services.insights_service import generate_repository_insights
from app.services.architecture_service import analyze_architecture
from app.services.tree_service import build_repository_tree
from app.services.top_complexity_service import get_top_complex_functions
from app.services.technical_debt_service import calculate_technical_debt
from app.services.dashboard_service import generate_dashboard
from app.services.hotspot_service import detect_hotspots
from app.services.duplicate_service import detect_duplicate_blocks
from app.services.maintainability_service import calculate_maintainability_index
from app.services.badge_service import generate_quality_badge
from app.services.documentation_service import analyze_documentation
from app.services.churn_service import estimate_code_churn
from app.services.license_service import detect_license
from app.services.gitignore_service import analyze_gitignore
from app.services.repository_size_service import analyze_repository_size
from app.services.import_statistics_service import analyze_imports
from app.services.test_coverage_service import estimate_test_coverage
from app.services.timeline_service import analyze_repository_timeline
from app.services.language_stats_service import analyze_language_statistics
from app.services.fingerprint_service import generate_repository_fingerprint
from app.services.ownership_service import analyze_code_ownership
from app.services.chart_service import generate_repository_charts
from app.services.naming_service import analyze_naming_quality
from app.services.cohesion_service import analyze_cohesion
from app.services.coupling_service import analyze_coupling
from app.services.repository_score_service import calculate_repository_score




def analyze_repository(repository_path: str):

    analysis = parse_repository(repository_path)

    summary = generate_repository_summary(analysis)

    repository_tree = build_repository_tree(
    repository_path
    )

    dependencies = build_dependency_graph(analysis)

    graph = generate_dependency_graph(
    dependencies
    )

    architecture = analyze_architecture(
    repository_path
    )

    metrics = calculate_repository_metrics(
        repository_path,
        analysis
    )

    complexity = calculate_repository_complexity(
        repository_path
    )

    top_complex_functions = get_top_complex_functions(
    complexity
    )

    call_graph = build_repository_call_graph(
        repository_path
    )

    dead_code = detect_dead_code(
        repository_path
    )

    todos = scan_todos(
        repository_path
    )

    code_smells = detect_code_smells(
        repository_path
    )

    duplicate = detect_duplicate_blocks(
    repository_path
    )

    security = scan_security(
        repository_path
    )

    technical_debt = calculate_technical_debt(
        dead_code,
        todos,
        security,
        code_smells
    )

    hotspots = detect_hotspots(
    complexity,
    dead_code,
    todos,
    code_smells
    )

    health = calculate_health_score(
        metrics,
        complexity,
        dead_code,
        todos,
        security
    )

    maintainability = calculate_maintainability_index(
    metrics,
    complexity,
    dead_code,
    code_smells
    )

    badge = generate_quality_badge(
    health,
    maintainability,
    security
    )

    documentation = analyze_documentation(
    repository_path
    )

    test_coverage = estimate_test_coverage(
    repository_path
    )

    timeline = analyze_repository_timeline(
    repository_path
    )

    language_statistics = analyze_language_statistics(
    repository_path
    )

    charts = generate_repository_charts(
    metrics,
    complexity,
    language_statistics,
    code_smells,
    security,
    todos,
    dead_code
    )

    fingerprint = generate_repository_fingerprint(
    repository_path
    )

    ownership = analyze_code_ownership(
    repository_path
    )

    naming = analyze_naming_quality(
    repository_path
    )

    cohesion = analyze_cohesion(
    repository_path
    )

    coupling = analyze_coupling(
    repository_path
    )

    license_info = detect_license(
    repository_path
    )

    gitignore = analyze_gitignore(
    repository_path
    )

    repository_size = analyze_repository_size(
    repository_path
    )

    import_stats = analyze_imports(
    repository_path
    )

    churn = estimate_code_churn(
    repository_path
    )
    
    dashboard = generate_dashboard(
    summary,
    metrics,
    complexity,
    health,
    security,
    dead_code,
    todos,
    code_smells
    )

    repository_score = calculate_repository_score(
    health,
    maintainability,
    security,
    documentation,
    complexity,
    duplicate,
    technical_debt
    )

    insights = generate_repository_insights(
    summary,
    metrics,
    complexity,
    dead_code,
    todos,
    security,
    health
    )

    recommendations = generate_recommendations(
    health,
    security,
    todos,
    dead_code,
    complexity
    )

    return {
        "repository": analysis["repository"],
        "summary": summary,
        "repository_tree": repository_tree,
        "architecture": architecture,
        "metrics": metrics,
        "dependencies": dependencies,
        "dependency_graph_image":graph,
        "complexity": complexity,
        "top_complex_functions": top_complex_functions,
        "call_graph": call_graph,
        "dead_code": dead_code,
        "todos": todos,
        "code_smells": code_smells,
        "duplicate": duplicate,
        "security": security,
        "technical_debt": technical_debt,
        "hotspots": hotspots,
        "health": health,
        "maintainability": maintainability,
        "quality_badge": badge,
        "documentation": documentation,
        "repository_score": repository_score,
        "test_coverage": test_coverage,
        "timeline": timeline,
        "language_statistics": language_statistics,
        "charts": charts,
        "fingerprint": fingerprint,
        "ownership": ownership,
        "naming": naming,
        "cohesion": cohesion,
        "coupling": coupling,
        "license": license_info,
        "gitignore": gitignore,
        "repository_size": repository_size,
        "import_statistics": import_stats,
        "code_churn": churn,
        "dashboard": dashboard,
        "insights": insights,
        "recommendations": recommendations,
        "parsed_files": analysis["parsed_files"]
        
    }