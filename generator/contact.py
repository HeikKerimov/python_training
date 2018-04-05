from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, max_len):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


def random_digits(prefix, max_len):
    return prefix + "".join([random.choice(string.digits) for i in range(random.randrange(max_len))])


test_data = [Contact(first_name=random_string("first", 5), last_name=random_string("last", 5),
                     home_phone=random_digits("8928", 7), work_phone=random_digits("8928", 7),
                      mobile_phone=random_digits("8928", 7), secondary_phone=random_digits("8928", 7),
                      address=random_string("address", 10), email_1=random_string("email_1", 4), email_2=random_string("email_2", 4),
                     email_3=random_string("email_3", 4))
             for i in range(2)]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))