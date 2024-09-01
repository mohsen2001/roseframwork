from testrose.mapdbs import TestMyModelMapDB


def create_test_my_model_map():
    return TestMyModelMapDB(
        default_columns=['id', 'field1','field2']
    )