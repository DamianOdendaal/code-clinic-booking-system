<<<<<<< HEAD
import re
import termcolor
from termcolor import colored


msg = termcolor.colored("[AVAILABLE]", "red")
string = f"something {msg} maybe"
ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
result = ansi_escape.sub('', string)
print(result)
=======
hey = {"a":1, "b":2, "c": 3}

print(len(hey))
>>>>>>> dd3e82cdd58f30a53ae7e67017dff44a75abb118
