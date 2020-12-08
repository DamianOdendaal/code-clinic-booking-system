import sys
import termcolor
import re 


msg_1 = termcolor.colored("[AVAILABLE]", attrs=["bold"])
msg = termcolor.colored("[AVAILABLE]", "red")
msg_3 = termcolor.colored("[AVAILABLE]", "green")

# print(ms
# expr = "\[A-Z]"
list_ = [msg, msg_1]
# print(msg_1)
# match = re.match(expr, msg)
ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
result = ansi_escape.sub('', msg)
result2 = ansi_escape.sub('', msg_1)
print(result)
print(result2)
print(list_)


###################################