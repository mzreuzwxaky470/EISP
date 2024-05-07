#，“”、“”、““、”“

import re
import sys

#”input()“，”“
def is_input(Code):
    #input
    if re.search(r"input\([^)]*\)", Code):
        return True
    else:
        return False
    
#”print()“，”“
def is_output(Code):
    if re.search(r"print\([^)]*\)", Code):
        return True
    else:
        return False
    
#”for“while，”“
def is_loop(Code):
    if re.search(r"for", Code) or re.search(r"while", Code):
        return True
    else:
        return False
    
#”if“”elif“”else“，”“
def is_judge(Code):
    if re.search(r"if", Code) or re.search(r"elif", Code) or re.search(r"else", Code):
        return True
    else:
        return False
    
#”def“，”“
def is_define(Code):
    if re.search(r"def ", Code):
        return True
    else:
        return False
#
def is_assign(Code):
    if re.search(r"=", Code):
        return True
    else:
        return False
    
def is_import(Code):
    if re.search(r"import", Code):
        return True
    else:
        return False
    
def is_class(Code):
    if re.search(r"class", Code):
        return True
    else:
        return False
    
def get_type(Code):
    code_first_line = Code.split("\n")[0]
    if is_input(code_first_line):
        return "input"
    elif is_output(code_first_line):
        return "output"
    elif is_loop(code_first_line):
        return "loop"
    elif is_judge(code_first_line):
        return "judge"
    elif is_define(code_first_line):
        return "define"
    elif is_assign(code_first_line):
        return "assign"
    elif is_import(code_first_line):
        return "import"
    elif is_class(code_first_line):
        return "class"
    else:
        return "other"
    

