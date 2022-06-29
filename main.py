from input import Dataframe
inp = Dataframe()
state = True
while state:
    request = input('Welcome admin\ntype "add student", "remove student" or "search student"\n')

    if request == 'add student':
        name = input('enter student name:')
        batch = input('enter batch:')
        phone = input('enter phone no.:')
        inp.add_student(name, batch, phone)


    if request == 'remove student':
        register = input('enter student register no:')
        inp.remove_register(register)


    if request == 'search student':
        search = input('enter student register no :')
        inp.search_student(search)

    if request == 'add csv':
        csv = input('enter file path :')
        inp.create_csv(csv)
        inp.create_register()
    if request == 'exit':
        state = False
        print('program ended')
    if request == 'refresh':
        inp.create_register()

