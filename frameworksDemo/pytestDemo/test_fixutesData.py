import pytest

from frameworksDemo.pytestDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("loadData")
class TestExample2(BaseClass):

    def test_editProfile2(self, loadData):
        log= self.test_getLogger()
        log.info(loadData[0])
        log.info(loadData[1])


