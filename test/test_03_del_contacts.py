# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test delete first contact"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.delete_first_contact()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts


def test_delete_all_contacts(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test delete all contacts"))
    app.contact.delete_all_contacts()
    assert app.contact.count() == 0
