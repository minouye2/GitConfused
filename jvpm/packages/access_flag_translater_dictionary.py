class AccessFlagTranslater:
    def translate_access_flag(self, access_flag_value):
        access_flag = {
            1 : "ACC_PUBLIC",
            2 : "ACC_PRIVATE",
            4 : "ACC_PROTECTED",
            8 : "ACC_STATIC",
            10 : "ACC_FINAL",
            20 : "ACC_SUPER",
            200 : "ACC_INTERFACE",
            400 : "ACC_ABSTRACT",
            1000 : "ACC_SYNTHETIC",
            2000 : "ACC_ANNOTATION",
            4000 : "ACC_ENUM"
        }
        return access_flag[access_flag_value]
