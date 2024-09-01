
from roseframwork.schema import RoseSchema


class TestMyModelSchema(RoseSchema):
    id:int
    field1 = str
    field2 = str

