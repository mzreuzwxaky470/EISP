import os
import sys
from code_spilt import *
from code_match import get_type

#
from myAPI import *
from code_extra import extract_dependencies,add_assign

#，”“，
# TH = 300

def OverAllLogic(Gen_Code,problem_statement,use_problem_statement,pre_logic):


    #，“”
    if pre_logic == "":
        use_pre_logic = False
    else:
        use_pre_logic = True

    

    #、

    Gen_Code = code_strip_spaces(Gen_Code)
    problem_statement = code_strip_spaces(problem_statement)

    Gen_Code = code_srtip_main(Gen_Code)

    #“”
    Gen_Code_unit = []

    temp = extract_first_level(Gen_Code)
    for i in range(len(temp)):
        Gen_Code_unit.append(temp[i])



    #、”“
    #：variable_logic = {"x1":"xxxxxxx"}
    snippet_logic = {} 
    assign_code = {}
    import re

    #
    code_structure = []
    #
    structure_code_dict = {}
    #
    structure_logic_dict = {}
    #import
    import_dict = {}
    #
    function_logic_dict = {}
    #
    class_logic_dict = {}
    

    for level in extract_first_level(Gen_Code):
        type = get_type(level)
        if type == "import" or type == "other":
            continue
        #code_structuretype，type1、type2、type3...
        if type in code_structure:
            count = 0
            for t in code_structure:
                if t.startswith(type):
                    count = count+1
            type = type+str(count)
            code_structure.append(type)
            temp = {type:level}
            structure_code_dict.update(temp)
        else:
            code_structure.append(type)
            temp = {type:level}
            structure_code_dict.update(temp)

    #bug，
    for s in code_structure:
        if structure_code_dict[s] == "":
            code_structure.remove(s)
            structure_code_dict.pop(s)
            #structure_logic_dict.pop(s)
    a = 0

    for s in code_structure:
        unit = structure_code_dict[s]

        if s.startswith("import"):
            #import
            #：import math，math 
            #from math import sqrt, pow，sqrt、pow
            packages = re.findall(r"import\s+(.*)",unit)[0]
            
            pack = packages.split(",")
            for p in pack:
                #key，value，
                temp = {p:structure_code_dict[s]}
                import_dict.update(temp)

            continue

        if s.startswith("input"):
            
            print("：")
            code_logic = return_input_assign_explain(unit,problem_statement=problem_statement,use_problem_statement=use_problem_statement)
            print(code_logic)
            print("-------------")
            #
            #：x1 = map(float, input().split())，x1、x1,y1,x2,y2 =map(float, input().split())，x1,y1,x2,y2
            #
            tempvar = unit.split("=")[0]
            #
            tempvar = tempvar.replace(" ","")

            tempvar = tempvar.split(",")

            #
            for t in tempvar:
                temp = {t:code_logic}
                snippet_logic.update(temp)


            #，x1,y1,x2,y2 =map(float, input().split())
            #

            #
            temp = {s:code_logic}
            structure_logic_dict.update(temp)
        


        if s.startswith("assign"):
            #：
            #：x1 = map(float, input().split())，x1
            var = unit.split("=")[0]
            #
            var = var.replace(" ","")

            #todo:
            vars = var.split(",")

            dependencies = extract_dependencies(unit)
            logic = return_assign_explain(unit,dependencies,class_logic_dict,function_logic_dict)

            for v in vars:


                #
                # （，）
                temp = {v:unit}
                assign_code.update(temp)

                #
                temp = {s:""}
                structure_logic_dict.update(temp)

                temp = {v:logic}
                snippet_logic.update(temp)

            continue


        if s.startswith("define"):
            #，def()
            func_name = re.search(r"def(.*?)\(", unit).group(1)
            #
            func_name = func_name.replace(" ","")
                
            dependencies = extract_dependencies(unit)
            for d in dependencies:
                if d in import_dict:
                    #import，
                    unit = import_dict[d] + "\n" + unit
            if(code_depth(unit)<=TH):

                func_logic = return_func_explain(unit)
                #
                temp = {func_name:func_logic}
                function_logic_dict.update(temp)

                #
                temp = {s:func_logic}
                structure_logic_dict.update(temp)
                print(""+func_name+"：")
                print(func_logic)
                print("----------------------")

            else:
                #
                new_unit = extract_second_indent(unit)
                sub_logic = OverAllLogic(new_unit,problem_statement,use_problem_statement)
                #print(sub_logic)

                #todo:
                #
                temp = {s:sub_logic}
                structure_logic_dict.update(temp)
                print(""+func_name+"：")
                print(sub_logic)
                print("----------------------")
                temp = {func_name:sub_logic}
                function_logic_dict.update(temp)
                continue



        if s.startswith("judge"):
            if(code_depth(unit)<=TH):
                #“”，，

                #
                dependencies = extract_dependencies(unit)
                #print(return_snippet_explain2(unit,dependencies,snippet_logic))

                for d in dependencies:
                    if d in import_dict:
                        #import，
                        unit = import_dict[d] + "\n" + unit

                unit = add_assign(unit,dependencies,structure_code_dict)
                loop_logic,code_snippet = return_snippet_explain2(unit,dependencies,snippet_logic,assign_code,function_logic_dict)
                
                
                temp = {s:loop_logic}
                structure_logic_dict.update(temp)

                #，
                #，
                for var in dependencies:
                    if var in snippet_logic:
                        new_logic = update_snippet_logic(loop_logic,var,code_snippet)

                        print(""+var+"：")
                        print(new_logic)
                        print("----------------------")
                        #
                        if var in snippet_logic:
                            snippet_logic[var] = str(new_logic)
                        else:
                            temp = {var:str(new_logic)}
                            snippet_logic.update(temp)

                #，
                #，


            else:
                #todo:
                #“”
                i=0
            continue
        if s.startswith("loop"):
            if(code_depth(unit)<=TH):
                #“”，，

                #
                dependencies = extract_dependencies(unit)
                #print(return_snippet_explain2(unit,dependencies,snippet_logic))

                for d in dependencies:
                    if d in import_dict:
                        #import，
                        unit = import_dict[d] + "\n" + unit
                unit = add_assign(unit,dependencies,structure_code_dict)

                loop_logic,code_snippet = return_snippet_explain2(unit,dependencies,snippet_logic,assign_code,function_logic_dict)
                
                
                temp = {s:loop_logic}
                structure_logic_dict.update(temp)

                #，
                #，
                for var in dependencies:
                    if var in snippet_logic:
                        new_logic = update_snippet_logic(loop_logic,var,code_snippet)

                        print(""+var+"：")
                        print(new_logic)
                        print("----------------------")
                        #
                        
                        snippet_logic[var] = str(new_logic)
                        """else:
                            temp = {var:str(new_logic)}
                            snippet_logic.update(temp)"""

                #，
                #，


            else:
                #todo:
                #“”
                i=0
                
        if s.startswith("class"):
            if(code_depth(unit)<=TH):
                #“”，，

                #
                dependencies = extract_dependencies(unit)
                #print(return_snippet_explain2(unit,dependencies,snippet_logic))

                for d in dependencies:
                    if d in import_dict:
                        #import，
                        unit = import_dict[d] + "\n" + unit
                #unit = add_assign(unit,dependencies,structure_code_dict)

                class_logic,code_snippet = return_snippet_explain2(unit,dependencies,snippet_logic,assign_code,function_logic_dict)
                
                
                temp = {s:class_logic}
                structure_logic_dict.update(temp)

                #
                class_name = re.search(r"class(.*?):", unit).group(1)
                #
                class_name = class_name.replace(" ","").replace("(","").replace(")","")

                temp = {class_name:class_logic}
                class_logic_dict.update(temp)
                temp = {s:class_logic}
                structure_logic_dict.update(temp)

                


            else:
                #todo:
                #“”
                i=0



        if s.startswith("output"):
            dependencies = extract_dependencies(unit)
            logic = return_output_explain(unit,dependencies,snippet_logic,function_logic_dict)

            temp = {s:logic}
            structure_logic_dict.update(temp)

    for s in code_structure:
        print(s)
        if s =="assign":
            assign_code = structure_code_dict[s]
            #
            var = assign_code.split("=")[0]
            #
            var = var.replace(" ","")
            if var in snippet_logic:
                var_logic = snippet_logic[var]
            
                #
                structure_logic_dict[s] = var_logic

            continue
        print(structure_code_dict[s])
        print("：")
        print(structure_logic_dict[s])
        print("-------------")

    #print(return_overall_explain(Gen_Code,code_structure,structure_code_dict,structure_logic_dict))
    return return_overall_explain(Gen_Code,code_structure,structure_code_dict,structure_logic_dict)
