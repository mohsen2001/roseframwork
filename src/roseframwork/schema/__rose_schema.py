from pydantic_core.core_schema import ModelSchema


def __check_is_empty(list):
    if list is None:
        return False
    if len(list) > 0:
        return True
    return False



class RoseSchema(ModelSchema):

    @classmethod
    def update_config_model(cls, model, include: [], exclude: []):
        # Assuming 'model' is the attribute we want to dynamically update
        setattr(cls.Config, 'model', model)
        if __check_is_empty(include):
            setattr(cls.Config, 'include', include)
        if __check_is_empty(exclude):
            setattr(cls.Config, 'exclude', exclude)
