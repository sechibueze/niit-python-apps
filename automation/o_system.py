import os

# help(os)

# Get environmental vcaraiable
# print(os.getenv('PATH'))

# print(os.getcwd())
# print(os.listdir('.'))
# print(os.sep)
# print(os.walk('.'))

# for content in os.walk('.'):
#     print(content)

print(os.path.pathsep)
print(os.path.abspath('./utils'))
print(os.path.relpath('./utils'))
print(os.path.basename(os.getcwd()))

# print(os.path.join(os.getcwd(), 'db', 'connect.py'))
# config_dir = os.path.join(os.getcwd(), 'config')
# print(os.mkdir(config_dir))
# os.renames('config', 'config2')

# os.rmdir('config2')