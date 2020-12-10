import re
import termcolor
from termcolor import colored


msg = termcolor.colored("[AVAILABLE]", "red")
string = f"something {msg} maybe"
ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
result = ansi_escape.sub('', string)
print(result)