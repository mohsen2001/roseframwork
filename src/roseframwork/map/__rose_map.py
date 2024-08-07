class RoseMap:
    __default_columns: []
    __schema = None

    def __init__(self, default_columns):
        self.__default_columns = default_columns


    def get_default_columns_to_insert(self, exclude_fields: [], include_fields: [], model, schema):
        return self.__default_columns

    def get_default_columns_to_update(self, exclude_fields: [], include_fields: [], model):
        return self.__default_columns
