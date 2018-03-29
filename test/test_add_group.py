# -*- coding: utf-8 -*-
from model.group import Group
import random
import string
import pytest


def random_string(prefix, max_len):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


test_data = [Group(name="", header="", footer="")] + [
            Group(name=random_string("name", 6), header=random_string("header", 6), footer=random_string("footer", 6))
            for i in range(1)
    ]


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


