import re
from random import randrange

from model.contact import Contact


def test_all_info_on_home_page(app, db):

    contact_from_home_page = db.get_contact_list()
    contact_from_edit_page = app.contact.get_contacts_info_from_edit_page()
    assert sorted(contact_from_home_page, key=Contact.id_or_max) == sorted(contact_from_edit_page, key=Contact.id_or_max)
