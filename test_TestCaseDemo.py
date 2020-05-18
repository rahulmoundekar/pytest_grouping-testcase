import pytest


@pytest.fixture()
def setUp():
    print("First your want to navigate login page")
    yield
    print("once after close all resources")


@pytest.mark.login
def test_login_by_gmail(setUp):
    print('Login using gmail account')


@pytest.mark.login
def test_login_by_official_mail(setUp):
    print('Login using official mail id')


@pytest.mark.signup
def test_signup_by_gmail(setUp):
    print('signup using gmail account')


@pytest.mark.signup
def test_signup_by_official_mail(setUp):
    print('signup using official account')
