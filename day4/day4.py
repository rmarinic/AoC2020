import re

def byrCheck(st):
    num = int(''.join(filter(str.isdigit, st)))
    return 1920 <= num <= 2002
def iyrCheck(st):
    num = int(''.join(filter(str.isdigit, st)))
    return 2010 <= num <= 2020
def eyrCheck(st):
    num = int(''.join(filter(str.isdigit, st)))
    return 2020 <= num <= 2030
def hgtCheck(st):
    if 'cm' in st:
        num = int(st[st.find(':')+1:st.find('c')])
        return 150 <= num <= 193
    if 'in' in st:
        num = int(st[st.find(':')+1:st.find('i')])
        return 59 <= num <= 76
def hclCheck(s):
    if re.match("^[A-Fa-f0-9]*$", s[s.find("#")+1:len(s)]):
        return True
def eclCheck(s):
    fields = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    for f in fields:
        if f in s:
            return True
def pidCheck(st):
    if(len(st) == 13):
        num = st[4:13]
        flag = True
        for i in num:
            if not i.isdigit():
                flag = False
        return (len(str(num))) == 9 and flag


inp = [line.strip() for line in open("input.txt", "r")]
#inp = [line.strip() for line in open("test.txt", "r")]

nextPass = False
fields = ['hgt', 'ecl', 'pid', 'byr', 'eyr', 'iyr', 'hcl']
counter = 0
ans = 0
for line in inp:
    if nextPass:
        counter = 0
    new = line.split(" ")
    for field in new:

        if nextPass:
            counter = 0
        nextPass = False
        if 'byr' in field:
            if byrCheck(field):
                counter = counter + 1
        if 'iyr' in field:
            if iyrCheck(field):
                counter = counter + 1
        if 'eyr' in field:
            if eyrCheck(field):
                counter = counter + 1
        if 'hgt' in field:
            if hgtCheck(field):
                counter = counter + 1
        if 'hcl' in field:
            if hclCheck(field):
                counter = counter + 1
        if 'ecl' in field:
            if eclCheck(field):
                counter = counter + 1
        if 'pid' in field:
            if pidCheck(field):
                counter = counter + 1

        if counter == 7:
            counter = 0
            ans = ans + 1

        if field == '':
            nextPass = True


print(ans)
