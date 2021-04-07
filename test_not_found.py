try:
    contact_file = open("data/invalid-name.csv", encoding='latin_1', mode='w+')

    for line in contact_file:
        print(line, end='')

except FileNotFoundError:
    print('File not found')
except PermissionError:
    print('Writing permission denied')
finally:
    contact_file.close()