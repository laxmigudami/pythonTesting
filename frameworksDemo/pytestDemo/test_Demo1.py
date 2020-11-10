#any pytest file should start with the test_ or it should end with _test
# pytest method names should start with test
# any code should be wrapped in the method only
# method name should have sense its the name of test case
# -k stands for the method name execution, -s logs in the output, -v more info like metadata
# we can run the specific file like py.test <file name>
# to run group TC's we have to use commond called py.test -m smoke -v -s   here -m stands for mark followed by name of the grp
# smoke is the custom mark we need to register them. its not compulsory though
import pytest
from test
@pytest.mark.smoke
def test_firstProgram():
    print("hello dear selenium")
@pytest.mark.xfail     #we use this where there are some free requisites in the tcs and u dont waant to skip it
# it will run that test case bt it will nt show it in the output
def test_firstProgram1():
    print("good morning")

def test_crossBrowser(cross_browser):
    print(cross_browser[1])