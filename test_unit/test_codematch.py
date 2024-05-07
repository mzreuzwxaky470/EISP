import sys
sys.path.append('/home/user/Automatic-Code-Evaluation')
from code_match import is_output

code = """
print("Distance with p = 1:", distances[0])
"""

print(is_output(code))