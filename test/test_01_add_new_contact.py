# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    old_contacts = app.contact.get_contacts_list()
    new_contact = Contact(firstname="Louis", lastname="Gaal")
    app.contact.create(new_contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_add_empty_contact(app):
#     old_contacts = app.contact.get_contacts_list()
#     new_contact = Contact(firstname="", lastname="")
#     app.contact.create(Contact())
#     new_contacts = app.contact.get_contacts_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(new_contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




