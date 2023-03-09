import pytest
from Ceejaytest.src.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:

    @pytest.mark.tcid12
    @pytest.mark.smoke
    def test_login_none_existing_user(self):
        print('*********')
        print('TEST LOGIN NOT EXISTING')
        print('*********')
        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        my_account.input_login_username('dffgggh')
        my_account.input_login_password('dffgggh')
        my_account.click_login_button()

        # # verify error message
        expected_err = 'Error: The username dffgggh is not registered on this site. If you are unsure of your username, try your email address instead'
        my_account.wait_until_error_is_displayed(expected_err)
