class RoseRepository:
    __model = None
    __map_db = None

    def __init__(self, model, map_db):
        self.__model = model
        self.__map_db = map_db
