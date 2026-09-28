import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import networkx as nx
from pathlib import Path


def generate_dependency_graph(dependencies, output_folder="generated_reports"):

    graph = nx.DiGraph()

    dependency_graph = dependencies.get(
        "dependency_graph",
        {}
    )

    for file_name, imports in dependency_graph.items():

        graph.add_node(file_name)

        for imported_module in imports:

            graph.add_edge(
                file_name,
                imported_module
            )

    output_directory = Path(output_folder)
    output_directory.mkdir(
        parents=True,
        exist_ok=True
    )

    image_path = output_directory / "dependency_graph.png"

    plt.figure(figsize=(18, 12))

    position = nx.spring_layout(
        graph,
        seed=42
    )

    nx.draw_networkx_nodes(
        graph,
        position,
        node_size=800
    )

    nx.draw_networkx_edges(
        graph,
        position,
        arrows=True,
        arrowsize=12
    )

    nx.draw_networkx_labels(
        graph,
        position,
        font_size=8
    )

    plt.title("Repository Dependency Graph")
    plt.axis("off")
    plt.tight_layout()

    plt.savefig(
        image_path,
        dpi=250
    )

    plt.close()

    return {
        "image": str(image_path),
        "nodes": graph.number_of_nodes(),
        "edges": graph.number_of_edges()
    }