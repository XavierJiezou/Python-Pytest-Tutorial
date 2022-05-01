import pytest
import time


def test_1():
    time.sleep(3)
    assert 1 == 1


def test_2():
    time.sleep(3)
    assert 2 == 2


@pytest.mark.run(order=1)
def test_3():
    assert 3 == 4


if __name__ == '__main__':
    pytest.main(['-v', '-n', str(3), '--reruns', str(3), '-k', 'test_'])
