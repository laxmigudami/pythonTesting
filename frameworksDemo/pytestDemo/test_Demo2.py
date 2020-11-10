import pytest
@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "hello"
    assert msg == "hi", "test failed because strings do not match"

def test_secondProgramCreditcard():

    a=4
    b=6
    assert a+2 == 6, "addition do not match"
