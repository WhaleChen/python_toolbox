# dict get()

a_dict = {'a':1,'b':'2','c':'3'}

# use .get() could handle the key missing case

key_list = ['a','b','c','d']

def value_generator_without_missing_data(key_list):
    for i in range(len(key_list)):
        # will make error
        # yield a_dict[key_list[i]]
        yield a_dict.get(key_list[i],'')

show_data = value_generator_without_missing_data(key_list)
for i in range(len(key_list)):
    print (next(show_data))
