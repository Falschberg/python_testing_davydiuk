# -*- coding: utf-8 -*-
import pytest
from fixture.supplement import Supplement
from model.new_contact import New_contact


@pytest.fixture
def app(request):
    fixture = Supplement()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(New_contact(firstname="Louis", middlename="van", lastname="Gaal", nickname="King Louis", title="Coach", company="Manchester United Football Club",
                                            address="Old Trafford", home="+44 (0) 161 868 8000", mobile="+44 (0) 161 868 8000", work="+44 (0) 161 868 8000", fax="+44 (0) 161 868 8000",
                                            email="membership@manutd.co.uk", email2="tickets@manutd.co.uk", email3="disability@manutd.co.uk", homepage="http://www.manutd.com/",
                                            byear="1951", ayear="2026", address2="Sir Matt Busby Way, Manchester, M16 0RA", phone2="+44 (0) 161 868 8000",
                                            notes="Aloysius Paulus Maria van Gaal", bday="//div[@id='content']/form/select[1]//option[10]", bmonth="//div[@id='content']/form/select[2]//option[9]",
                                            aday="//div[@id='content']/form/select[3]//option[10]", amonth="//div[@id='content']/form/select[4]//option[9]",
                                            photo="C:\\Users\\FalschBerg\\Desktop\\Louis_van_Gaal_2013.jpg"))
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_empty_contact()
    app.logout()

