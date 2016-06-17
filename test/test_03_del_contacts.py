# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test delete first contact"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts


def test_delete_all_contacts(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test delete all contacts"))
    app.contact.delete_all_contacts()
    assert app.contact.count() == 0
