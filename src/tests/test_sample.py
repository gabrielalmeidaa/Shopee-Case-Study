import mongoengine

from settings import TEST_DATABASE_NAME, DATABASE_HOST, DATABASE_PORT

mongoengine.connect('TEST_DATABASE_NAME', host=DATABASE_HOST, port=DATABASE_PORT)


def func(x):
    return x + 1


def test_answer():
    import pdb;
    pdb.set_trace()
    assert func(2) == 3
