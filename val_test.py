import re
#This is a file to test the regex validation of the validate row in the csvalchemy file
def validate(email):
    reg_refs = {}
    keys = ["Office Email"]
    row = [email]
    reg_refs['Office Email'] = re.compile(r'[\w]*@[\w]*\.{1}(com|gov|edu|io|net){1}$')
    is_good = True
    for i,key in enumerate(keys):
        form_good = reg_refs[key].search(row[i])
        if not form_good:
            #ERROR and display message
            print('Not valid boy', row[i])
        is_good = is_good and form_good
    return is_good

assert validate('kode.creer@gmail.com'), 'Email thinks this is false man' 
assert not validate('kode.koy koy')
assert not validate('CS2450 dog in .edu town')
assert not validate('@kode.com@dog')