# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

from group import Group


class test_add_group(unittest.TestCase):

    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_test_add_group(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.create_group(wd, Group(name="Group", header="Some text", footer="Some text"))
        self.logout(wd)

    def test_empty_add_group(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.create_group(wd, Group(name="", header="", footer=""))
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def create_group(self, wd, group):
        self.open_groups_page(wd)
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page(wd)

    def open_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, username, password):
        self.open_home_page(wd)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")


if __name__ == '__main__':
    unittest.main()
