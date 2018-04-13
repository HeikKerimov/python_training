import random

from model.contact import Contact
from model.group import Group


def test_delete_some_contact_from_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="Group", header="Some text", footer="Some text"))

    groups = orm.get_group_list()
    group = random.choice(groups)

    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Heik", last_name="Kerimov", home_phone="9214410883",
                                   work_phone="9214410883", mobile_phone="9214410883", secondary_phone="9214410883"))
    contacts = orm.get_contact_list()
    contact = random.choice(contacts)

    if len(orm.get_contacts_in_group(group)) == 0:
        app.contact.add_contact_to_group_by_id(contact.id, group.id)

    app.contact.delete_contact_from_group_by_id(contact.id, group.id)
    assert contact not in orm.get_contacts_in_group(group)
