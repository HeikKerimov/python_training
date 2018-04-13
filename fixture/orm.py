from datetime import datetime

from pony.orm import *
from pymysql.converters import encoders, decoders, convert_mysql_timestamp
from model.group import Group
from model.contact import Contact


class ORMFixture:

    db = Database()

    def __init__(self, host, name, user, password):
        conv = encoders
        conv.update(decoders)
        conv[datetime] = convert_mysql_timestamp
        self.db.bind("mysql", host=host, database=name, user=user, password=password, conv=conv)
        self.db.generate_mapping()

    class ORMGroup(db.Entity):
        _table_ = "group_list"
        id = PrimaryKey(int, column="group_id")
        name = Optional(str, column="group_name")
        header = Optional(str, column="group_header")
        footer = Optional(str, column="group_footer")
        contacts = Set(lambda: ORMFixture.ORMContact, table="address_in_groups", column="id", reverse="groups", lazy=True)

    class ORMContact(db.Entity):
        _table_ = "addressbook"
        id = PrimaryKey(int, column="id")
        first_name = Optional(str, column="firstname")
        last_name = Optional(str, column="lastname")
        home_phone = Optional(str, column="home")
        work_phone = Optional(str, column="work")
        mobile_phone = Optional(str, column="mobile")
        secondary_phone = Optional(str, column="phone2")
        address = Optional(str, column="address")
        email_1 = Optional(str, column="email")
        email_2 = Optional(str, column="email2")
        email_3 = Optional(str, column="email3")
        deprecated = Optional(datetime, column="deprecated")
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id", reverse="contacts", lazy=True)

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), first_name=contact.first_name, last_name=contact.last_name, home_phone=contact.home_phone,
                           work_phone=contact.work_phone, mobile_phone=contact.mobile_phone, secondary_phone=contact.secondary_phone,
                           address=contact.address, email_1=contact.email_1, email_2=contact.email_2, email_3=contact.email_3)
        return list(map(convert, contacts))