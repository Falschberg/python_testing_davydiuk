# -*- coding: utf-8 -*-
from model.group import Group
from model.contact import Contact
from fixture.orm import ORMFixture
import random

#orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

# def test_add_contact_in_group(app, db):
#     if len(db.get_groups_list()) == 0:
#         app.group.create(Group(name="Test Group"))
#         app.contact.open_home_page()
#     old_groups = db.get_groups_list()
#     group = random.choice(old_groups)
#     if len(orm.get_contacts_not_in_group(group)) == 0:
#         app.contact.create(Contact(firstname="Test", lastname="Contact"))
#     old_contacts = orm.get_contacts_not_in_group(group)
#     contact = random.choice(old_contacts)
#     old_contacts_in_group = orm.get_contacts_in_group(group)
#     print('\n', group)
#     print('\n', contact)
#     print('\n', old_contacts_in_group)
#     app.contact.add_contact_in_group_by_id(contact.id, group.name)
#     new_contacts_in_group = orm.get_contacts_in_group(group)
#     print('\n', new_contacts_in_group)
#     old_contacts_in_group.append(contact)
#     print('\n', old_contacts_in_group)
#     assert sorted(old_contacts_in_group, key=Group.id_or_max) == sorted(new_contacts_in_group, key=Group.id_or_max)

def test_del_contact_in_group(app, db):
    groups_with_contacts = db.get_groups_with_contacts()
    # group = random.choice(groups_with_contacts)
    # contacts_in_group = orm.get_contacts_in_group(group)
    print('\n', groups_with_contacts)
    # print('\n', group)
    # print('\n', contacts_in_group)

