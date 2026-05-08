import ast
from pathlib import Path


def get_dependencies():

    dependencies = {}

    repo_dir = Path(
        "data/repos/langchain"
    )

    for py_file in repo_dir.rglob("*.py"):

        try:

            code = py_file.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            tree = ast.parse(code)

            imports = []

            for node in ast.walk(tree):

                if isinstance(node, ast.Import):

                    for alias in node.names:

                        imports.append(
                            alias.name
                        )

                elif isinstance(
                    node,
                    ast.ImportFrom
                ):

                    if node.module:

                        imports.append(
                            node.module
                        )

            dependencies[
                str(py_file)
            ] = imports

        except:

            pass

    return dependencies