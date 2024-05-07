class CodeStructure:
    def __init__(self):
        # ：，snippet_name:logic
        self.snippet_logic = {} 
        # ： assign_name:code
        self.assign_code = {}
        # ："import"
        self.code_structure = []
        # (import)：
        self.structure_code_dict = {}
        # ：structure_name:logic
        self.structure_logic_dict = {}
        #  module_name:import_logic
        self.import_dict = {}
        # : {function_name:logic}
        self.function_logic_dict = {}
        # class_name:logic
        self.class_logic_dict = {}

    def add_code_struct(self, structure_name):
        self.code_structure.append(structure_name)

    def add_structure(self, structure_name, code):
        """  """
        temp = {structure_name:code}
        self.structure_code_dict.update(temp)
    
    def add_structure_logic(self, structure_name, logic):
        """  """
        temp = {structure_name:logic}
        self.structure_logic_dict.update(temp)

    def add_snippet_logic(self, snippet_name, logic):
        """ snippet """
        temp = {snippet_name:logic}
        self.snippet_logic.update(temp)

    def add_assign_code(self, assign_name, code):
        """  """
        temp = {assign_name:code}
        self.assign_code.update(temp)

    def add_import(self, module_name, import_logic):
        """ import """
        temp = {module_name:import_logic}
        self.import_dict.update(temp)

    def add_function_logic(self, function_name, logic):
        """  """
        temp = {function_name:logic}
        self.function_logic_dict.update(temp)

    def add_class_logic(self, class_name, logic):
        """  """
        temp = {class_name:logic}
        self.class_logic_dict.update(temp)

    def get_structure_code(self):
        """  """
        return self.structure_code_dict
    
    def get_snippet_logic(self):
        """ snippet """
        return self.snippet_logic
    
    def get_assign_code(self):
        """  """
        return self.assign_code

    def get_structure_logic(self):
        """  """
        return self.structure_logic_dict

    def get_import(self):
        """ import """
        return self.import_dict

    def get_function_logic(self):
        """  """
        return self.function_logic_dict

    def get_class_logic(self):
        """  """
        return self.class_logic_dict
    def get_code_struct(self):
        """  """
        return self.code_structure
    def remove_structure(self, structure_name):
        """  """
        self.code_structure.remove(structure_name)
        self.structure_code_dict.pop(structure_name)
    def update_structure_logic(self, structure_name, logic):
        """  """
        self.structure_logic_dict[structure_name] = logic
    def update_function_logic(self, function_name, logic):
        """  """
        self.function_logic_dict[function_name] = logic
    def update_snippet_logic(self, snippet_name, logic):
        """ snippet """
        self.snippet_logic[snippet_name] = logic

    def assign_code_struct(self,struct):
        self.code_structure = struct
    def delete_code_struct(self):
        self.code_structure = []

    def assign_struct_code(self,struct_code):
        self.structure_code_dict = struct_code
    def delete_struct_code(self):
        self.structure_code_dict = {}

    def assign_struct_logic(self,struct_logic):
        self.structure_logic_dict = struct_logic
    def delete_struct_logic(self):
        self.structure_logic_dict = {}
        
        