from model.group import Group
import random
import string

constant = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]


def random_string(prefix, max_len):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


test_data = [Group(name="", header="", footer="")] + [
            Group(name=random_string("name", 6), header=random_string("header", 6), footer=random_string("footer", 6))
            for i in range(1)
    ]
