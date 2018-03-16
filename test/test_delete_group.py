# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group", header="Some text", footer="Some text"))
    app.group.delete_first_group()
