# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group", header="Some text", footer="Some text"))
    app.group.edit_first_group(Group(name="Edited_group", header="Edited_text", footer="Edited_text"))
