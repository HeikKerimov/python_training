# -*- coding: utf-8 -*-
import pytest
from fixture.contact_application import ContactApplication
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = ContactApplication()
    request.addfinalizer(fixture.close)
    return fixture


def test_add_new_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(first_name="Heik", last_name="Kerimov", phone="9214410883"))
    app.logout()

