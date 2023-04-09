def read_from_file_buffer():
    contact_file = open("data/contacts_iso8859-1.csv", encoding='latin_1')

    print(type(contact_file.buffer))

    file_content = contact_file.buffer.read()
    byte_text = bytes('This é a byte text', 'latin_1')

    print(byte_text)

    contact_file.close()


def write_to_file_buffer():
    contact_file = open("data/contacts_iso8859-1-write.csv", encoding='latin_1', mode='w')

    print(type(contact_file.buffer))

    byte_text = bytes('This é a byte text', 'latin_1')
    contact = bytes('14,Verônica,verônica@verônica.com.br\n', 'latin_1')

    contact_file.buffer.write(contact)

    contact_file.close()


write_to_file_buffer()