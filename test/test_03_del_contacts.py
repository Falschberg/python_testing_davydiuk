# -*- coding: utf-8 -*-

def test_delete_first_contact(app):
    app.new_contact.delete_first_contact()


def test_delete_all_contacts(app):
    app.new_contact.delete_all_contacts()
