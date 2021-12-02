
fh = open('data_files/hello.txt', 'a')

# print(fh.read())
# print(fh.readline())
# print(fh.readlines())
# print(fh.readable())
# print(fh.writable())
# data = ["\nSam like better thing", '\nHey! What\'s up with you']
# fh.writelines(data)
# help(fh)


def save_data(records, file_path):
    fh = open(file_path, 'w')

    fh.writelines(records)
    fh.close()
def contribute(text, location):
    fh = open(location, 'a')
    fh.write('\n' + text)
    fh.close()

def get_records(file_path):
    records = []
    try:
        fh = open(file_path, 'r')
        for line in fh.readlines():
            records.append(line.strip())
    except FileNotFoundError:
        print("File not found")

    return  records

def display_records(r):
    for name in r:
        print("{}".format(name))
students = [
    'Wisdom\n',
    'Sam\n',
    'Ade\n',
    'Ola\n'
]
location = 'data_files/studentsm.txt'
print(get_records(location))
# save_data(students, location)
# data = get_records(location)
# # display_records(data)
# contribute("Yet another content", location)
# display_records(get_records(location))
# print(data)

actions = [
    "create",
    "read"
]
for opt in actions:
    print(opt)
# selected_action = input("What do you want")
# if selected_action == 'read':
#     display_records(get_records(location))
# elif selected_action == 'create':
#     text = input("Enter your content ")
#     contribute(text, location)
#     print('Thank you')
# else:
#     print("Selection not found")