import ast
import builtins
import re



#ast，
#
def extract_dependencies(code):
    """
    。

    :
        code (str): Python。

    :
        set: 。
    """
    tree = ast.parse(code)
    names = set()

    # AST
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
            names.add(node.id)

    # 
    local_vars = {v.id for v in ast.walk(tree) if isinstance(v, ast.Name) and isinstance(v.ctx, (ast.Store, ast.Param))}
    built_in_names = dir(builtins)

    #dependencies = names - local_vars - set(built_in_names)
    #，，
    
    #local_varsbuilt_in_namesnames
    for var in local_vars:
        names.add(var)

    dependencies = names
    
    return dependencies


def add_assign(code,dependencies,structure_code_dict):

    for key in structure_code_dict:
    #keyassign
        if key.startswith("assign"):
            #
            var = re.search(r"(.*?)=", structure_code_dict[key]).group(1)
            #
            var = var.replace(" ","")
            var = var.split(",")
            print(var)
            print(structure_code_dict[key])
            print("------------")
            #，
            for v in var:
                if v in dependencies:
                    print("yes")
                    code = structure_code_dict[key] + "\n" + code
                    
        
    return code







