# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_delete_some_contact(app, db):
    if len(db.get_contacts_list()) == 0:
        app.contact.create(Contact(firstname="Test delete first contact"))
    old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contacts_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts


# def test_delete_all_contacts(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="Test delete all contacts"))
#     app.contact.delete_all_contacts()
#     assert app.contact.count() == 0
