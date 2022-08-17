import time
from pytest import mark


# pip install pytest-xdist
# use "-n 4" flag to set the amount of threads
@mark.data
@mark.parametrize('a', [1, 2, 3, 4])
def test_multiple_threads(a):
    time.sleep(2)
    print(f'Test {a} complete')
