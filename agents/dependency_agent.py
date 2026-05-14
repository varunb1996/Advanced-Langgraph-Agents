from tools.dependency_tool import (
    get_dependencies
)


def dependency_agent(state):

    query = state["query"]

    dependencies = get_dependencies()

    matched = {}

    for file, imports in dependencies.items():

        if query.lower() in file.lower():

            matched[file] = imports

    state["dependencies"] = matched

    return state