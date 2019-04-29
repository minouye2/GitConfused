from collections import defaultdict

# ****************************************************************************************

class TagTranslate():

    def UTF_8_string(self):
        return "UTF 8 String"

    def integer(self):
        return "Integer"

    def float(self):
        return "Float"

    def long(self):
        return "Long"

    def double(self):
        return "Double"

    def class_reference(self):
        return "Class Reference"

    def string_reference(self):
        return "String Reference"

    def field_reference(self):
        return"Field Reference"

    def method_reference(self):
        return "Method Reference"

    def interface_method_reference(self):
        return "Interface Method Reference"

    def name_and_type_discriptor(self):
        return "Name and Type"

    def method_handle(self):
        return "Method Handle"

    def method_type(self):
        return "Method Type"

    def dynamic(self):
        return"Dynamic"

    def invoke_dynamic(self):
        return "Invoke Dynamic"

    def module(self):
        return "Module"

    def package(self):
        return "Package"

# ****************************************************************************************
    
    switcher = {

        "01": UTF_8_string,  # add two ints
        "03": integer,  # add two ints
        "04": float,  # add two ints
        "05": long,  # add two ints
        "06": double,  # add two ints
        "07": class_reference,  # add two ints
        "08": string_reference,  # add two ints
        "09": field_reference,  # add two ints
        "0a": method_reference,  # add two ints
        "0b": interface_method_reference,  # add two ints
        "0c": name_and_type_discriptor,  # add two ints
        "0f": method_handle,  # add two ints
        "10": method_type,  # add two ints
        "11": dynamic,  # add two ints
        "12": invoke_dynamic,  # add two ints
        "13": module,  # add two ints
        "14": package,  # add two ints

    }

# ****************************************************************************************

    def token_dict(self, argument):
        method = TagTranslate.switcher.get(argument, "invalid")
        # execute function
        return method(self)
    
# ****************************************************************************************

