# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app, db, json_contacts):
    contact = json_contacts
    old_contacts = db.get_contacts_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = db.get_contacts_list()
    old_contacts.append(contact)
    print("\nold_contacts - ",old_contacts)
    print("\nnew_contacts - ", new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




