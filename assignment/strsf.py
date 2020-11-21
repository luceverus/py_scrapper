def get_from_dict(dic, key=""):
    if type(dic) != dict:
        print(f'You need to send a dictionary. You sent: {type(dic)}')
        return
    if key == "":
        print('You need to send a word to search for.')
        return
    if key not in dic:
        print(f'{key} was not found in this dict.')
        return
    print(f'{key}: {dic[key]}')


my_english_dict = {"kimchi": "good"}
print("\n\n###### get_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\nget_from_dict("hello", "kimchi"):')
get_from_dict("hello", "kimchi")

# Should not work. Word to search from is required.
print('\nget_from_dict(my_english_dict):')
get_from_dict(my_english_dict)

# Should not work. Word is not found.
print('\nget_from_dict(my_english_dict, "galbi"):')
get_from_dict(my_english_dict, "galbi")

# Should work and print the definiton of 'kimchi'
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")
