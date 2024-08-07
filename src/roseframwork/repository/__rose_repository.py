from src.roseframwork.map import RoseMap


class RoseRepository:
    """Rose Repository is base repositories that define in project

        This is particularly helpful when you want to create repository of models.
        .

        ```python
        from typing import List

        from typing_extensions import Annotated

        from pydantic import BaseModel, PlainSerializer

        CustomStr = Annotated[
            List, PlainSerializer(lambda x: ' '.join(x), return_type=str)
        ]

        class StudentModel(BaseModel):
            courses: CustomStr

        student = StudentModel(courses=['Math', 'Chemistry', 'English'])
        print(student.model_dump())
        #> {'courses': 'Math Chemistry English'}
        ```

        Attributes:
            func: The serializer function.
            return_type: The return type for the function. If omitted it will be inferred from the type annotation.
            when_used: Determines when this serializer should be used. Accepts a string with values `'always'`,
                `'unless-none'`, `'json'`, and `'json-unless-none'`. Defaults to 'always'.
        """
    __model = None
    __map_db: RoseMap = None

    def __init__(self, model, map_db: RoseMap):
        """Plain serializers use a function to modify the output of serialization.

            This is particularly helpful when you want to customize the serialization for annotated types.
            Consider an input of `list`, which will be serialized into a space-delimited string.

            ```python
            from typing import List

            from typing_extensions import Annotated

            from pydantic import BaseModel, PlainSerializer

            CustomStr = Annotated[
                List, PlainSerializer(lambda x: ' '.join(x), return_type=str)
            ]

            class StudentModel(BaseModel):
                courses: CustomStr

            student = StudentModel(courses=['Math', 'Chemistry', 'English'])
            print(student.model_dump())
            #> {'courses': 'Math Chemistry English'}
            ```

            Attributes:
                func: The serializer function.
                return_type: The return type for the function. If omitted it will be inferred from the type annotation.
                when_used: Determines when this serializer should be used. Accepts a string with values `'always'`,
                    `'unless-none'`, `'json'`, and `'json-unless-none'`. Defaults to 'always'.
            """
        self.__model = model
        self.__map_db = map_db
