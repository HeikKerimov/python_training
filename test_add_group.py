# -*- coding: utf-8 -*-
import pytest
from group_application import GroupApplication
from group import Group


@pytest.fixture
def app(request):
    fixture = GroupApplication()
    request.addfinalizer(fixture.close)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="Group", header="Some text", footer="Some text"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
