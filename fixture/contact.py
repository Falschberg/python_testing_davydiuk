# -*- coding: utf-8 -*-
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init new contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submite new contact creation
        wd.find_element_by_name("submit").click()
        self.open_home_page()
        self.contacts_cache = None

    def change_field_value(self, field_firstname, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_firstname).click()
            wd.find_element_by_name(field_firstname).clear()
            wd.find_element_by_name(field_firstname).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        # self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        # self.change_field_value("nickname", contact.nickname)
        # self.change_field_value("title", contact.title)
        # self.change_field_value("company", contact.company)
        # self.change_field_value("address", contact.address)
        # self.change_field_value("home", contact.home)
        # self.change_field_value("mobile", contact.mobile)
        # self.change_field_value("work", contact.work)
        # self.change_field_value("fax", contact.fax)
        # self.change_field_value("email", contact.email)
        # self.change_field_value("email2", contact.email2)
        # self.change_field_value("email3", contact.email3)
        # self.change_field_value("homepage", contact.homepage)
        # self.change_field_value("address2", contact.address2)
        # self.change_field_value("phone2", contact.phone2)
        # self.change_field_value("notes", contact.notes)

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        # modify first contact
        wd.find_elements_by_css_selector("img[alt=\"Edit\"]")[index].click()
        self.fill_contact_form(new_contact_data)
        # submite contact modification
        wd.find_element_by_name("update").click()
        self.open_home_page()
        self.contacts_cache = None

    def delete_first_contact(self, index):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # select first contact
        wd.find_elements_by_name("selected[]")[index].click()
        self.submite_deletion()
        self.open_home_page()
        self.contacts_cache = None

    def delete_all_contacts(self):
        wd = self.app.wd
        # select all contacts
        wd.find_element_by_id("MassCB").click()
        self.submite_deletion()
        self.open_home_page()
        self.contacts_cache = None

    def submite_deletion(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_id("MassCB")) > 0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    contacts_cache = None

    def get_contacts_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contacts_cache = []
            for element in wd.find_elements_by_name("entry"):
                text_firstname = element.find_element_by_xpath("td[3]").text
                text_lastname = element.find_element_by_xpath("td[2]").text
                id = element.find_element_by_name("selected[]").get_attribute("id")
                self.contacts_cache.append(Contact(firstname=text_firstname, lastname=text_lastname, id=id))
        return list(self.contacts_cache)