from .__rose_repository import RoseRepository


class CreateRepository(RoseRepository):

    def __init__(self, model, map_db):
        super().__init__(model=model, map_db=map_db)

    def create(self, entity, columns_to_insert):
        self.__
