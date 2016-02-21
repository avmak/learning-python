# Module "mymod" is fully imported
import mymod

print(mymod.countLines('mymod.py'))
print(mymod.countChars('mymod.py'))
print(mymod.test('mymod.py'))

# Functions are imported from the module
from mymod import countLines, countChars, test

print(countLines('mymod.py'))
print(countChars('mymod.py'))
print(test('mymod.py'))
