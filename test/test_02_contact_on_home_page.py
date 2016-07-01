# -*- coding: utf-8 -*-
from model.contact import Contact
import re
from random import randrange


def test_contacts_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Firstname", middlename="Middlename" ,lastname="Lastname" , nickname="Nickname",
                                   title="Title", company="Company", address="Address",
                                   homephone="+11111", mobilephone="(22)222", workphone="3-33-33", faxphone="44444",
                                   email="email@email.com", email2="email2@email.com", email3="email3@email.com", homepage="www.homepage.com",
                                   address2="Address2", secondaryphone="5 55 55", notes="Notes"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    print(len(old_contacts))
    print(index)
    contact_from_home_page = app.contact.get_contacts_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                    filter(lambda x: x is not None,
                                           [contact.email, contact.email2, contact.email3])))


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                map(lambda x: clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))