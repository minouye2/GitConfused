from collections import defaultdict


class ReadAttribute():



    def get_code_attribute(self, methods_table, reader_location, data, op_codes, method_index, pool):
        add_one_byte = 1
        attribute_table = []
        values_to_return= [0,0]

        ############### attribute name index
        attribute_table.append(format((data[reader_location]), "02x"))
        attribute_table.append(format((data[reader_location + add_one_byte]), "02x"))

        ################## attribute length
        attribute_table.append(format((data[reader_location + 2]), "02x"))
        attribute_table.append(format((data[reader_location + 3]), "02x"))
        attribute_table.append(format((data[reader_location + 4]), "02x"))
        attribute_table.append(format((data[reader_location + 5]), "02x"))

        attribute_length = (data[reader_location + 2]) + (data[reader_location + 3]) \
                           + (data[reader_location + 4]) \
                           + (data[reader_location + 5])
        reader_location += 6
        ################# max stack
        attribute_table.append(format((data[reader_location]), "02x"))  # max stack
        attribute_table.append(format((data[reader_location + add_one_byte]), "02x"))
        reader_location += 2
        ###############   max locals
        attribute_table.append(format((data[reader_location]), "02x"))  # max locals
        attribute_table.append(format((data[reader_location + add_one_byte]), "02x"))
        reader_location += 2
        ###################  code length
        attribute_table.append(format((data[reader_location]), "02x")) # code length
        attribute_table.append(format((data[reader_location + add_one_byte]), "02x"))
        attribute_table.append(format((data[reader_location + 2]), "02x"))
        attribute_table.append(format((data[reader_location + 3]), "02x"))
        code_length = (data[reader_location]) + (data[reader_location + add_one_byte]) \
                      + (data[reader_location + 2]) + (data[reader_location + 3])
        reader_location += 4

        #################  opc odes
        i = 0
        while i < code_length:
            op_codes.append(format((data[reader_location]), "02x"))
            attribute_table.append(format((data[reader_location]), "02x"))
            i += 1
            reader_location += 1

        #############  exception table length
        exception_table_length = (data[reader_location]) + (data[reader_location + add_one_byte])

        attribute_table.append(format((data[reader_location]), "02x")) # exception table length
        attribute_table.append(format((data[reader_location + add_one_byte]), "02x"))
        reader_location += 2


        ############## exception table
        for x in range(exception_table_length):
            attribute_table.append(format((data[reader_location]), "02x"))  # start pc
            attribute_table.append(format((data[reader_location + add_one_byte]), "02x"))
            reader_location += 2
            attribute_table.append(format((data[reader_location]), "02x"))  # end pc
            attribute_table.append(format((data[reader_location + add_one_byte]), "02x"))
            reader_location += 2
            attribute_table.append(format((data[reader_location]), "02x"))  # handler pc pc
            attribute_table.append(format((data[reader_location + add_one_byte]), "02x"))
            reader_location += 2
            attribute_table.append(format((data[reader_location]), "02x"))  # catch type
            attribute_table.append(format((data[reader_location + add_one_byte]), "02x"))
            reader_location += 2


        ############## attribute count
        attribute_table.append(format((data[reader_location]), "02x"))  # attribute count
        attribute_table.append(format((data[reader_location + add_one_byte]), "02x"))
        next_attribute_count = (data[reader_location]) + (data[reader_location + add_one_byte])
        tag_location = (data[reader_location+2]) + (data[reader_location + 3])
        tag = pool[tag_location]
        reader_location += 2

        methods_table[method_index].append(attribute_table)

        for x in range(next_attribute_count):
            reader_location = ReadAttribute.get_attribute(self, tag, methods_table, reader_location, data, op_codes, method_index, pool)

        values_to_return[0] = reader_location
        values_to_return[1] = op_codes

        return values_to_return




    def get_line_number_table(self, methods_table, reader_location, data, op_codes, method_index, pool):
        line_number_table = []
        ##################    name index
        line_number_table.append(format((data[reader_location]), "02x"))
        line_number_table.append(format((data[reader_location + 1]), "02x"))

        ##################### attribute length
        line_number_table.append(format((data[reader_location + 2]), "02x"))
        line_number_table.append(format((data[reader_location + 3]), "02x"))
        line_number_table.append(format((data[reader_location + 4]), "02x"))
        line_number_table.append(format((data[reader_location + 5]), "02x"))
        attribute_length = (data[reader_location + 2]) + (data[reader_location + 3]) \
                           + (data[reader_location + 4]) + (data[reader_location + 5])
        reader_location += 6

        ############### line number table length
        line_number_table.append(format((data[reader_location]), "02x"))
        line_number_table.append(format((data[reader_location + 1]), "02x")) # not sure if this is correct for line number table length i jsut read 4 more
        line_number_table_length = ((data[reader_location])+ (data[reader_location + 1]))

        reader_location += 2


        #line_number_table = ((data[reader_location])+ (data[reader_location + 1]))
        for x in range(line_number_table_length):
            ########### start pc
            line_number_table.append(format((data[reader_location]), "02x"))
            line_number_table.append(format((data[reader_location + 1]), "02x"))
            reader_location += 2

            ########### line number
            line_number_table.append(format((data[reader_location]), "02x"))
            line_number_table.append(format((data[reader_location + 1]), "02x"))
            reader_location += 2


        methods_table[method_index].append(line_number_table)

        return reader_location

    def get_source_file(self, methods_table, reader_location, data, op_codes, method_index, pool):
        x=0
    # *DO NOT DELETE WILL NEED FOR LATER CLASS FILES*    
    """
    def get_local_variable_table(self, methods_table, reader_location, data, op_codes, method_index, pool):
        x=0
        local_variable_table = []
        ##################    name index
        local_variable_table.append(format((data[reader_location]), "02x"))
        local_variable_table.append(format((data[reader_location + 1]), "02x"))

        ##################### attribute length
        local_variable_table.append(format((data[reader_location + 2]), "02x"))
        local_variable_table.append(format((data[reader_location + 3]), "02x"))
        local_variable_table.append(format((data[reader_location + 4]), "02x"))
        local_variable_table.append(format((data[reader_location + 5]), "02x"))

        local_variable_length = (data[reader_location + 2]) + (data[reader_location + 3]) \
                              + (data[reader_location + 4]) + (data[reader_location + 5])
        reader_location += 6

        local_variable_table.append(format((data[reader_location]), "02x"))
        local_variable_table.append(format((data[reader_location + 1]), "02x"))

        local_variable_table_length = (data[reader_location]) + (data[reader_location + 1])
        reader_location += 2

        for x in range(local_variable_table_length):

            ########### start pc
            local_variable_table_length.append(format((data[reader_location]), "02x"))
            local_variable_table_length.append(format((data[reader_location + 1]), "02x"))
            reader_location += 2

            ########### length
            local_variable_table_length.append(format((data[reader_location]), "02x"))
            local_variable_table_length.append(format((data[reader_location + 1]), "02x"))
            reader_location += 2

            ########### name index
            local_variable_table_length.append(format((data[reader_location]), "02x"))
            local_variable_table_length.append(format((data[reader_location + 1]), "02x"))
            reader_location += 2

            ########### discriptor index
            local_variable_table_length.append(format((data[reader_location]), "02x"))
            local_variable_table_length.append(format((data[reader_location + 1]), "02x"))
            reader_location += 2

            ########### index
            local_variable_table_length.append(format((data[reader_location]), "02x"))
            local_variable_table_length.append(format((data[reader_location + 1]), "02x"))
            reader_location += 2

        methods_table[method_index].append(local_variable_table_length)

        return reader_location """



    def get_exceptions(self, methods_table, reader_location, data, op_codes, method_index, pool):
        exception_table = []
        ##################    name index
        exception_table.append(format((data[reader_location]), "02x"))
        exception_table.append(format((data[reader_location + 1]), "02x"))

        ##################### attribute length
        exception_table.append(format((data[reader_location + 2]), "02x"))
        exception_table.append(format((data[reader_location + 3]), "02x"))
        exception_table.append(format((data[reader_location + 4]), "02x"))
        exception_table.append(format((data[reader_location + 5]), "02x"))
        attribute_length = (data[reader_location + 2]) + (data[reader_location + 3]) \
                           + (data[reader_location + 4]) + (data[reader_location + 5])
        reader_location += 6

        #################### number of exceptions
        exception_table.append(format((data[reader_location]), "02x"))
        exception_table.append(format((data[reader_location + 1]), "02x"))

        number_of_exceptions = (data[reader_location ]) + (data[reader_location + 1])
        reader_location += 2

        for x in range(number_of_exceptions):
            exception_table.append(format((data[reader_location]), "02x"))
            exception_table.append(format((data[reader_location + 1]), "02x"))
            reader_location += 2


        methods_table[method_index].append(exception_table)

        return reader_location









    switcher = {
        "Code": get_code_attribute,  # 2+x bytes
        "LineNumberTable": get_line_number_table,  # 4 bytes
        "SourceFile": get_source_file,
        "Exceptions": get_exceptions,
        #"LocalVariableTable": get_local_variable_table,
    }


    def get_attribute(self, tag, methods_table, reader_location, data, op_codes, method_index, pool):

        method = ReadAttribute.switcher.get(tag, "invalid")
        return method(self, methods_table, reader_location, data, op_codes, method_index, pool)
