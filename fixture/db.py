import pymysql.cursors

from model.contact import Contact
from model.group import Group


class DbFixture():

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit(True)

    def get_group_list(self):
        groups = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list")
            for row in cursor:
                (id, name, header, footer) = row
                groups.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return groups

    def get_contact_list(self):
        contacts = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, firstname, lastname, home, work, mobile, phone2, address, email, email2, email3 FROM addressbook")
            for row in cursor:
                (id, firstname, lastname, home, work, mobile, phone2, address, email, email2, email3) = row
                contacts.append(Contact(id=str(id), first_name=firstname, last_name=lastname, home_phone=home, work_phone=work,
                                        mobile_phone=mobile, secondary_phone=phone2, address=address,
                                        email_1=email, email_2=email2, email_3=email3))
        finally:
            cursor.close()
        return contacts

    def close(self):
        self.connection.close()
