# when we think that perticular fixture is shared by the multiple files that time we need to define that fixture in
# conftest file request is an instance which belongs to the fixture. its like an object, we use request instance only
# when we have some fixtures with some values that we are passing. usally we will not pass a single value in real
# time. we pass the grp of values.

import pytest


@pytest.fixture(scope="class")
def setup():
    print("i will be executed first")
    yield
    print("i will execute last")


@pytest.fixture()
def loadData():
    print("user profile data is being created")
    return ["rahul", "shetty", "rahulshettyacademy.com"]


@pytest.fixture(params=[("chrome", "rahul", "shetty"), ("firefox", "laxmi"), ("IE", "smruti")])
def cross_browser(request):
    return request.param
