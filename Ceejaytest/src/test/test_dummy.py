import pytest
import pdb

@pytest.mark.usefixtures("init_driver")

class TestDummy():

    def test_dummy_func(self):
        print("I am dummy test line 1")
        print("I am dummy test line 2")
        self.driver.get("http://demostore.supersqa.com/")
        pdb.set_trace()
