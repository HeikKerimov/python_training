# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    app.contact.create(Contact(first_name="Heik", last_name="Kerimov", phone="9214410883"))


