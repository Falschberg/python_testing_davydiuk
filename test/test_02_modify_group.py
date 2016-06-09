# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test New Name"))
    app.group.modify_first_group(Group(name="New Name"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test New Header"))
    app.group.modify_first_group(Group(header="New Header"))


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test New Footer"))
    app.group.modify_first_group(Group(footer="New Footer"))
