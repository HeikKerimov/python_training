# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.edit_first_contact(Contact(first_name="Edited", last_name="Edited", phone="0000000000"))

