import os
import sys
import time
import stat

## os.walk()
# if len(sys.argv) == 1:
#     root = '.'
# else:
#     root = sys.argv[1]
# for dir_name, sub_dirs, files in os.walk(root):
#     print(dir_name)
#     # Make the subdirectory names stand out with /
#     contents = sorted(files+sub_dirs)
#     # Show the contents
#     for c in contents:
#         print('  {}'.format(os.path.join(dir_name, c)))

## os.scandir()
# print(os.listdir("."))
# for entry in os.scandir("."):
#     typ = "unknown"
#     print(type(entry))
#     if entry.is_dir():
#         typ = "dir"
#     elif entry.is_file():
#         typ = "file"
#     elif entry.is_symlink():
#         typ = "link"
#     print('{} {}'.format(entry.name, typ))

if len(sys.argv) == 1:
    filename = __file__
else:
    filename = sys.argv[1]

stat_info = os.stat(filename)

print('os.stat({}):'.format(filename))
print('  Size:', stat_info.st_size)
print('  Permissions:', oct(stat_info.st_mode))
print('  Owner:', stat_info.st_uid)
print('  Device:', stat_info.st_dev)
print('  Created      :', time.ctime(stat_info.st_ctime))
print('  Last modified:', time.ctime(stat_info.st_mtime))
print('  Last accessed:', time.ctime(stat_info.st_atime))
