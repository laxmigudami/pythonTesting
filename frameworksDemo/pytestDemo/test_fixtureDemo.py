# fixtures are used for the setup and tear down methods
# conftest is used to generalize and make it available to all the files
import pytest

@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixtureDemo(self):
        print("test case1 is being executed")

    def test_fixtureDemo2(self):
        print("test case2 is being executed")

    def test_fixtureDemo3(self):
        print("test case3 is being executed")

    def test_fixtureDemo4(self):
        print("test case4 is being executed")