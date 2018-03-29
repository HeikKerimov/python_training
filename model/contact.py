from sys import maxsize


class Contact:

    def __init__(self, id=None, first_name=None, last_name=None, home_phone=None, mobile_phone=None, work_phone=None, secondary_phone=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.home_phone = home_phone

    def __repr__(self):
        return "%s : %s %s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
