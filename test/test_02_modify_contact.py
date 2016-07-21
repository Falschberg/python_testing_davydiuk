# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_modify_some_contact1(app, db, check_ui):
    old_contacts = db.get_contacts_list()
    if len(old_contacts) == 0:
        app.contact.create(Contact(firstname="Test modify contact firstname"))
    contact = random.choice(old_contacts)
    new_contact = Contact(id=contact.id, firstname="New Firstname", lastname="New Lastname")
    app.contact.modify_contact_by_id(contact.id, new_contact)
    new_contacts = db.get_contacts_list()
    old_contacts.remove(contact)
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)



# def test_modify_contact_lastname(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="Test modify contact lastname"))
#     app.contact.modify_first_contact(Contact(lastname="New Lastname"))