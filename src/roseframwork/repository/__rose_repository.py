
class RoseRepository:
    """Rose Repository is an abstract base class that define in project

            This is particularly helpful when you want to create a repository.
            .

            ```python

            class MyRepository(RoseRepository):
                def __init__(self):
                    super().__init__(model=model, map_db=map_db)
            ```

            Args::
                model: The model class .
                map_db: Map db class that will be used as map db of the repository


    """
    __model = None
    __map_db = None

    def __init__(self, model, map_db):
        self.__model = model
        self.__map_db = map_db

    def save(self):
        self.__model.save()
