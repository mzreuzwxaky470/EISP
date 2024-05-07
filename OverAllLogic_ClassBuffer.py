import os
import sys
from code_spilt import *
from code_match import get_type

#
from myAPI import *
from code_extra import extract_dependencies,add_assign

#，”“，
# TH = 3
from BufferClass import CodeStructure





def OverAllLogic(Gen_Code,problem_statement,use_problem_statement,code_struct=None):
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

    assign_code = {}
    import re

    if_main = False

    #CodeStructure
    if code_struct == None:
        code_struct = CodeStructure()
        if_main = True
    else:
        pre_code_struct = code_struct.get_code_struct()
        code_struct.delete_code_struct()

        pre_struct_code = code_struct.get_structure_code()
        code_struct.delete_struct_code()

        pre_struct_logic = code_struct.get_structure_logic()
        code_struct.delete_struct_logic()

    
    
    

    for level in extract_first_level(Gen_Code):
        type = get_type(level)
        if type == "import" or type == "other":
            continue
        #code_structuretype，type1、type2、type3...
        if type in code_struct.get_code_struct():
            count = 0
            for t in code_struct.get_code_struct():
                if t.startswith(type):
                    count = count+1
            type = type+str(count)
            code_struct.add_code_struct(type)
            #code_structure.append(type)
            #temp = {type:level}
            #structure_code_dict.update(temp)
            code_struct.add_structure(type,level)
        else:
            #code_structure.append(type)
            code_struct.add_code_struct(type)
            #temp = {type:level}
            #structure_code_dict.update(temp)
            code_struct.add_structure(type,level)

    #bug，
    for s in code_struct.get_code_struct():
        structure_code_dict = code_struct.get_structure_code()
        if structure_code_dict[s] == "":
            code_struct.remove_structure(s)
            #code_structure.remove(s)
            #structure_code_dict.pop(s)
            #structure_logic_dict.pop(s)
    a = 0

    for s in code_struct.get_code_struct():
        structure_code_dict = code_struct.get_structure_code()
        unit = structure_code_dict[s]

        if s.startswith("import"):
            #import
            #：import math，math 
            #from math import sqrt, pow，sqrt、pow
            packages = re.findall(r"import\s+(.*)",unit)[0]
            
            pack = packages.split(",")
            for p in pack:
                #key，value，
                code_struct.add_import(p,structure_code_dict[s])

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
                #temp = {t:code_logic}
                #snippet_logic.update(temp)
                code_struct.add_snippet_logic(t,code_logic)


            #，x1,y1,x2,y2 =map(float, input().split())
            #

            #
            code_struct.add_structure_logic(s,code_logic)
        


        if s.startswith("assign"):
            #：
            #：x1 = map(float, input().split())，x1
            var = unit.split("=")[0]
            #
            var = var.replace(" ","")

            #todo:
            vars = var.split(",")

            dependencies = extract_dependencies(unit)
            logic = return_assign_explain(unit,dependencies,code_struct.get_class_logic(),code_struct.get_function_logic())

            for v in vars:


                #
                # （，）
                code_struct.add_assign_code(v,unit)

                #
                code_struct.add_structure_logic(s,logic)

                #temp = {v:logic}
                #snippet_logic.update(temp)
                code_struct.add_snippet_logic(v,logic)

            continue


        if s.startswith("define"):
            #，def()
            func_name = re.search(r"def(.*?)\(", unit).group(1)
            #
            func_name = func_name.replace(" ","")
                
            dependencies = extract_dependencies(unit)
            for d in dependencies:
                import_dict = code_struct.get_import()
                if d in import_dict:
                    #import，
                    unit = import_dict[d] + "\n" + unit
            if(code_depth(unit)<=TH):

                func_logic = return_func_explain(unit)
                #

            else:

                #(“”)
                #
                new_unit = extract_second_indent(unit)
                print("：",new_unit)
                sub_logic = OverAllLogic(new_unit,problem_statement,use_problem_statement,code_struct)
                #print(sub_logic)
                print("：",sub_logic)
                print("----------------------")
                #
                new_code = unit.split("\n")[0]+"**nested code block**"
                
                func_logic = return_func_explain(new_code+"nested code block logic:"+str(sub_logic))
            code_struct.add_function_logic(func_name,func_logic)

            #
            code_struct.add_structure_logic(s,func_logic)
            print(""+func_name+"：")
            print(func_logic)
            print("----------------------")
            #return return_snippet_explain3(new_code+"nested code block logic:"+str(sub_logic),dependencies,code_struct)




        if s.startswith("judge"):
            
            #“”，，

                #
            dependencies = extract_dependencies(unit)
            #print(return_snippet_explain2(unit,dependencies,snippet_logic))
            for d in dependencies:
                import_dict = code_struct.get_import()
                if d in import_dict:
                    #import，
                    unit = import_dict[d] + "\n" + unit

            unit = add_assign(unit,dependencies,code_struct.get_structure_code())

            if(code_depth(unit)<=TH):
                judge_logic,code_snippet = return_snippet_explain3(unit,dependencies,code_struct)


            else:
                #
                new_unit = extract_second_indent(unit)
                print("：",new_unit)
                sub_logic = OverAllLogic(new_unit,problem_statement,use_problem_statement,code_struct)
                #print(sub_logic)
                print("：",sub_logic)
                print("----------------------")
                #
                new_code = unit.split("\n")[0]+"**nested code block**"
                
                judge_logic,code_snippet = return_snippet_explain3(new_code+"nested code block logic:"+str(sub_logic),dependencies,code_struct)

            code_struct.add_structure_logic(s,judge_logic)

                #，
                #，
            for var in dependencies:
                if var in code_struct.get_snippet_logic():
                    #
                    ori_logic = code_struct.get_snippet_logic()[var]
                    new_logic = update_snippet_logic(judge_logic,var,code_snippet,ori_logic)

                    print(""+var+"：")
                    print(new_logic)
                    print("----------------------")
                    #
                    if var in code_struct.get_snippet_logic():
                        code_struct.update_snippet_logic(var,str(new_logic))
                    else:
                        code_struct.add_snippet_logic(var,str(new_logic))

            #，
            #，

        if s.startswith("loop"):
            #“”，，
            #
            dependencies = extract_dependencies(unit)
            #print(return_snippet_explain2(unit,dependencies,snippet_logic))

            for d in dependencies:
                import_dict = code_struct.get_import()
                if d in import_dict:
                    #import，
                    unit = import_dict[d] + "\n" + unit
            unit = add_assign(unit,dependencies,code_struct.get_structure_code())
            if(code_depth(unit)<=TH):
                loop_logic,code_snippet = return_snippet_explain3(unit,dependencies,code_struct)
                
            else:
                #
                new_unit = extract_second_indent(unit)
                print("：",new_unit)
                sub_logic = OverAllLogic(new_unit,problem_statement,use_problem_statement,code_struct)
                #print(sub_logic)
                print("：",sub_logic)
                print("----------------------")
                #
                new_code = unit.split("\n")[0]+"\n**nested code block**\n"
                
                loop_logic,code_snippet = return_snippet_explain3(new_code+"nested code block logic:"+str(sub_logic),dependencies,code_struct)

            code_struct.add_structure_logic(s,loop_logic)

            #，
            #，
            for var in dependencies:
                if var in code_struct.get_snippet_logic():
                    ori_logic = code_struct.get_snippet_logic()[var]
                    new_logic = update_snippet_logic(loop_logic,var,code_snippet,ori_logic)
                    print(""+var+"：")
                    print(new_logic)
                    print("----------------------")
                    #
                        
                    #varsnippet_logic，
                    code_struct.update_snippet_logic(var,str(new_logic))
                
        if s.startswith("class"):

            #“”，，

            #
            dependencies = extract_dependencies(unit)
            #print(return_snippet_explain2(unit,dependencies,snippet_logic))

            for d in dependencies:
                import_dict = code_struct.get_import()
                if d in import_dict:
                    #import，
                    unit = import_dict[d] + "\n" + unit
            #unit = add_assign(unit,dependencies,structure_code_dict)
            if(code_depth(unit)<=TH):
                class_logic,code_snippet = return_snippet_explain3(unit,dependencies,code_struct)

            else:
                #
                new_unit = extract_second_indent(unit)
                print("：",new_unit)
                sub_logic = OverAllLogic(new_unit,problem_statement,use_problem_statement,code_struct)
                #print(sub_logic)
                print("：",sub_logic)
                print("----------------------")
                #
                new_code = unit.split("\n")[0]+"**nested code block**"
                
                class_logic,code_snippet = return_snippet_explain3(new_code+"nested code block logic:"+str(sub_logic),dependencies,code_struct)
            code_struct.add_structure_logic(s,class_logic)

            #
            class_name = re.search(r"class(.*?):", unit).group(1)
            #
            class_name = class_name.replace(" ","").replace("(","").replace(")","")

            code_struct.add_class_logic(class_name,class_logic)
            temp = {s:class_logic}
            code_struct.add_class_logic(class_name,class_logic)




        if s.startswith("output"):
            dependencies = extract_dependencies(unit)
            logic = return_output_explain(unit,dependencies,code_struct.get_snippet_logic(),code_struct.get_function_logic())

            code_struct.add_structure_logic(s,logic)

    for s in code_struct.get_code_struct():
        print(s)
        if s =="assign":
            structure_code_dict = code_struct.get_structure_code()
            assign_code = structure_code_dict[s]
            #
            var = assign_code.split("=")[0]
            #
            var = var.replace(" ","")
            snippet_logic = code_struct.get_snippet_logic()
            if var in snippet_logic:
                var_logic = snippet_logic[var]
            
                #
                #structure_logic_dict[s] = var_logic
                code_struct.update_structure_logic(s,var_logic)


            continue


    #print(return_overall_explain(Gen_Code,code_structure,structure_code_dict,structure_logic_dict))
    if if_main:
        return return_overall_explain2(Gen_Code,code_struct.get_code_struct(),code_struct.get_structure_code(),code_struct.get_structure_logic())
    else:
        snippet_overall_explain = return_snippet_overall_explain(Gen_Code,code_struct.get_code_struct(),code_struct.get_structure_code(),code_struct.get_structure_logic())
        #（、、）
        code_struct.assign_code_struct(pre_code_struct)
        code_struct.assign_struct_code(pre_struct_code)
        code_struct.assign_struct_logic(pre_struct_logic)

        return snippet_overall_explain
        