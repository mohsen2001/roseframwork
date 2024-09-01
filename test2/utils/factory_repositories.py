from testrose import repositories as testrose_repositories
from . import factory_maps as maps
from testrose import schemas as testrose_schemas
from testrose.models import TestMyModel


def create_test_my_model_repository():
    return testrose_repositories.TestMyModelRepository(
        model=TestMyModel,
        map_db=maps.create_test_my_model_map(),
        schema=testrose_schemas.TestMyModelSchema
    )