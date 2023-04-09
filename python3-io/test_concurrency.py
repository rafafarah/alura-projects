carol = '11,Carol,carol@carol.com.br\n'
ana = '12,Ana,ana@ana.com.br\n'

def concurrent_write():
    contact_file1 = open("data/contacts_iso8859-1-write.csv", encoding='latin_1', mode='w')
    contact_file2 = open("data/contacts_iso8859-1-write.csv", encoding='latin_1', mode='w')

    # second write will overwrite file content
    contact_file1.write(carol)
    contact_file2.write(ana)

    contact_file1.close()
    contact_file2.close()

def concurrent_write_using_with_as():
    # manage context of use of file
    with open("data/contacts_iso8859-1-write.csv", encoding='latin_1', mode='w') as contact_file1:
        contact_file1.write(carol)

    with open("data/contacts_iso8859-1-write.csv", encoding='latin_1', mode='a') as contact_file2:
        contact_file2.write(ana)


concurrent_write_using_with_as()