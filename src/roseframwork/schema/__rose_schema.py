from pydantic_core.core_schema import ModelSchema



class RoseSchema(ModelSchema):
    class Config:
        orm_mode = True
        extra = "allow"


