import random

from model.contact import Contact
from model.group import Group


def test_add_some_contact_to_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Heik", last_name="Kerimov", home_phone="9214410883",
                                   work_phone="9214410883", mobile_phone="9214410883", secondary_phone="9214410883"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="Group", header="Some text", footer="Some text"))

    groups = orm.get_group_list()
    group = random.choice(groups)
    contacts = orm.get_contact_list()
    contact = random.choice(contacts)
    app.contact.add_contact_to_group_by_id(contact.id, group.id)
    assert contact in orm.get_contacts_in_group(group)
