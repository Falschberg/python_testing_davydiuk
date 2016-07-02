# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*100
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_numbers(maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(1, maxlen, 1))])

testdata = [Contact(firstname="", lastname="", address="")] + [
    Contact(firstname=random_string("first", 3), middlename=random_string("middle", 3), lastname=random_string("last", 3), nickname=random_string("nick", 3),
            title=random_string("title", 3), company=random_string("company", 3), address=random_string("address", 3),
            homephone=random_numbers(5), mobilephone=random_numbers(5), workphone=random_numbers(5), faxphone=random_numbers(5),
            email=random_string("email", 3), email2=random_string("email2", 3), email3=random_string("email3", 3), homepage=random_string("homepage", 3),
            address2=random_string("address2", 3), secondaryphone=random_numbers(5), notes=random_string("notes", 3))
    for i in range(3)
]

@pytest.mark.parametrize("new_contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new_contact(app, new_contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(new_contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




