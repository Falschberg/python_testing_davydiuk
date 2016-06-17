# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="TestName"))
    old_groups = app.group.get_groups_list()
    group = Group(name="NewName")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="NewHeader"))
#     old_groups = app.group.get_groups_list()
#     app.group.modify_first_group(Group(header="Header"))
#     new_groups = app.group.get_groups_list()
#     assert len(old_groups) == len(new_groups)
#
#
# def test_modify_group_footer(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="NewFooter"))
#     old_groups = app.group.get_groups_list()
#     app.group.modify_first_group(Group(footer="Footer"))
#     new_groups = app.group.get_groups_list()
#     assert len(old_groups) == len(new_groups)


