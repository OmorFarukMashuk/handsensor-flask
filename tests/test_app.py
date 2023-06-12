from app import hs_driver


def test_hs_driver():
    assert hs_driver() == "Hello World!"