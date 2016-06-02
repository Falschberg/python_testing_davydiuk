# -*- coding: utf-8 -*-
from model.new_contact import New_contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.new_contact.edit_first_contact(New_contact(firstname="New Name", middlename="", lastname="", nickname="", title="", company="",
                                       address="", home="", mobile="", work="", fax="",
                                       email="", email2="", email3="", homepage="",
                                       byear="", ayear="", address2="", phone2="",
                                       notes="", bday="", bmonth="",
                                       aday="", amonth="",
                                       photo=""))
    app.session.logout()