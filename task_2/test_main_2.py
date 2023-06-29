import pytest
from main_task_2 import main

@pytest.mark.parametrize('status_code_',[
            201,
            401,
            409
            ])

def test_main_task_2(status_code_):
    res = main().status_code
    assert res == status_code_

