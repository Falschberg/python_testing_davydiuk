# -*- coding: utf-8 -*-
from model.group import Group
from model.contact import Contact
from fixture.orm import ORMFixture
import random


orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_del_contact_in_group(app, db):
    if len(db.get_groups_with_contacts()) == 0:
        if len(db.get_groups_list()) == 0:
            app.group.create(Group(name="Test Group"))
            app.contact.open_home_page()
        old_groups = db.get_groups_list()
        group = random.choice(old_groups)
        if len(db.get_contacts_list()) == 0:
            app.contact.create(Contact(firstname="Test", lastname="Contact"))
        old_contacts = db.get_contacts_list()
        contact = random.choice(old_contacts)
        app.contact.add_contact_in_group_by_id(contact.id, group.name)
    groups_with_contacts = db.get_groups_with_contacts()
    print('\n\ngroups_with_contacts - ', groups_with_contacts)
    group_with_contact = random.choice(groups_with_contacts)
    print('\ngroup_with_contact - ', group_with_contact)
    id = group_with_contact.id
    print('\nid - ', id)
    group_with_name = orm.get_group_by_id(id)
    print('\ngroup_with_name - ', group_with_name)
    group_name = group_with_name.name
    #group_name = 'name2'
    contacts_in_group = orm.get_contacts_in_group(group_with_contact)
    print('\ncontacts_in_group - ', contacts_in_group)
    contact_in_group = random.choice(contacts_in_group)
    print('\ncontact_in_group - ', contact_in_group)
    old_contacts_in_group = orm.get_contacts_in_group(group_with_name)
    old_contacts_out_group = orm.get_contacts_not_in_group(group_with_name)
    app.contact.del_group_in_contact(contact_in_group.id, group_name)
    new_contacts_in_group = orm.get_contacts_in_group(group_with_name)
    new_contacts_out_group = orm.get_contacts_not_in_group(group_with_name)
    old_contacts_in_group.remove(contact_in_group)
    old_contacts_out_group.append(contact_in_group)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)
    assert sorted(old_contacts_out_group, key=Contact.id_or_max) == sorted(new_contacts_out_group, key=Contact.id_or_max)