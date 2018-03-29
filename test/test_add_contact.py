# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import pytest


def random_string(prefix, max_len):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


def random_digits(prefix, max_len):
    return prefix + "".join([random.choice(string.digits) for i in range(random.randrange(max_len))])


test_data = [Contact(first_name=random_string("first", 5), last_name=random_string("last", 5),
                     home_phone=random_digits("8928", 7), work_phone=random_digits("8928", 7),
                      mobile_phone=random_digits("8928", 7), secondary_phone=random_digits("8928", 7),
                      address=random_string("address", 10), email_1=random_string("email_1", 4), email_2=random_string("email_2", 4))
             for i in range(2)]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_new_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


