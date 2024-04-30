import pytest
from pages.create_account import CreateAccount
from pages.eco_friendly import EcoFriendly
from pages.sale import Sale


@pytest.fixture(scope='session')
def start_end():
    print('\nStart testing')
    yield
    print('\nTesting completed')


@pytest.fixture()
def create_account(page):
    return CreateAccount(page)


@pytest.fixture()
def create_new_account(create_account):
    create_account.open_page()
    data = create_account.fill_all_form()
    return data


@pytest.fixture()
def eco_friendly(page):
    return EcoFriendly(page)


@pytest.fixture()
def sale_page(page):
    return Sale(page)
