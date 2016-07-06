# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
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

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_numbers(maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(5, maxlen, 1))])


testdata = [Contact(firstname="", lastname="", address="")] + [
    Contact(firstname=random_string("first", 3), middlename=random_string("middle", 3), lastname=random_string("last", 3), nickname=random_string("nick", 3),
            title=random_string("title", 3), company=random_string("company", 3), address=random_string("address", 3),
            homephone=random_numbers(15), mobilephone=random_numbers(15), workphone=random_numbers(15), faxphone=random_numbers(15),
            email=random_string("email", 3), email2=random_string("email2", 3), email3=random_string("email3", 3), homepage=random_string("homepage", 3),
            address2=random_string("address2", 3), secondaryphone=random_numbers(15), notes=random_string("notes", 3))
    for i in range(2)
]

# testdata = [
#     Group(name=name, header=header, footer=footer)
#     for name in ["", random_string("name", 10)]
#     for header in ["", random_string("header", 20)]
#     for footer in ["", random_string("footer", 20)]
# ] - перебор всех возможных комбинаций из пустых и случайных значений


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
