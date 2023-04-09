def division(num, div):
    if not (isinstance(num, int) and isinstance(div, int)):
        raise ValueError("division() must be called only with integer parameters")
    try:
        return num / div
    except:
        print(f'Unable to complete division of {num} by {div}')
        raise


def test_div(div):
    result = division(10, div)
    print(f'Division result of 10/{div} is {result}')


# try:
#     test_div(0.0)
# except AttributeError as E:
#     print(E)
# except ZeroDivisionError as E:
#     print(E)
# # general exception:
# except Exception as E:
#     print('generic exception')
#     print(E)

# print('end of script')

try:
    print('flow is here')
    raise ValueError
except Exception:
    print('now is here')

print('flow continues')