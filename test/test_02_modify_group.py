# -*- coding: utf-8 -*-
from model.group import Group
import random

#first variant
def test_modify_group_name(app, db):
    if len(db.get_groups_list()) == 0:
        app.group.create(Group(name="TestName"))
    old_groups = db.get_groups_list()
    print("\nСтарый список групп из базы - ", old_groups)
    index = random.randrange(len(old_groups))
    group = Group(name="NewName")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = db.get_groups_list()
    print("\nНовый список групп из базы - ", new_groups)
    old_groups[index] = group
    print("\nСписок из броузера - ", app.group.get_groups_list())
    print("\nСтарый измененный список групп из базы - ", old_groups)
    assert old_groups == new_groups
    assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)

# second variant
# def test_modify_group_name(app, db):
#     if len(db.get_groups_list()) == 0:
#         app.group.create(Group(name="TestName"))
#     old_groups = db.get_groups_list()
#     print("\nСтарый список групп из базы - ", old_groups)
#     group = random.choice(old_groups)
#     new_group = Group(name="NewName", id=group.id)
#     app.group.modify_group_by_id(group.id, new_group)
#     new_groups = db.get_groups_list()
#     print("\nНовый список групп из базы - ", new_groups)
#     index = 0
#     for i in old_groups:
#         if i.id == group.id:
#             print("\n - ", i)
#             break
#         index =+ 1
#     old_groups[index] = new_group
#     ui_groups = app.group.get_groups_list()
#     print("\nСписок из броузера - ", ui_groups)
#     print("\nСтарый измененный список групп из базы - ", old_groups)
#     assert old_groups == new_groups
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# third variant
# def test_modify_group_name(app, db, ):
#     if len(db.get_groups_list()) == 0:
#         app.group.create(Group(name="TestName"))
#     old_groups = db.get_groups_list()
#     group = random.choice(old_groups)
#     new_group = Group(name="NewName")
#     app.group.modify_group_by_id(group.id, new_group)
#     assert len(old_groups) == app.group.count()
#     new_groups = db.get_groups_list()
#     assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)

# old variant
# def test_modify_group_name(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="TestName"))
#     old_groups = app.group.get_groups_list()
#     index = random.randrange(len(old_groups))
#     group = Group(name="NewName")
#     group.id = old_groups[index].id
#     app.group.modify_group_by_index(index, group)
#     assert len(old_groups) == app.group.count()
#     new_groups = app.group.get_groups_list()
#     old_groups[index] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
#
# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="NewHeader"))
#     old_groups = app.group.get_groups_list()
#     app.group.modify_first_group(Group(header="Header"))
#     new_groups = app.group.get_groups_list()
#     assert len(old_groups) == len(new_groups)
#
# def test_modify_group_footer(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="NewFooter"))
#     old_groups = app.group.get_groups_list()
#     app.group.modify_first_group(Group(footer="Footer"))
#     new_groups = app.group.get_groups_list()
#     assert len(old_groups) == len(new_groups)


