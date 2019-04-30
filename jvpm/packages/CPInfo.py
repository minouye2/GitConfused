"""Module that parses the Constant Pool."""

# pylint: disable=C0111,W0612

class ConstInfo:
    """Class with modules that parse the CP."""

    def __init__(self):
        self.tag = None
        self.pool = []

    def read(self, bits):
        tag = bits.read('hex:8')
        self.pool.append(tag)

        self.const_tag_dict[tag](self, bits)

        return self.pool

    def parse_class(self, bits):
        for i in range(2):
            next_byte = bits.read('hex:8')
            if next_byte != "00":
                self.pool.append(next_byte)

    def parse_field(self, bits):
        for i in range(4):
            next_byte = bits.read('hex:8')
            if next_byte != "00":
                self.pool.append(next_byte)

    def parse_method(self, bits):
        for i in range(4):
            next_byte = bits.read('hex:8')
            if next_byte != "00":
                self.pool.append(next_byte)

    def parse_interface(self, bits):
        for i in range(4):
            next_byte = bits.read('hex:8')
            if next_byte != "00":
                self.pool.append(next_byte)

    def parse_string(self, bits):
        for i in range(2):
            next_byte = bits.read('hex:8')
            if next_byte != "00":
                self.pool.append(next_byte)

    def parse_integer(self, bits):
        for i in range(2):
            next_byte = bits.read('hex:8')
            if next_byte != "00":
                self.pool.append(next_byte)

    def parse_float(self, bits):
        for i in range(4):
            next_byte = bits.read('hex:8')
            if next_byte != "00":
                self.pool.append(next_byte)

    def parse_long(self, bits):
        for i in range(8):
            next_byte = bits.read('hex:8')
            if next_byte != "00":
                self.pool.append(next_byte)


    def parse_double(self, bits):
        for i in range(8):
            next_byte = bits.read('hex:8')
            if next_byte != "00":
                self.pool.append(next_byte)

    def parse_name_and_type(self, bits):
        for i in range(4):
            next_byte = bits.read('hex:8')
            if next_byte != "00":
                self.pool.append(next_byte)

    def parse_UTF8(self, bits):
        self.pool.append(bits.read('hex:8'))
        self.pool.append(bits.read('hex:8'))
        bytes_to_read = int(self.pool[1], 16)+int(self.pool[2], 16)

        for i in range(bytes_to_read):
            next_byte = bits.read('hex:8')
            self.pool.append(next_byte)

    def parse_method_handle(self, bits):
        for i in range(3):
            next_byte = bits.read('hex:8')
            if next_byte != "00":
                self.pool.append(next_byte)

    def parse_method_type(self, bits):
        for i in range(2):
            next_byte = bits.read('hex:8')
            if next_byte != "00":
                self.pool.append(next_byte)

    def parse_invoke_dynamic(self, bits):
        for i in range(4):
            next_byte = bits.read('hex:8')
            if next_byte != "00":
                self.pool.append(next_byte)

    const_tag_dict = {
        "07" : parse_class,
        "09" : parse_field,
        "0a" : parse_method,
        "0b" : parse_interface,
        "08" : parse_string,
        "03" : parse_integer,
        "04" : parse_float,
        "05" : parse_long,
        "06" : parse_double,
        "0c" : parse_name_and_type,
        "01" : parse_UTF8,
        "0f" : parse_method_handle,
        "10" : parse_method_type,
        "12" : parse_invoke_dynamic,
    }