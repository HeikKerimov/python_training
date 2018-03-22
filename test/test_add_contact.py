# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    contact = Contact(first_name="Heik", last_name="Kerimov", phone="9214410883")
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


