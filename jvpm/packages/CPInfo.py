from bitstring import ConstBitStream
import struct

class ConstInfo:

    def __init__(self):
        self.tag = None
        self.pool = []

    def read(self, bits):
        #pool = []
        tag = bits.read('hex:8')
        self.pool.append(tag)

        self.const_tag_dict[tag](self, bits)

        return self.pool

    def parseClass(self, bits):
        for i in range(2):
            next_byte = bits.read('hex:8')
            if (next_byte != "00"):
                self.pool.append(next_byte)

    def parseField(self, bits):
        for i in range(4):
            next_byte = bits.read('hex:8')
            if (next_byte != "00"):
                self.pool.append(next_byte)

    def parseMethod(self, bits):
        for i in range(4):
            next_byte = bits.read('hex:8')
            if (next_byte != "00"):
                self.pool.append(next_byte)

    def parseInterface(self, bits):
        for i in range(4):
            next_byte = bits.read('hex:8')
            if (next_byte != "00"):
                self.pool.append(next_byte)

    def parseString(self, bits):
        for i in range(2):
            next_byte = bits.read('hex:8')
            if (next_byte != "00"):
                self.pool.append(next_byte)

    def parseInteger(self, bits):
        for i in range(2):
            next_byte = bits.read('hex:8')
            if (next_byte != "00"):
                self.pool.append(next_byte)

    def parseFloat(self, bits):
        for i in range(4):
            next_byte = bits.read('hex:8')
            if (next_byte != "00"):
                self.pool.append(next_byte)

    def parseLong(self, bits):
        for i in range(8):
            next_byte = bits.read('hex:8')
            if (next_byte != "00"):
                self.pool.append(next_byte)


    def parseDouble(self, bits):
        for i in range(8):
            next_byte = bits.read('hex:8')
            if (next_byte != "00"):
                self.pool.append(next_byte)

    def parseNameAndType(self, bits):
        for i in range(4):
            next_byte = bits.read('hex:8')
            if (next_byte != "00"):
                self.pool.append(next_byte)

    def parseUTF8(self, bits):
        self.pool.append(bits.read('hex:8'))
        self.pool.append(bits.read('hex:8'))
        bytes_to_read = int(self.pool[1], 16)+int(self.pool[2], 16)

        for i in range(bytes_to_read):
            next_byte = bits.read('hex:8')
            self.pool.append(next_byte)

    def parseMethodHandle(self, bits):
        for i in range(3):
            next_byte = bits.read('hex:8')
            if (next_byte != "00"):
                self.pool.append(next_byte)

    def parseMethodType(self, bits):
        for i in range(2):
            next_byte = bits.read('hex:8')
            if (next_byte != "00"):
                self.pool.append(next_byte)

    def parseInvokeDynamic(self, bits):
        for i in range(4):
            next_byte = bits.read('hex:8')
            if (next_byte != "00"):
                self.pool.append(next_byte)

    const_tag_dict = {
        "07" : parseClass,
        "09" : parseField,
        "0a" : parseMethod,
        "0b" : parseInterface,
        "08" : parseString,
        "03" : parseInteger,
        "04" : parseFloat,
        "05" : parseLong,
        "06" : parseDouble,
        "0c" : parseNameAndType,
        "01" : parseUTF8,
        "0f" : parseMethodHandle,
        "10" : parseMethodType,
        "12" : parseInvokeDynamic,
    }
