from .__rose_repository import RoseRepository
from ..map import RoseMap


class CreateRepository(RoseRepository):

#https://testdriven.io/blog/django-and-pydantic/
    def __init__(self, model, map_db):
        super().__init__(model=model, map_db=map_db)

    def create(self, entity_schema, columns_to_insert):
        self.entity_schema.config
        inserted_model = self.__model.objects.create(entity_schema)
        entity_schema = inserted_model.from_django(inserted_model)

