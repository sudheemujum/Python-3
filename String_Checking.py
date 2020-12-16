#Starting and ending part of the string

s='Learning Python is very Easy'

print(s.startswith('Learning'))
print(s.startswith('learning'))
print(s.endswith('Easy'))
print(s.endswith('easy'))

s=input('Enter any character:')

if s.isalnum():
    print('It is alphanumeric character')
    if s.isalpha():
        print('It is alphabet character')
        if s.islower():
            print('Characters are in lower case')
        else:
            print('Characters are in upper case')
    else:
        print('It is a digit')
elif s.isspace():
    print('It is space character')
else:
    print('It is non space special character')
        



