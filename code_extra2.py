import ast
import builtins

def extract_dependencies(code):
    tree = ast.parse(code)

    loaded_vars = set()
    assigned_vars = set()
    dependencies = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
            loaded_vars.add(node.id)
        elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
            assigned_vars.add(node.id)
            if node.id not in assigned_vars and node.id not in dependencies:
                dependencies.add(node.id)
        elif isinstance(node, ast.AugAssign):  # for cases like c += 1
            if isinstance(node.target, ast.Name):
                if node.target.id not in assigned_vars:
                    dependencies.add(node.target.id)

    dependencies = (dependencies | loaded_vars) - assigned_vars
    built_in_names = dir(builtins)

    return dependencies - set(built_in_names)

# 
code = """
list_ = [[False for i in range(13)] for j in range(4)]
"""

print(extract_dependencies(code))  # {'A', 'n', 'c'}
