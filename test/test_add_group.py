# -*- coding: utf-8 -*-
import allure
import pytest

from model.group import Group


def test_add_group(app, db, check_ui, json_groups):
    group = json_groups
    with allure.step("Given A group list"):
        old_groups = db.get_group_list()
    with allure.step("When I add a group %s to the list" % group):
        app.group.create(group)
    with allure.step("Then New group list is equal to the old list with the added group"):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


