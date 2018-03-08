# -*- coding: utf-8 -*-
import pytest
from contact_application import ContactApplication
from contact import Contact


@pytest.fixture
def app(request):
    fixture = ContactApplication()
    request.addfinalizer(fixture.close)
    return fixture


def test_add_new_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Heik", lastname="Kerimov", phone="9214410883"))
    app.logout()

