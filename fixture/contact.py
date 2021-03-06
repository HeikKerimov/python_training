import re

from model.contact import Contact


class ContactHelper:

    contact_cache = None

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_add_new_contact_page()
        self.fill_contact_form(contact)
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_to_edit_by_index(index)
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(0, contact)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def add_contact_to_group_by_id(self, contact_id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name("to_group").click()
        wd.find_element_by_xpath("//select[@name='to_group']//option[@value='%s']" % group_id).click()
        wd.find_element_by_name("add").click()
        wd.find_element_by_link_text('group page "name"').click()
        self.contact_cache = None

    def delete_contact_from_group_by_id(self, contact_id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("group").click()
        wd.find_element_by_xpath("//select[@name='group']//option[@value='%s']" % group_id).click()
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name("remove").click()
        wd.find_element_by_link_text('group page "name"').click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_phone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.secondary_phone)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email_1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email_2)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[id='%s']" % id).click()

    def select_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        elements = wd.find_elements_by_xpath("//img[@alt='Edit']")
        elements[index].click()

    def open_contact_view_page_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        elements = wd.find_elements_by_xpath("//img[@alt='Details']")
        elements[index].click()

    def open_add_new_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("theform")) > 0):
            wd.find_element_by_link_text("add new").click()

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                first_name = element.find_element_by_xpath("td[3]").text
                last_name = element.find_element_by_xpath("td[2]").text
                address = element.find_element_by_xpath("td[4]").text
                all_emails = element.find_element_by_xpath("td[5]").text
                all_phones = element.find_element_by_xpath("td[6]").text
                self.contact_cache.append(Contact(id=id, first_name=first_name, last_name=last_name, address=address,
                                                  all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def get_contacts_info_from_edit_page(self):
        wd = self.app.wd
        self.contact_cache = []
        for index, contact in enumerate(wd.find_elements_by_xpath("//img[@alt='Details']")):
            self.select_contact_to_edit_by_index(index)
            id = wd.find_element_by_name("id").get_attribute("value")
            first_name = wd.find_element_by_name("firstname").get_attribute("value")
            last_name = wd.find_element_by_name("lastname").get_attribute("value")
            home_phone = wd.find_element_by_name("home").get_attribute("value")
            work_phone = wd.find_element_by_name("work").get_attribute("value")
            mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
            secondary_phone = wd.find_element_by_name("phone2").get_attribute("value")
            address = wd.find_element_by_name("address").get_attribute("value")
            email_1 = wd.find_element_by_name("email").get_attribute("value")
            email_2 = wd.find_element_by_name("email2").get_attribute("value")
            email_3 = wd.find_element_by_name("email3").get_attribute("value")
            self.contact_cache.append(Contact(id=id, first_name=first_name, last_name=last_name,
                       home_phone=home_phone, work_phone=work_phone,
                       mobile_phone=mobile_phone, secondary_phone=secondary_phone, address=address,
                       email_1=email_1, email_2=email_2, email_3=email_3))
            self.app.open_home_page()
        return list(self.contact_cache)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_page_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        secondary_phone = re.search("P: (.*)", text).group(1)
        return Contact(id=id, home_phone=home_phone, work_phone=work_phone,
                       mobile_phone=mobile_phone, secondary_phone=secondary_phone)