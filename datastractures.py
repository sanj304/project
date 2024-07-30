list
names = ['john','smith','andrew']
tuple
names = ('john','smith','andrew')
set
names = ('john','smith','andrew')
dict

students = {'john': 100,'smith':300,'andrew':200}

# lists

employees = ['peter', 'john', 'smith', 'ruth', 'ester', 'annastacia' ]
print(employees)
print(employees[2])
print(employees[0])
print(employees[4])
print(employees[5])
print(employees[1:5])
print(employees[0:2])
employees[1] = 'Alex'
print(employees)
employees[3] = 'Moses'
print(employees)
employees.append('pauline')
print(employees)
employees.insert(0,'jack')
print(employees)
employees.extend(['kamau','mutua','wafula'])
print(employees)
marks = [200,321,324,455]
print(max(marks))
print(min(marks))
print(sum(marks))
# Tuple
languages = ('python','java','php','kotlin')
print(languages)
print(languages[1])
print(languages[3:6])
# sets
mysets = {1,2,3,4,5,6,7,8,9}
print(mysets)
number = 6
if number in mysets:
    output = number
    print(output)
majina = {'john','smith','ruth','esther'}
name = 'esther'
if name in majina:
    jina = name
    print(jina)

majina.add('charles')
print(majina)
majina.update(['njoroge','collins','peter'])
# dictionary
books = {
    'title': 'the code',
    'author': 'john doe',
    'year published':2000
}
print(books)
books['version'] = ('version one')
print(books)

if 'title' in books:
    print('yes it is in the dictation')
else:
    print('no it is not in the dictionary')
# dictionary
students = {
    'title': 'students',
    'name': 'john ken',
    'year admitted':2010,
    'school': 'mangohigh'

}