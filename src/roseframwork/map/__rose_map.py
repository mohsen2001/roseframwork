class RoseMap:
    __default_columns: []
    __schema = None

    def __init__(self, default_columns:[]):
        self.__validate_default_columns(default_columns)
        self.__default_columns = default_columns

    def __validate_default_columns(self,default_columns:[]):
        if default_columns is None:
            raise ValueError
        if len(default_columns)== 0:
            raise ValueError


    def get_default_columns_to_insert(self, exclude_fields: [], include_fields: [], schema):
        if include_fields is None:
            include_fields = self.__default_columns
        if len(include_fields) == 0:
            include_fields = self.__default_columns
        if exclude_fields is not None and len(exclude_fields)>0:
            entity_dict = schema.dict(
                include=dict(include_fields),  # Only these fields will be included
                exclude=dict(exclude_fields)  # 'description' field will be excluded even if it was included
            )
        else:
            entity_dict = schema.dict(
                include=dict(include_fields),  # Only these fields will be included
            )
        return entity_dict



    def get_default_columns_to_update(self, exclude_fields: [], include_fields: [], model):
        return self.__default_columns
