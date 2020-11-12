import os

PATH = os.getcwd()
result = [os.path.join(dp, f) for dp, dn, filenames in os.walk(PATH) for f in filenames if os.path.splitext(f)[0] == 'credentials']
print(result[0])