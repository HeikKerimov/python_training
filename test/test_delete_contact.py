# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Heik", last_name="Kerimov", phone="9214410883"))
    app.contact.delete_first_contact()

