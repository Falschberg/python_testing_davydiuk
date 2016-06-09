# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    app.contact.create(Contact(firstname="Louis",
                               middlename="van",
                               lastname="Gaal",
                               nickname = "King Louis",
                               title = "Coach",
                               company = "Manchester United Football Club",
                               address = "Old Trafford",
                               home = "+44 (0) 161 868 8000",
                               mobile = "+44 (0) 161 868 8000",
                               work = "+44 (0) 161 868 8000",
                               fax = "+44 (0) 161 868 8000",
                               email = "membership@manutd.co.uk",
                               email2 = "tickets@manutd.co.uk",
                               email3 = "disability@manutd.co.uk",
                               homepage = "http://www.manutd.com/",
                               address2 = "Sir Matt Busby Way, Manchester, M16 0RA",
                               phone2 = "+44 (0) 161 868 8000",
                               notes = "Aloysius Paulus Maria van Gaal"))


def test_add_empty_contact(app):
    app.contact.create(Contact())



