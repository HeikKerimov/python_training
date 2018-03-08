# -*- coding: utf-8 -*-
import pytest
from fixture.group_application import GroupApplication
from model.group import Group


@pytest.fixture
def app(request):
    fixture = GroupApplication()
    request.addfinalizer(fixture.close)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Group", header="Some text", footer="Some text"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
