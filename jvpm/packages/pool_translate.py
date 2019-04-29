from collections import defaultdict
import struct
import binascii
from collections import deque
import numpy
from . import jvpm_opcodes, pool_methods
SUPER_INDEX = 0
METHODREFS = []
CP_STRINGS = []

# pylint: disable = C0111, R0201

# ****************************************************************************************

class PoolTranslate:

    def __init__(self, constant_pool, skips, name="testSaveVar.class"):

        self.name = name
        self.pulled_constant_pool = constant_pool

        self.byte_list_length = len(self.pulled_constant_pool.keys())
        self.key_list = list(self.pulled_constant_pool.keys())
        self.translated_pool = []
        self.current_pool_list = []
        self.constant_pool_index = 0
        self.current_pool_index = 0
        self.counter = 0
        self.pool_list_index = 0
        self.skips_in_pool = skips

        self.constant_pool_length = len(self.pulled_constant_pool)
        self.translated_pool = ["0"] * (self.constant_pool_length + self.skips_in_pool)
        self.SUPER_INDEX = 0

    def UTF_8_string(self, sub_list):  # 01
        #print(sub_list, "^^^^^^^^^^  sub list in utf   ^^^^^^^^^^")
        #complete_string = sub_list[0]


        index = 2
        complete_string = ""
        while index < len(sub_list):
            byte_to_translate = int(sub_list[index], 16)
            translated_byte = (byte_to_translate).to_bytes(1, byteorder='big')
            converted_text = translated_byte.decode("utf-8", "ignore")
            complete_string += converted_text
            index += 1
        self.translated_pool[self.current_pool_index] = complete_string
        return complete_string

    def tag_integer(self, sub_list):  # 03
        hex_full = ""
        for i in range(len(sub_list)):
            hex_full += sub_list[i]

    def tag_float(self, sub_list):  # 04
        hex_string = ""
        sub_list.reverse()
        for i in range(len(sub_list)):
            hex_string += sub_list[i]
        tuple_float = struct.unpack('<f', binascii.unhexlify(hex_string))
        dec_float = tuple_float[0]
        return dec_float

    def tag_long(self, sub_list):  # 5
        string_hex = "0x"
        for i in range(len(sub_list)):
            string_hex += sub_list[i]
        dec_long = int(string_hex,16)
        return dec_long

    def tag_double(self, sub_list):  # 6
        print("Double    8 bytes")

    def class_reference(self, sub_list):  # 7

        index = 0

        complete_string = ""
        strings_to_combine = 0

        while index < len(sub_list):
            new_index = int(sub_list[index], 16)

            pulled_string = PoolTranslate.method_dict(self, self.pulled_constant_pool, new_index)
            index += 1
            if len(sub_list) > 1:

                if strings_to_combine < 1:
                    pulled_string = pulled_string + "."
                strings_to_combine += 1
                complete_string += pulled_string
            else:
                complete_string = pulled_string

        return complete_string

    def string_reference(self, sub_list):  # 8
        index = 0

        complete_string = ""
        strings_to_combine = 0

        while index < len(sub_list):
            new_index = int(sub_list[index], 16)

            pulled_string = PoolTranslate.method_dict(self, self.pulled_constant_pool, new_index)
            index += 1
            if len(sub_list) > 1:

                if strings_to_combine < 1:
                    pulled_string = pulled_string + "."
                strings_to_combine += 1
                complete_string += pulled_string
            else:
                complete_string = pulled_string

        return complete_string

    def field_reference(self, sub_list):  # 9

        index = 0

        complete_string = ""
        strings_to_combine = 0

        while index < len(sub_list):
            new_index = int(sub_list[index], 16)

            pulled_string = PoolTranslate.method_dict(self, self.pulled_constant_pool, new_index)
            index += 1
            if len(sub_list) > 1:

                if strings_to_combine < 1:
                    pulled_string = pulled_string + "."
                strings_to_combine += 1
                complete_string += pulled_string
            else:
                complete_string = pulled_string

        return complete_string

    def method_reference(self, sub_list):  # 10
        index = 0

        complete_string = ""
        strings_to_combine = 0

        while index < len(sub_list):
            new_index = int(sub_list[index], 16)

            pulled_string = PoolTranslate.method_dict(self, self.pulled_constant_pool, new_index)
            methodrefs.append(pulled_string)
            index += 1

            if strings_to_combine < 1:
                pulled_string = pulled_string + "."
            strings_to_combine += 1
            complete_string += pulled_string

        return complete_string

    def interface_method_reference(self, sub_list):  # 11
        print("Interface Method Reference    4 bytes")

    def name_and_type_discriptor(self, sub_list):  # 12

        index = 0

        complete_string = ""
        strings_to_combine = 0

        while index < len(sub_list):
            new_index = int(sub_list[index], 16)

            pulled_string = PoolTranslate.method_dict(self, self.pulled_constant_pool, new_index)
            index += 1
            if strings_to_combine < 1:
                pulled_string = pulled_string + ":"
            strings_to_combine += 1
            complete_string += pulled_string

        return complete_string

    def method_handle(self, sub_list):  # 15
        print("Method Handle    3 bytes")

        type = {
            1: "REF_getField",
            2: "REF_getStatic",
            3: "REF_putField",
            4: "REF_putStatic",
            5: "REF_invokeVirtual",
            8: "REF_newInvokeSpecial",
            6: "REF_invokeStatic",
            7: "REF_invokeSpecial",
            9: "REF_invokeInterface"
        }

    def method_type(self, sub_list):  # 16
        print("Method Type    2 bytes")

    def dynamic(self, sub_list):  # 17
        print("Dynamic    4 bytes")

    def invoke_dynamic(self, sub_list):  # 18
        print("Invoke Dynamic    4 bytes")

    def module(self, sub_list):  # 19
        print("Module    2 bytes")

    def package(self, sub_list):  # 20
        print("Package    2 bytes")

    switcher = {

        "01": UTF_8_string,  # 2+x bytes
        "03": tag_integer,  # 4 bytes
        "04": tag_float,  # 4 bytes
        "05": tag_long,  # 8 bytes
        "06": tag_double,  # 8 bytes
        "07": class_reference,  # 2 bytes
        "08": string_reference,  # 2 bytes
        "09": field_reference,  # 4 bytes
        "0a": method_reference,  # 4 bytes
        "0b": interface_method_reference,  # 4 bytes
        "0c": name_and_type_discriptor,  # 4 bytes
        "0f": method_handle,  # 3 bytes
        "10": method_type,  # 2 bytes
        "11": dynamic,  # 4 bytes
        "12": invoke_dynamic,  # 4 bytes
        "13": module,  # 2 bytes
        "14": package,  # 2 bytes

    }

    def method_dict(self, constant_pool, current_index):

        current_key = current_index
        current_list = constant_pool[current_key]
        current_list_length = len(current_list)
        sub_list = []
        tag_byte = current_list[0]

        j = 1
        while j < current_list_length:
            sub_list.append(current_list[j])
            j += 1

        method = PoolTranslate.switcher.get(tag_byte, "invalid")

        return method(self, sub_list)

    def translate_pool(self):
        pool_translater = PoolTranslate(self.pulled_constant_pool, self.skips_in_pool,
                                        name=self.name)
        pool_index = 1
        while pool_index <= self.constant_pool_length + self.skips_in_pool-1:
            self.translated_pool[pool_index] = pool_translater.method_dict(self.pulled_constant_pool, pool_index)

            if (self.pulled_constant_pool[pool_index][0] == '05' or self.pulled_constant_pool[pool_index][0] == '06'):
                pool_index += 1
            pool_index += 1

        return self.translated_pool
