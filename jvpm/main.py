import packages
import argparse


if '__main__' == __name__:                  #pragma: no cover


    ap = argparse.ArgumentParser(description='This is a Java Virtual Machine.')
    ap.add_argument("-f", "--file",
                    required=False,
                    help='Name of java class file with .class extension')
    args = vars(ap.parse_args())

    if args['file'] is None:
        file = input("Select file to run: ")
    else:
        file = args['file']

    if not '.class' in file:
        file += '.class'

    file_name = ("jvpm/javafiles/%s" % str(file))
    header_class_object = packages.jvpm_opcodes.HeaderClass(name=file_name)               #pragma: no cover
    print(header_class_object.get_magic())              #pragma: no cover
    print(header_class_object.get_minor())              #pragma: no cover
    print(header_class_object.get_major())              #pragma: no cover

    n = header_class_object.get_const_pool()
    print(n)
    p_translator = packages.pool_translate.PoolTranslate(n,
                                                         header_class_object.skips_in_constant_pool,
                                                         name=file_name)

    pool = p_translator.translate_pool()
    print(pool, "translated")

    a = header_class_object.get_access_flags()
    print(a, "   access flags")

    b = header_class_object.get_this_class()
    print(b, "   this class")

    c = header_class_object.get_super_class()
    print(c, "   super class")

    d = header_class_object.get_interfaces_count()
    print(d, "   interfaces count")

    # no method built yet but should just be index in constant pool
    header_class_object.get_interface()

    e = header_class_object.get_field_count()
    print(e, "   field count")

    # no method built yet but should just be variable table
    header_class_object.get_field()

    opcodes = header_class_object.get_methods_count()
    print(opcodes, " - methods count       \n ",
          header_class_object.integer_method_count,
          " -int meth count")

    opcodes = header_class_object.get_methods(pool)
    print("OpCodes:\n ", opcodes, "** op codes **")


    dict_search_object = packages.jvpm_opcodes.OpCodes(opcodes, pool)
    dict_search_object.dict_search()