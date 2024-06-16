def reverse(inputpath, outputpath):
  if not (is_str(inputpath) and is_str(outputpath)):
    print('Please specify the strings for the first and second arguments')
    exit(1)
  contents = ''
  with open(inputpath) as f:
    contents = f.read()
  with open(outputpath, 'w') as f:
    reveresed = contents[::-1]
    f.write(reveresed)

def copy(inputpath, outputpath):
  if not (is_str(inputpath) and is_str(outputpath)):
    print('Please specify the strings for the first and second arguments')
    exit(1)
  contents = ''
  with open(inputpath) as f:
    contents = f.read()
  with open(outputpath, 'w') as f:
    f.write(contents)
    
def duplicate_contents(inputpath, n):
  if not (is_str(inputpath) and is_int(n)):
    print('Please enter a string for the first argument and a number for the second argument')
    exit(1)
  contents = ''
  with open(inputpath) as f:
    contents = f.read()
  with open(inputpath, 'w') as f:
    for i in range(0, n - 1):
      f.write(contents + contents)


def replace_string(inputpath, needle, newstring):
  if not (is_str(inputpath) and is_str(needle) and is_str(newstring)):
    print('Please specify the strings for the first and second and third arguments')
    exit(1)
  contents = ''
  with open(inputpath) as f:
    contents = f.read()
  with open(inputpath, 'w') as f:
    contents = contents.replace(needle, newstring)  
    print(contents)
    f.write(contents)
    
    
def is_str(string):
  return type(string) is str

def is_int(integer):
  return type(integer) is int