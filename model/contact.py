from sys import maxsize


class Contact:

    def __init__(self, id=None, first_name=None, last_name=None, home_phone=None, work_phone=None,
                 mobile_phone=None, secondary_phone=None, address=None,
                 email_1=None, email_2=None,
                 all_emails_from_home_page=None, all_phones_from_home_page=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.home_phone = home_phone
        self.work_phone = work_phone
        self.mobile_phone = mobile_phone
        self.secondary_phone = secondary_phone
        self.address = address
        self.email_1 = email_1
        self.email_2 = email_2
        self.all_emails_from_home_page = all_emails_from_home_page
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s : %s %s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
