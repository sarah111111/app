import pytest


def test_cart1(login):
    print("购物车用例1")


def test_cart2(login):
    print("购物车用例2")


@pytest.mark.parametrize('login', [
    ('username', 'password'),
    ('username1', 'password1')
], indirect=True)
def test_cart3(login):
    print("购物车用例3")
