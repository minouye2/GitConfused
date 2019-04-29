import unittest
from unittest.mock import mock_open, patch, call
from jvpm import packages
import sys
from collections import deque, defaultdict


class UnittestHeader(unittest.TestCase):

    def setUp(self):
        m = mock_open(read_data='CAFEBABE00000036000F')
        with patch(__name__ + '.open', m):
            self.cf = packages.jvpm_opcodes.HeaderClass()

class test_get_opcode(unittest.TestCase):
    def test_opcode(self):
        self.assertEqual(packages.jvpm_dict.get_opcode("91"), "i2b")
        self.assertEqual(packages.jvpm_dict.get_opcode("82"), "ixor")
        self.assertEqual(packages.jvpm_dict.get_opcode("1c"), "iload_2")
        self.assertEqual(packages.jvpm_dict.get_opcode("03"), "iconst_0")
        self.assertEqual(packages.jvpm_dict.get_opcode("SQ"), "Byte code not found!")

class test_const_pool(unittest.TestCase):
    def test_const_pool(self):

        x = packages.jvpm_opcodes.HeaderClass(name= "jvpm/javafiles/tester.class")
        x.get_magic()  # pragma: no cover
        x.get_minor()  # pragma: no cover
        x.get_major()
        #x.data = self.data
        n = x.get_const_pool()

        a = {
            0: ['0a', '03', '13'],
            1: ['07', '14'],
            2: ['07', '15'],
            3: ['01', '00', '06', '3c', '69', '6e', '69', '74', '3e'],
            4: ['01', '00', '03', '28', '29', '56'],
            5: ['01', '00', '04', '43', '6f', '64', '65'],
            6: ['01', '00', '0f', '4c', '69', '6e', '65', '4e', '75', '6d', '62', '65', '72', '54', '61', '62', '6c', '65'],
            7: ['01', '00', '12', '4c', '6f', '63', '61', '6c', '56', '61', '72', '69', '61', '62', '6c', '65', '54', '61','62', '6c', '65'],
            8: ['01', '00', '04', '74', '68', '69', '73'],
            9: ['01', '00', '08', '4c', '74', '65', '73', '74', '65', '72', '3b'],
            10: ['01', '00', '04', '6d', '61', '69', '6e'],
            11: ['01', '00', '16', '28', '5b', '4c', '6a', '61', '76', '61', '2f', '6c', '61', '6e', '67', '2f', '53', '74','72', '69', '6e', '67', '3b', '29', '56'],
            12: ['01', '00', '04', '61', '72', '67', '73'],
            13: ['01', '00', '13', '5b', '4c', '6a', '61', '76', '61', '2f', '6c', '61', '6e', '67', '2f', '53', '74', '72','69', '6e', '67', '3b'],
            14: ['01', '00', '01', '61'],
            15: ['01', '00', '01', '49'],
            16: ['01', '00', '0a', '53', '6f', '75', '72', '63', '65', '46', '69', '6c', '65'],
            17: ['01', '00', '0b', '74', '65', '73', '74', '65', '72', '2e', '6a', '61', '76', '61'],
            18: ['0c', '04', '05'],
            19: ['01', '00', '06', '74', '65', '73', '74', '65', '72'],
            20: ['01', '00', '10', '6a', '61', '76', '61', '2f', '6c', '61', '6e', '67', '2f', '4f', '62', '6a', '65', '63','74']
        }

        self.assertEqual(n[1], a[0])
        self.assertEqual(n[2], a[1])
        self.assertEqual(n[3], a[2])
        self.assertEqual(n[4], a[3])
        self.assertEqual(n[5], a[4])
        self.assertEqual(n[6], a[5])
        self.assertEqual(n[7], a[6])
        self.assertEqual(n[8], a[7])
        self.assertEqual(n[9], a[8])
        self.assertEqual(n[10], a[9])
        self.assertEqual(n[11], a[10])
        self.assertEqual(n[12], a[11])
        self.assertEqual(n[13], a[12])
        self.assertEqual(n[14], a[13])
        self.assertEqual(n[15], a[14])
        self.assertEqual(n[16], a[15])


class test_pool_translate1(unittest.TestCase):

    def test_working_methods(self):
        jvpm_opcodes_obj = packages.jvpm_opcodes.HeaderClass(name="jvpm/javafiles/testSaveVar.class")
        jvpm_opcodes_obj.get_magic()
        jvpm_opcodes_obj.get_minor()
        jvpm_opcodes_obj.get_major()  # pragma: no cover
        n = jvpm_opcodes_obj.get_const_pool()
        y = packages.pool_translate.PoolTranslate(n, jvpm_opcodes_obj.skips_in_constant_pool,
                                                  name="jvpm/javafiles/testSaveVar.class")


        # y.dictionary = x.get_const_pool()
       # b = defaultdict(list)
        #b = jvpm_opcodes_obj.get_const_pool()
        new_array = ["0",
                     "java/lang/Object.<init>:()V",
                     "hello",
                     1002,
                     "0",
                     None,
                     "0",
                     "java/lang/System.out:Ljava/io/PrintStream;",
                     None,
                     "java/io/PrintStream.println:(Ljava/lang/String;)V",
                     "testSaveVar",
                     "java/lang/Object",
                     "<init>",
                     "()V",
                     "Code",
                     "LineNumberTable",
                     "LocalVariableTable",
                     "this",
                     "LtestSaveVar;",
                     "main",
                     "([Ljava/lang/String;)V",
                     "args",
                     "[Ljava/lang/String;",
                     "myInt",
                     "I",
                     "myString",
                     "Ljava/lang/String;",
                     "myLong",
                     "J",
                     "myDouble",
                     "D",
                     "SourceFile",
                     "testSaveVar.java",
                     "<init>:()V",
                     "hello",
                     "java/lang/System",
                     "out:Ljava/io/PrintStream;",
                     "BootstrapMethods",
                     None,
                     "\x01 \x01 \x01 \x01",
                     "makeConcatWithConstants:(ILjava/lang/String;JD)Ljava/lang/String;",
                     "java/io/PrintStream",
                     "println:(Ljava/lang/String;)V",
                     "testSaveVar",
                     "java/lang/Object",
                     "java/lang/System",
                     "out",
                     "Ljava/io/PrintStream;",
                     "java/lang/invoke/StringConcatFactory.makeConcatWithConstants:(Ljava/lang/invoke/MethodHandles$Lookup;Ljava/lang/String;Ljava/lang/invoke/MethodType;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/invoke/CallSite;",
                     "\x01 \x01 \x01 \x01",
                     "makeConcatWithConstants",
                     "(ILjava/lang/String;JD)Ljava/lang/String;",
                     "java/io/PrintStream",
                     "println",
                     "(Ljava/lang/String;)V",
                     "java/lang/invoke/StringConcatFactory",
                     "makeConcatWithConstants:(Ljava/lang/invoke/MethodHandles$Lookup;Ljava/lang/String;Ljava/lang/invoke/MethodType;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/invoke/CallSite;",
                     "java/lang/invoke/StringConcatFactory",
                     "java/lang/invoke/MethodHandles$Lookup",
                     "Lookup",
                     "InnerClasses",
                     "(Ljava/lang/invoke/MethodHandles$Lookup;Ljava/lang/String;Ljava/lang/invoke/MethodType;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/invoke/CallSite;",
                     "java/lang/invoke/MethodHandles",
                     "java/lang/invoke/MethodHandles$Lookup",
                     "java/lang/invoke/MethodHandles"
                     ]

        a = {
            0: "0",
            1: "java/lang/Object.<init>:()V",
            2: "hello",
            3: "1002",
            4: "0",
            5: None,
            6: "0",
            7: "java/lang/System.out:Ljava/io/PrintStream;",
            8: None,
            9: "java/io/PrintStream.println:(Ljava/lang/String;)V",
            10: "testSaveVar",
            11: "java/lang/Object",
            12: "<init>",
            13: "()V",
            14: "Code",
            15: "LineNumberTable",
            16: "LocalVariableTable",
            17: "this",
            18: "LtestSaveVar;",
            19: "main",
            20: "([Ljava/lang/String;)V",
            21: "args",
            22: "[Ljava/lang/String;",
            23: "myInt",
            24: "I",
            25: "myString",
            26: "Ljava/lang/String;",
            27: "myLong",
            28: "J",
            29: "myDouble",
            30: "D",
            31: "SourceFile",
            32: "testSaveVar.java",
            33: "<init>:()V",
            34: "hello",
            35: "java/lang/System",
            36: "out:Ljava/io/PrintStream;",
            37: "BootstrapMethods",
            38: None,
            39: "\x01 \x01 \x01 \x01",
            40: "makeConcatWithConstants:(ILjava/lang/String;JD)Ljava/lang/String;",
            41: "java/io/PrintStream",
            42: "println:(Ljava/lang/String;)V",
            43: "testSaveVar",
            44: "java/lang/Object",
            45: "java/lang/System",
            46: "out",
            47: "Ljava/io/PrintStream;",
            48: "java/lang/invoke/StringConcatFactory.makeConcatWithConstants:(Ljava/lang/invoke/MethodHandles$Lookup;Ljava/lang/String;Ljava/lang/invoke/MethodType;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/invoke/CallSite;",
            49: "\x01 \x01 \x01 \x01",
            50: "makeConcatWithConstants",
            51: "(ILjava/lang/String;JD)Ljava/lang/String;",
            52: "java/io/PrintStream",
            53: "println",
            54: "(Ljava/lang/String;)V",
            55: "java/lang/invoke/StringConcatFactory",
            56: "makeConcatWithConstants:(Ljava/lang/invoke/MethodHandles$Lookup;Ljava/lang/String;Ljava/lang/invoke/MethodType;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/invoke/CallSite;",
            57: "java/lang/invoke/StringConcatFactory",
            58: "java/lang/invoke/MethodHandles$Lookup",
            59: "Lookup",
            60: "InnerClasses",
            61: "(Ljava/lang/invoke/MethodHandles$Lookup;Ljava/lang/String;Ljava/lang/invoke/MethodType;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/invoke/CallSite;",
            62: "java/lang/invoke/MethodHandles",
            63: "java/lang/invoke/MethodHandles$Lookup",
            64: "java/lang/invoke/MethodHandles"
        }

        new_dict = y.translate_pool()

        n = {
            0: 'java/lang/Object.<init>:()V',
            1: 'tester',
            2: 'java/lang/Object',
            3: '<init>',
            4: '()V',
            5: 'Code',
            6: 'LineNumberTable',
            7: 'LocalVariableTable',
            8: 'this',
            9: 'Ltester;',
            10: 'main',
            11: '([Ljava/lang/String;)V',
            12: 'args',
            13: '[Ljava/lang/String;',
            14: 'a',
            15: 'I',
            16: 'SourceFile',
            17: 'tester.java',
            18: '<init>:()V',
            19: 'tester',
            20: 'java/lang/Object'

        }

        self.assertEqual(new_dict, new_array)
        """
        self.assertEqual(new_dict[1], n[0])
        self.assertEqual(new_dict[2], n[1])
        self.assertEqual(new_dict[3], n[2])
        self.assertEqual(new_dict[4], n[3])
        self.assertEqual(new_dict[5], n[4])
        self.assertEqual(new_dict[6], n[5])
        self.assertEqual(new_dict[7], n[6])
        self.assertEqual(new_dict[8], n[7])
        self.assertEqual(new_dict[9], n[8])
        self.assertEqual(new_dict[10], n[9])
        self.assertEqual(new_dict[11], n[10])
        self.assertEqual(new_dict[12], n[11])
        self.assertEqual(new_dict[13], n[12])
        self.assertEqual(new_dict[14], n[13])
        self.assertEqual(new_dict[15], n[14])
        self.assertEqual(new_dict[16], n[15])
        self.assertEqual(new_dict[17], n[16])
        self.assertEqual(new_dict[18], n[17])
        self.assertEqual(new_dict[19], n[18])
        self.assertEqual(new_dict[20], n[19])
        self.assertEqual(new_dict[21], n[20])
        """


class test_pool_methods(unittest.TestCase):
    def test_tag_translate(self):
         jvpm_opcodes_obj = packages.jvpm_opcodes.HeaderClass(name="jvpm/javafiles/tester.class")
         jvpm_opcodes_obj.get_magic()
         jvpm_opcodes_obj.get_minor()
         jvpm_opcodes_obj.get_major()  # pragma: no cover
         n = jvpm_opcodes_obj.get_const_pool()
         x = packages.pool_translate.PoolTranslate(n, jvpm_opcodes_obj.skips_in_constant_pool,
                                                  name="jvpm/javafiles/tester.class")
         new_dict = {
             "1": "01",
             "2": "03",
             "3": "04",
             "4": "05",
             "5": "06",
             "6": "07",
             "7": "08",
             "8": "09",
             "9": "0a",
             "10": "0b",
             "11": "0c",
             "12": "0f",
             "13": "10",
             "14": "11",
             "15": "12",
             "16": "13",
             "17": "14"
         }
         #x = packages.pool_translate.PoolTranslate(name ="jvpm/javafiles/tester.class")
         """
         x.field_reference()
         sys.stdout.assert_has_calls(
             [call.write("Field Reference    4 bytes")]
         )
         """
         x_list = [0]



         x.interface_method_reference(x_list)
         sys.stdout.assert_has_calls(
             [call.write("Interface Method Reference    4 bytes")]
         )

         x.method_handle(x_list)
         sys.stdout.assert_has_calls(
             [call.write("Method Handle    3 bytes")]
         )

         x.method_type(x_list)
         sys.stdout.assert_has_calls(
             [call.write("Method Type    2 bytes")]
         )

         x.dynamic(x_list)
         sys.stdout.assert_has_calls(
             [call.write("Dynamic    4 bytes")]
         )
         x.invoke_dynamic(x_list)
         sys.stdout.assert_has_calls(
             [call.write("Invoke Dynamic    4 bytes")]
         )
         x.module(x_list)
         sys.stdout.assert_has_calls(
             [call.write("Module    2 bytes")]
         )
         x.package(x_list)
         sys.stdout.assert_has_calls(
             [call.write("Package    2 bytes")]
         )


         x = packages.pool_methods.TagTranslate()
         self.assertEqual(x.token_dict(new_dict['1']), "UTF 8 String")
         self.assertEqual(x.token_dict(new_dict['2']), "Integer")
         self.assertEqual(x.token_dict(new_dict['3']), "Float")
         self.assertEqual(x.token_dict(new_dict['4']), "Long")
         self.assertEqual(x.token_dict(new_dict['5']), "Double")
         self.assertEqual(x.token_dict(new_dict['6']), "Class Reference")
         self.assertEqual(x.token_dict(new_dict['7']), "String Reference")
         self.assertEqual(x.token_dict(new_dict['8']), "Field Reference")
         self.assertEqual(x.token_dict(new_dict['9']), "Method Reference")
         self.assertEqual(x.token_dict(new_dict['10']), "Interface Method Reference")
         self.assertEqual(x.token_dict(new_dict['11']), "Name and Type")
         self.assertEqual(x.token_dict(new_dict['12']), "Method Handle")
         self.assertEqual(x.token_dict(new_dict['13']), "Method Type")
         self.assertEqual(x.token_dict(new_dict['14']), "Dynamic")
         self.assertEqual(x.token_dict(new_dict['15']), "Invoke Dynamic")
         self.assertEqual(x.token_dict(new_dict['16']), "Module")
         self.assertEqual(x.token_dict(new_dict['17']), "Package")

class test_stack(unittest.TestCase):
    def test_is_empty(self):
        s = packages.stack.Stack()
        s.push(1)
        s.pop()
        self.assertTrue(s.is_empty())

    def test_push(self):
        s = packages.stack.Stack()
        s.push(2)
        s.push(3)
        v = s.pop()
        self.assertEqual(v, 3)

    def test_pop(self):
        s = packages.stack.Stack()
        s.push(3)
        s.push(2)
        s.push(4)
        s.push(0)
        a = s.pop()
        b = s.pop()
        self.assertEqual(a, 0)
        self.assertEqual(b, 4)

    def test_peek(self):
        s = packages.stack.Stack()
        s.push("hello")
        s.push("hi")
        self.assertEqual(s.peek(),"hi")
        s.pop()

    def test_size(self):
        s = packages.stack.Stack()
        s.push("hello")
        s.push(2)
        s.push("hi")
        self.assertEqual(s.size(), 3)
        s.pop()
        self.assertEqual(s.size(), 2)

class Test_Op_Methods(unittest.TestCase):

    def test_iadd(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()
        # packages.jvpm_methods.S.push(1) EXAMPLE THAT I USED IN THE MAIN AND IT WORKS
        packages.jvpm_methods.S.push(2)
        packages.jvpm_methods.S.push(1)
        a.iadd(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 3)

    def test_iand(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.S.push(5)
        packages.jvpm_methods.S.push(3)
        a.iand(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b,1)

    def test_iconst_m1(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()
        a.iconst_m1(op, con, arg)
        b = packages.jvpm_methods.S.peek()
        self.assertEqual(b, -1)
        packages.jvpm_methods.S.push(5)
        self.assertEqual(packages.jvpm_methods.S.peek(), 5)
        self.assertNotEqual(packages.jvpm_methods.S.peek(), -1)

    def test_iconst_0(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()
        a.iconst_0(op, con, arg)
        b = packages.jvpm_methods.S.peek()
        self.assertEqual(b, 0)
        packages.jvpm_methods.S.push(5)
        self.assertEqual(packages.jvpm_methods.S.peek(), 5)
        self.assertNotEqual(packages.jvpm_methods.S.peek(), 0)

    def test_iconst_1(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()
        a.iconst_1(op, con, arg)
        b = packages.jvpm_methods.S.peek()
        self.assertEqual(b, 1)
        packages.jvpm_methods.S.push(5)
        self.assertEqual(packages.jvpm_methods.S.peek(), 5)
        self.assertNotEqual(packages.jvpm_methods.S.peek(), 1)

    def test_iconst_2(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()
        a.iconst_2(op, con, arg)
        b = packages.jvpm_methods.S.peek()
        self.assertEqual(b, 2)
        packages.jvpm_methods.S.push(5)
        self.assertEqual(packages.jvpm_methods.S.peek(), 5)
        self.assertNotEqual(packages.jvpm_methods.S.peek(), 2)

    def test_iconst_3(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()
        a.iconst_3(op, con, arg)
        b = packages.jvpm_methods.S.peek()
        self.assertEqual(b, 3)
        packages.jvpm_methods.S.push(5)
        self.assertEqual(packages.jvpm_methods.S.peek(), 5)
        self.assertNotEqual(packages.jvpm_methods.S.peek(), 3)

    def test_iconst_4(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()
        a.iconst_4(op, con, arg)
        b = packages.jvpm_methods.S.peek()
        self.assertEqual(b, 4)
        packages.jvpm_methods.S.push(5)
        self.assertEqual(packages.jvpm_methods.S.peek(), 5)
        self.assertNotEqual(packages.jvpm_methods.S.peek(), 4)

    def test_iconst_5(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()
        a.iconst_5(op, con, arg)
        b = packages.jvpm_methods.S.peek()
        self.assertEqual(b, 5)
        packages.jvpm_methods.S.push(2)
        self.assertEqual(packages.jvpm_methods.S.peek(), 2)
        self.assertNotEqual(packages.jvpm_methods.S.peek(), 5)

    def test_idiv(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.S.push(4)
        packages.jvpm_methods.S.push(2)
        a.idiv(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 2.0)
        packages.jvpm_methods.S.push(6)
        packages.jvpm_methods.S.push(-2)
        a.idiv(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, -3)
        packages.jvpm_methods.S.push(-6)
        packages.jvpm_methods.S.push(-2)
        a.idiv(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 3)

    def test_iload_0(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.VARIABLES.append(7)
        packages.jvpm_methods.VARIABLES.append(5)
        packages.jvpm_methods.VARIABLES.append(6)
        packages.jvpm_methods.VARIABLES.append(1)
        packages.jvpm_methods.VARIABLES[0] = 2
        a.iload_0(op, con, arg)
        b = packages.jvpm_methods.S.peek()
        self.assertEqual(b, 2)

    def test_iload_1(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.VARIABLES.insert(0, 7)
        packages.jvpm_methods.VARIABLES.insert(1, 5)
#         a.VARIABLES.append(6)
#         a.VARIABLES.append(1)
#        a.VARIABLES[1] = 5
        a.iload_1(op, con, arg)
        b = packages.jvpm_methods.S.peek()
        self.assertEqual(b, 5)

    def test_iload_2(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.VARIABLES.append(7)
        packages.jvpm_methods.VARIABLES.append(5)
        packages.jvpm_methods.VARIABLES.append(6)
        packages.jvpm_methods.VARIABLES.append(1)
        del packages.jvpm_methods.VARIABLES[2]
        packages.jvpm_methods.VARIABLES[2] = 7
        a.iload_2(op, con, arg)
        b = packages.jvpm_methods.S.peek()
        self.assertEqual(b, 7)

    def test_iload_3(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.VARIABLES.append(7)
        packages.jvpm_methods.VARIABLES.append(5)
        packages.jvpm_methods.VARIABLES.append(6)
        packages.jvpm_methods.VARIABLES.append(1)
        packages.jvpm_methods.VARIABLES.append(10)
        del packages.jvpm_methods.VARIABLES[3]
        packages.jvpm_methods.VARIABLES[3] = 9
        a.iload_3(op, con, arg)
        b = packages.jvpm_methods.S.peek()
        self.assertEqual(b, 9)

    def test_imul(self):
        op = None
        con = None
        arg = None

        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.S.push(3)
        packages.jvpm_methods.S.push(4)
        a.imul(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 12)
        packages.jvpm_methods.S.push(-2)
        packages.jvpm_methods.S.push(3)
        a.imul(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, -6)
        packages.jvpm_methods.S.push(-5)
        packages.jvpm_methods.S.push(-4)
        a.imul(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 20)

    def test_ineg(self):
        op = None
        con = None
        arg = None

        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.S.push(3)
        a.ineg(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, -3)
        packages.jvpm_methods.S.push(-5)
        a.ineg(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 5)

    def test_ior(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.S.push(2)
        packages.jvpm_methods.S.push(5)
        a.ior(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 7)
        packages.jvpm_methods.S.push(8)
        packages.jvpm_methods.S.push(2)
        a.ior(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 10)
        packages.jvpm_methods.S.push(10)
        packages.jvpm_methods.S.push(-3)
        a.ior(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, -1)
        packages.jvpm_methods.S.push(-5)
        packages.jvpm_methods.S.push(-6)
        a.ior(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, -5)

    def test_irem(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()

        packages.jvpm_methods.S.push(5)
        packages.jvpm_methods.S.push(2)
        a.irem(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 1)

        packages.jvpm_methods.S.push(10)
        packages.jvpm_methods.S.push(5)
        a.irem(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 0)

        packages.jvpm_methods.S.push(-6)
        packages.jvpm_methods.S.push(5)
        a.irem(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 4)

        packages.jvpm_methods.S.push(6)
        packages.jvpm_methods.S.push(-6)
        a.irem(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 0)

    def test_ishl(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()

        packages.jvpm_methods.S.push(2)
        packages.jvpm_methods.S.push(1)
        a.ishl(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 4)

    def test_ishr(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()

        packages.jvpm_methods.S.push(3)
        packages.jvpm_methods.S.push(1)
        a.ishr(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 1)

        packages.jvpm_methods.S.push(-1)
        packages.jvpm_methods.S.push(1)
        a.ishr(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, -1)

        packages.jvpm_methods.S.push(5)
        packages.jvpm_methods.S.push(0)
        a.ishr(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 5)

        packages.jvpm_methods.S.push(0)
        packages.jvpm_methods.S.push(5)
        a.ishr(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 0)

    def test_istore_0(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.S.push(3)
        a.istore_0(op, con, arg)
        b = packages.jvpm_methods.VARIABLES[0]
        self.assertEqual(b, 3)

    def test_istore_1(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.S.push(2)
        packages.jvpm_methods.S.push(4)
        a.istore_0(op, con, arg)
        a.istore_1(op, con, arg)
        b = packages.jvpm_methods.VARIABLES[1]
        self.assertEqual(b, 2)

    def test_istore_2(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.S.push(8)
        packages.jvpm_methods.S.push(7)
        packages.jvpm_methods.S.push(9)
        a.istore_0(op, con, arg)
        a.istore_1(op, con, arg)
        a.istore_2(op, con, arg)
        b = packages.jvpm_methods.VARIABLES[2]
        self.assertEqual(b, 8)

    def test_istore_3(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.S.push(9)
        packages.jvpm_methods.S.push(10)
        packages.jvpm_methods.S.push(3)
        packages.jvpm_methods.S.push(4)
        a.istore_0(op, con, arg)
        a.istore_1(op, con, arg)
        a.istore_2(op, con, arg)
        a.istore_3(op, con, arg)
        b = packages.jvpm_methods.VARIABLES[3]
        self.assertEqual(b, 9)

    def test_isub(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()

        packages.jvpm_methods.S.push(5)
        packages.jvpm_methods.S.push(2)
        a.isub(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 3)

        packages.jvpm_methods.S.push(5)
        packages.jvpm_methods.S.push(5)
        a.isub(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 0)

        packages.jvpm_methods.S.push(5)
        packages.jvpm_methods.S.push(0)
        a.isub(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 5)

        packages.jvpm_methods.S.push(0)
        packages.jvpm_methods.S.push(0)
        a.isub(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 0)

    def test_iushr(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()

        packages.jvpm_methods.S.push(5)
        packages.jvpm_methods.S.push(2)
        a.iushr(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 1)
    """
        a.stack.push(-1)
        a.stack.push(2)
        a.iushr()
        b = a.stack.pop()
        self.assertEqual(b, 3)
    """

    def test_ixor(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()

        packages.jvpm_methods.S.push(5)
        packages.jvpm_methods.S.push(3)
        a.ixor(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 6)

    def test_i2f(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()

        packages.jvpm_methods.S.push(5)
        a.i2f(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 5.0)

        packages.jvpm_methods.S.push(0)
        a.i2f(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 0.0)

        packages.jvpm_methods.S.push(-1)
        a.i2f(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, -1.0)

    def test_i2b(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()

        packages.jvpm_methods.S.push(5)
        a.i2b(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, b'\x00\x00\x00\x00\x00\x00\x00\x05')

        packages.jvpm_methods.S.push(0)
        a.i2b(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, b'\x00\x00\x00\x00\x00\x00\x00\x00')

    def test_i2c(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()

        packages.jvpm_methods.S.push(5)
        a.i2c(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, '\x05')

        packages.jvpm_methods.S.push(0)
        a.i2c(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, '\x00')

    def test_i2s(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.S.push(5)
        a.i2d(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 5)

        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.S.push(0)
        a.i2d(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 0)

        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.S.push(-1)
        a.i2d(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, -1)

    def test_i2d(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.S.push(5)
        a.i2d(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 5)

        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.S.push(0)
        a.i2d(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 0)

        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.S.push(-1)
        a.i2d(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, -1)

    def test_i2l(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.S.push(5)
        a.i2l(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 5)

        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.S.push(0)
        a.i2l(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 0)

        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.S.push(-1)
        a.i2d(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, -1)
    
    def test_dup(self):
        op = None
        con = None
        arg = None
        a = packages.jvpm_methods.OpCodeMethods()

        packages.jvpm_methods.S.push(5)
        a.dup(op, con, arg)
        b = packages.jvpm_methods.S.pop()
        c = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 5)
        self.assertEqual(c, 5)

    def test_dict_search(self):
        op = None
        con = None
        a = packages.jvpm_methods.OpCodeMethods()
        l = packages.jvpm_opcodes.OpCodes(op, con)

        l.opcodes =['06', '3c', '04', '3d', '1b', '1c', '82', '3e'] # Testing some op codes
        packages.jvpm_methods.VARIABLES.append(0) # adding random constants to test methods \/
        packages.jvpm_methods.VARIABLES.append(1)
        packages.jvpm_methods.VARIABLES.append(2)
        packages.jvpm_methods.VARIABLES.append(3)
        packages.jvpm_methods.VARIABLES.append(4)
        packages.jvpm_methods.VARIABLES.append(5)

        sys.stdout = unittest.mock.Mock()

        # l.dict_search()
#         sys.stdout.assert_has_calls(

#             [call.write('iconst_3'), call.write('\n'),
#             call.write('ran iconst_3'), call.write('\n'),
#             call.write('istore_1'), call.write('\n'),
#             call.write('ran istore_1'), call.write('\n'),
#             call.write('iconst_1'), call.write('\n'),
#             call.write('ran iconst_1'), call.write('\n'),
#             call.write('istore_2'), call.write('\n'),
#             call.write('ran istore_2'), call.write('\n'),
#             call.write('iload_1'), call.write('\n'),
#             call.write('ran iload_1'), call.write('\n'),
#             call.write('iload_2'), call.write('\n'),
#             call.write('ran iload_2'), call.write('\n'),
#             call.write('ixor'), call.write('\n'),
#             call.write('ran ixor'), call.write('\n'),
#             call.write('istore_3'), call.write('\n'),
#             call.write('ran istore_3'), call.write('\n'), call.write('\n')]
#         )

class test_long(unittest.TestCase):
    def test_tag_long(self):
        sub_list = ["00", "00", "00", "00", "00", "00", "03", "ea"]
        long_result = packages.pool_translate.PoolTranslate.tag_long(self, sub_list)

        self.assertEqual(long_result, 1002)

    def test_tag_float(self):
        sub_list = ["44","a3","1a","38"]
        float_result = packages.pool_translate.PoolTranslate.tag_float(self, sub_list)
        self.assertEqual(float_result, 1304.8193359375)

class test_pool_opcodes(unittest.TestCase):

    def test_get_opcodes(self):
        jvpm_opcodes_obj = packages.jvpm_opcodes.HeaderClass(name="jvpm/javafiles/AddTwo.class")
        
        self.assertEqual(jvpm_opcodes_obj.get_magic(), "cafebabe")
        self.assertEqual(jvpm_opcodes_obj.get_minor(), "0000")
        self.assertEqual(jvpm_opcodes_obj.get_minor(), "0037")

        const_pool = jvpm_opcodes_obj.get_const_pool()
        translator = packages.pool_translate.PoolTranslate(const_pool, jvpm_opcodes_obj.skips_in_constant_pool, name="jvpm/javafiles/AddTwo.class")
        translated_pool = translator.translate_pool()
        a_f = ['00', '21']
        this = ['00', '08']
        super = ['00', '09']
        interface = ['00', '00']
        int_table = "interface table empty"
        f_c = ['00', '00']
        field_table = "field table empty"
        methods_count = ['00', '02']
        op_codes = ['2a', 'b7', '00', '01', 'b1', 'bb', '00', '02', '59', 'b2', '00', '03', 'b7', '00', '04', '4c', '2b', 'b6', '00', '05', '3d', '2b', 'b6', '00', '05', '3e', 'b2', '00', '06', '1c', '1d', '60', 'b6', '00', '07', 'b1']
        self.assertEqual(jvpm_opcodes_obj.get_access_flags(), a_f)
        self.assertEqual(jvpm_opcodes_obj.get_this_class(), this)
        self.assertEqual(jvpm_opcodes_obj.get_super_class(), super)
        self.assertEqual(jvpm_opcodes_obj.get_interfaces_count(), interface)
        self.assertEqual(jvpm_opcodes_obj.get_interface(), None)
        self.assertEqual(jvpm_opcodes_obj.get_field_count(), f_c)
        self.assertEqual(jvpm_opcodes_obj.get_field(), None)
        self.assertEqual(jvpm_opcodes_obj.get_methods_count(), methods_count)
        self.assertEqual(jvpm_opcodes_obj.get_methods(translated_pool), op_codes)


class TestAccessFlagTranslater(unittest.TestCase):
    def test_translate_access_flag(self):
        a = packages.access_flag_translater_dictionary.AccessFlagTranslater()
        
        self.assertEqual(a.translate_access_flag(1), "ACC_PUBLIC")
        self.assertEqual(a.translate_access_flag(2), "ACC_PRIVATE")
        self.assertEqual(a.translate_access_flag(4), "ACC_PROTECTED")
        self.assertEqual(a.translate_access_flag(8), "ACC_STATIC")
        self.assertEqual(a.translate_access_flag(10), "ACC_FINAL")
        self.assertEqual(a.translate_access_flag(20), "ACC_SUPER")
        self.assertEqual(a.translate_access_flag(200), "ACC_INTERFACE")
        self.assertEqual(a.translate_access_flag(400), "ACC_ABSTRACT")
        self.assertEqual(a.translate_access_flag(1000), "ACC_SYNTHETIC")
        self.assertEqual(a.translate_access_flag(2000), "ACC_ANNOTATION")
        self.assertEqual(a.translate_access_flag(4000), "ACC_ENUM")

