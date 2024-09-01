from .__rose_repository import RoseRepository
from ..map import RoseMap


class CreateRepository(RoseRepository):
    """Rose Repository is a base class that define in project

                This is particularly helpful when you want to create a repository that insert records to specific model.
                .

                ```python

                class MyCreatRepository(CreateRepository):
                    def __init__(self):
                        super().__init__(model=model, map_db=map_db)
                ```

                Args::
                    model: The model class .
                    map_db: Map db class that will be used as map db of the repository


        """
    __schema = None
    def __init__(self, model, map_db,schema):
        super().__init__(model=model, map_db=map_db)
        self.__schema = schema

    def create(self, entity_schema, includes:[], excludes:[]):
        entity_dict = self.__map_db.get_default_columns_to_insert(excludes=excludes, include_fields=includes,
                                                               schema=entity_schema)
        inserted_model = self.__model.objects.create(entity_dict)
        self.save()
        entity_schema = self.__schema(**{**entity_schema.dict(), **self.__schema.from_orm(inserted_model).dict(
            include=dict(includes),  # Only include these fields
            exclude=dict(excludes)
        )})



