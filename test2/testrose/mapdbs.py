from roseframwork import map


class TestMyModelMapDB(map.RoseMap):
    def __init__(self, default_columns:[]):
        super().__init__(default_columns=default_columns)
