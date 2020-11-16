import os


# print(os.getcwd())
# print(os.path.abspath('.'))
def find_credentials(filename, search_path):
    """
    Looks for 'credentials.json'.
    Walking top-down from the root.
    """

    result = []

    for root, dirs, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
   
    search_path = os.getcwd()
    print(result[0])
    return result[0]
    find_credentials(filename, search_path)

# result = find_credentials("credentials.json", search_path)
# print(result)
