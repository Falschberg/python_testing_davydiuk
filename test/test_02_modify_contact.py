# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test modify contact firstname"))
    old_contacts = app.contact.get_contacts_list()
    new_contact = Contact(firstname="New Firstname", lastname="New Lastname")
    new_contact.id = old_contacts[0].id
    app.contact.modify_first_contact(new_contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[0] = new_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    print(new_contact)


# def test_modify_contact_lastname(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="Test modify contact lastname"))
#     app.contact.modify_first_contact(Contact(lastname="New Lastname"))