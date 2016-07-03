# -*- coding: utf-8 -*-
from model.contact import Contact
import re

def test_phones_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Firstname", middlename="Middlename", lastname="Lastname", nickname="Nickname",
                    title="Title", company="Company", address="Address",
                    homephone="+11111", mobilephone="(22)222", workphone="3-33-33", faxphone="44444",
                    email="email@email.com", email2="email2@email.com", email3="email3@email.com",
                    homepage="www.homepage.com",
                    address2="Address2", secondaryphone="5 55 55", notes="Notes"))
    contact_from_home_page = app.contact.get_contacts_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


# def test_phones_on_contact_view_page(app):
#     if app.contact.count() == 0:
#         app.contact.create(
#             Contact(firstname="Firstname", middlename="Middlename", lastname="Lastname", nickname="Nickname",
#                     title="Title", company="Company", address="Address",
#                     homephone="+11111", mobilephone="(22)222", workphone="3-33-33", faxphone="44444",
#                     email="email@email.com", email2="email2@email.com", email3="email3@email.com",
#                     homepage="www.homepage.com",
#                     address2="Address2", secondaryphone="5 55 55", notes="Notes"))
#     contact_from_view_page = app.contact.get_contacts_from_view_page(0)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_view_page.homephone == contact_from_edit_page.homephone
#     assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
#     assert contact_from_view_page.workphone == contact_from_edit_page.workphone
#     assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                map(lambda x: clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))