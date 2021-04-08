import csv, pickle, json
from contact import Contact

def csv_to_contacts(path, encoding='latin_1'):
    contacts = []

    with open(path, encoding=encoding) as file:
        # reads cvs and parse columns
        reader = csv.reader(file)

        for line in reader:
            # id = line[0]
            # name = line[1]
            # email = line[2]
            # this unpack line and assings in order
            id, name, email = line

            contacts.append(Contact(id, name, email))

    return contacts


def contacts_to_pickle(contacts, path):
    with open(path, mode='wb') as file:
        pickle.dump(contacts, file)


def pickle_to_contacts(path):
    with open(path, mode='rb') as file:
        return pickle.load(file)


def contacts_to_json(contacts, path):
    with open(path, mode='w') as file:
        json.dump(contacts, file, default=_contact_to_json)


def _contact_to_json(contact):
    return contact.__dict__


def json_to_contact(path):
    contacts = []

    with open(path) as file:
        contacts_json = json.load(file)

        for contact in contacts_json:
            # contacts.append(Contact(contact['id'], contact['name'], contact['email']))
            # this unpack dictionary contact and assings each valeu to variable with key name
            contacts.append(Contact(**contact))

    return contacts