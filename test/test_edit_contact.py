# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_edit_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Heik", last_name="Kerimov", home_phone="9214410883",
                                   work_phone="9214410883", mobile_phone="9214410883", secondary_phone="9214410883",
                                   email_1="heik@mail.ru", email_2="heik2@mail.ru", email_3="heik3@mail.ru", address="spb"))

    contact = Contact(first_name="Edited", last_name="Edited", home_phone="811111", work_phone="811111",
                      mobile_phone="811111", secondary_phone="811111",
                      email_1="heik@mail.ru", email_2="heik2@mail.ru", email_3="heik3@mail.ru", address="msk")

    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)



