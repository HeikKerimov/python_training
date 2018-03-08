# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.close)
    return fixture


def test_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="Heik", last_name="Kerimov", phone="9214410883"))
    app.session.logout()

