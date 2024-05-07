def extract_first_level(code):
    lines = code.split("\n")
    i = 0
    first_level_sections = []

    while i < len(lines):
        if not lines[i].startswith(" "):  # 4（1）
            if lines[i].startswith('if'):
                #if else
                section = lines[i]
                i += 1
                while i < len(lines) and lines[i].startswith(" "):
                    section += "\n" + lines[i]
                    i += 1
                temp = lines[i]
                while(lines[i].startswith('else')or lines[i].startswith('elif')):
                    section += "\n" + lines[i]
                    i += 1
                    while i < len(lines) and lines[i].startswith(" "):
                        section += "\n" + lines[i]
                        i += 1
                first_level_sections.append(section)
            else:
                section = lines[i]
                i += 1
                while i < len(lines) and lines[i].startswith(" "):  # 
                    section += "\n" + lines[i]
                    i += 1
                first_level_sections.append(section)
        else:
            i += 1

    return first_level_sections


#，，
def extract_second_indent(code):
    lines = code.split("\n")
    output = []
    indent_level = None

    for line in lines:
        stripped = line.lstrip()
        if not stripped:  # Skip empty lines
            continue

        indent = len(line) - len(stripped)
    

        # If this is a new base level of indentation
        if indent_level is None and indent:
            indent_level = indent
            output.append(line)
        elif indent_level is not None:
            # If this line is the same or deeper level of indentation, add to output
            if indent >= indent_level:
                output.append(line)
            else:  # Otherwise, break as we've returned to a top-level line
                break
    #，
    leading_spaces = len(output[0]) - len(output[0].lstrip(' '))
    for i in range(len(output)):
        output[i] = output[i][leading_spaces:]
    return "\n".join(output)
    

def strip_spaces(newcode):
    while newcode.startswith("    "):
        temcode = newcode.split("\n")
        temcode2 = ""
        for i in range(len(temcode)):
            temcode[i] = temcode[i][4:]
            temcode2 += temcode[i] + "\n"
        newcode = temcode2
    return temcode2

def code_strip_spaces(code):
    #
    newcode = code.split("\n")
    temp = ""
    for line in newcode:
        if line == "":
            continue
        #，
        elif line.lstrip().startswith('#'):
            continue
        #"""（），
        elif line.lstrip().startswith('"""'):
            continue
        else:
            temp += line + "\n"
    return temp

#if __name__ == "__main__":
def code_srtip_main(code):
    newcode = extract_first_level(code)
    main_code = ""
    for c in newcode:
        if c.startswith("if __name__ == '__main__'") or c.startswith("if __name__ == \"__main__\""):
            #if __name__ == "__main__" ，mian
            lines = c.split("\n")
            lines.pop(0)
            #，main
            
            #
            leading_spaces = len(lines[0]) - len(lines[0].lstrip(' '))
            for line in lines:
                main_code += line[leading_spaces:] + "\n"
    for c in newcode:
        if c.startswith("if __name__ == '__main__'") or c.startswith("if __name__ == \"__main__\""):
            #newcodec
            newcode.remove(c)
            #main_code
            newcode.append(main_code)
    #newcode
    newcode = "\n".join(newcode)

            
    return newcode
    



def get_indent_level(line, tab_size=4):
    # 
    line = line.replace('\t', ' ' * tab_size)
    # 
    return len(line) - len(line.lstrip(' '))

def code_depth(code):
    lines = code.split('\n')
    max_indent = 0
    indent_levels = [0]  # 

    for line in lines:
        if not line.strip():  # 
            continue
        indent = get_indent_level(line)
        # ，
        if indent > indent_levels[-1]:
            indent_levels.append(indent)
            max_indent = max(max_indent, len(indent_levels) - 1)
        # ，
        else:
            # 
            while indent_levels and indent < indent_levels[-1]:
                indent_levels.pop()
            # ，
            if indent_levels and indent != indent_levels[-1]:
                indent_levels.append(indent)
    
    return max_indent

def code_width(code):
    #
    lines = code.split("\n")
    #
    for line in lines:
        if line == "":
            lines.remove(line)
    
    return len(lines)














