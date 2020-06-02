import jsonschema
import pytest

import main

class TestMain:
    def test_pass(self):
        main.check(
            {
                'firstName': 'John',
                'lastName': 'Doe',
                'age': 28
            }
        )

    def test_fail(self):
        with pytest.raises(jsonschema.ValidationError):
            main.check(
                {
                    'firstName': 'John',
                    'lastName': 'Doe',
                    'age': 27
                }
            )
