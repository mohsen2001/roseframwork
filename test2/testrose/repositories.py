from roseframwork import repository


class TestMyModelRepository(repository.CreateRepository):
    def __init__(self, model, map_db, schema):
        super().__init__(model=model, map_db=map_db,schema=schema)
        