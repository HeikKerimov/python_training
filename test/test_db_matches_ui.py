from model.group import Group


def test_group_list(app, db):
    def clean(group):
        return Group(id=group.id, name=group.name.strip())

    ui_list = app.group.get_group_list()
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)