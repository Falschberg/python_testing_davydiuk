# -*- coding: utf-8 -*-
from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None,
                 title=None, company=None, address=None,
                 homephone=None, mobilephone=None, workphone= None, faxphone=None,
                 email=None, email2=None, email3=None, homepage=None,
                 address2=None, secondaryphone=None, notes=None,
                 id=None, all_emails_from_home_page=None, all_phones_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.faxphone = faxphone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address2 = address2
        self.secondaryphone = secondaryphone
        self.notes = notes
        self.id = id
        self.all_emails_from_home_page = all_emails_from_home_page
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.middlename, self.lastname, self.nickname, self.title,
                                   self.company, self.address, self.homephone, self.mobilephone, self.workphone, self.faxphone, self.email, self.email2,
                                   self.email3, self.homepage, self.address2, self.secondaryphone, self.notes, self.all_emails_from_home_page, self.all_phones_from_home_page)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname and self.address == other.address and self.all_phones_from_home_page == other.all_phones_from_home_page and self.all_emails_from_home_page == other.all_emails_from_home_page

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize


