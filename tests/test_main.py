import jsonschema
import pytest

import main

class TestMain:
    def test_pass(self):
        main.handler(
            {
                'firstName': 'John',
                'lastName': 'Doe',
                'age': 21
            },
            None
        )

    def test_fail(self):
        with pytest.raises(jsonschema.ValidationError):
            main.handler(
                {
                    'firstName': 'John',
                    'lastName': 'Doe',
                    'age': -1
                },
                None
            )
