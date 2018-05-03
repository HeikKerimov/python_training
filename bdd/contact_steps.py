import random

from pytest_bdd import given, when, then

from model.contact import Contact


@given("A contact list")
def contact_list(db):
    return db.get_contact_list()


@given("A contact with <first_name>, <last_name>, <home_phone>, <work_phone>, <mobile_phone>, <secondary_phone>, <email_1>, <email_2>, <email_3>, <address>")
def new_contact(first_name, last_name, address, home_phone, work_phone, mobile_phone, secondary_phone, email_1, email_2, email_3):
    return Contact(first_name=first_name, last_name=last_name, home_phone=home_phone, work_phone=work_phone,
                                        mobile_phone=mobile_phone, secondary_phone=secondary_phone, address=address,
                                        email_1=email_1, email_2=email_2, email_3=email_3)


@when("I add the contact to the list")
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@then("New contact list is equal to the old list with the added contact")
def verify_contact_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@given("A non-empty contact list")
def non_empty_contact_list(app, db):
    if db.get_contact_list() == 0:
        app.contact.create(Contact(first_name="Heik", last_name="Kerimov", home_phone="9214410883",
                                   work_phone="9214410883", mobile_phone="9214410883", secondary_phone="9214410883", email_1="asdasd",
                                   email_2="asdasd", email_3="asas"))
    return db.get_contact_list()


@given("A random contact from the list")
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when("I delete the contact from the list")
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)


@then("The new list is equal to the old list without the deleted contact")
def verify_contact_deleted(app, db, non_empty_contact_list, random_contact, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


@given("A contact to edit")
def contact_to_edit():
    return Contact(first_name="Edited", last_name="Edited", home_phone="811111", work_phone="811111",
                      mobile_phone="811111", secondary_phone="811111",
                      email_1="heik@mail.ru", email_2="heik2@mail.ru", email_3="heik3@mail.ru", address="msk")


@given("A random index")
def random_index(non_empty_contact_list):
    return random.randrange(len(non_empty_contact_list))

@when("I edit the contact from the list")
def edit_contact(app, contact_to_edit,random_index, non_empty_contact_list):
    index = random_index
    contact_to_edit.id = non_empty_contact_list[index].id
    app.contact.edit_contact_by_index(index, contact_to_edit)


@then("The new list is equal to the old list with edited contact")
def verify_contact_edited(db, non_empty_contact_list, random_index, contact_to_edit):
    new_contacts = db.get_contact_list()
    assert len(non_empty_contact_list) == len(new_contacts)
    non_empty_contact_list[random_index] = contact_to_edit
    assert sorted(non_empty_contact_list, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)