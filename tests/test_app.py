from api.app import hs_driver

def test_hs_driver():
    assert type(hs_driver()) is str
