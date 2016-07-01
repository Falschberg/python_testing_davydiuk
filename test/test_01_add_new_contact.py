# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    old_contacts = app.contact.get_contacts_list()
    new_contact = Contact(firstname="Firstname", middlename="Middlename" ,lastname="Lastname" , nickname="Nickname",
                          title="Title", company="Company", address="Address",
                          homephone="+11111", mobilephone="(22)222", workphone="3-33-33", faxphone="44444",
                          email="email@email.com", email2="email2@email.com", email3="email3@email.com", homepage="www.homepage.com",
                          address2="Address2", secondaryphone="5 55 55", notes="Notes")
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




