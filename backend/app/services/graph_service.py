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

    python_files = set()

    for file_name in dependency_graph.keys():
        python_files.add(file_name)

    # -------------------------
    # Build Graph
    # -------------------------

    for file_name, imports in dependency_graph.items():

        graph.add_node(file_name)

        for imported_module in imports:

            imported_file = imported_module

            if not imported_file.endswith(".py"):
                imported_file += ".py"

            # Ignore self imports
            if imported_file == file_name:
                continue

            graph.add_node(imported_file)

            graph.add_edge(
                file_name,
                imported_file
            )

    # -------------------------
    # Node Colors
    # -------------------------

    node_colors = []

    for node in graph.nodes():

        if node in python_files:
            node_colors.append("#EC4899")      # Pink
        else:
            node_colors.append("#F472B6")      # Light Pink

    # -------------------------
    # Output Folder
    # -------------------------

    output_directory = Path(output_folder)

    output_directory.mkdir(
        parents=True,
        exist_ok=True
    )

    image_path = output_directory / "dependency_graph.png"

    # -------------------------
    # Figure
    # -------------------------

    plt.figure(figsize=(22,16))

    position = nx.kamada_kawai_layout(graph)

    # -------------------------
    # Nodes
    # -------------------------

    nx.draw_networkx_nodes(
        graph,
        position,
        node_size=5000,
        node_color=node_colors,
        edgecolors="black",
        linewidths=2.5
    )

    # -------------------------
    # Edges
    # -------------------------

    nx.draw_networkx_edges(
        graph,
        position,
        arrows=True,
        arrowsize=35,
        width=3,
        edge_color="#555555",
        connectionstyle="arc3,rad=0.08"
    )

    # -------------------------
    # Labels
    # -------------------------

    nx.draw_networkx_labels(
        graph,
        position,
        font_size=20,
        font_weight="bold",
        font_color="black"
    )

    # -------------------------
    # Title
    # -------------------------

    plt.title(
        "Repository Dependency Graph",
        fontsize=26,
        fontweight="bold",
        pad=25
    )

    plt.axis("off")

    plt.tight_layout()

    plt.savefig(
        image_path,
        dpi=350,
        bbox_inches="tight",
        facecolor="white"
    )

    plt.close()

    return {
        "image": str(image_path),
        "nodes": graph.number_of_nodes(),
        "edges": graph.number_of_edges()
    }