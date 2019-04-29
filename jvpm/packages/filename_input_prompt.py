class FileNameInputPrompt:
    def input_prompt():
        name = str(input("What file do you want to run: "))
        extension = ".class"
        directory = "jvpm/javafiles/"
        new_name = directory + name + extension

        return new_name
