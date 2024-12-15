file_name = 'input.txt'
#file_name = 'i2'

with open(file_name, 'r') as f:
    data = f.read()

virtual_index = 0

where_are_files = {}
to_handle = []
free_space = {}

for i, c in enumerate(data):
    if i%2 == 0: # and c != '0':
        to_handle.append(int(c))
        where_are_files[i//2] = virtual_index
        virtual_index += int(c)
    else:
        if c == '0':
            continue
        free_space[virtual_index] = (int(c))
        virtual_index += int(c)


to_handle = list(reversed(to_handle))

#print("to_handle: ", to_handle)
#print("free_space: ", free_space)
#print("where are files", where_are_files)

last_file_id = len(data)//2

for index, size_to_fit in enumerate(to_handle):
    index_file =  last_file_id - index
    #print("index_file :", index_file)
    #print("size_to_fit :", size_to_fit)
    for index_space, space in free_space.items():
        #print("index_space :", index_space, " space :", space)
        if index_space < where_are_files[index_file]:
            if size_to_fit <= space:
                #print("We fit", index_file, " at", index_space)
                where_are_files[index_file] = index_space
                del free_space[index_space]
                space -= size_to_fit
                if space > 0:
                    free_space[index_space+size_to_fit] = space
                #print("new free_space: ", free_space)
                free_space = dict(sorted(free_space.items()))
                #print("sorted : ", free_space)
                break


checksum = 0

#print(where_are_files)
to_handle = list(reversed(to_handle))
for id, index in where_are_files.items():
    #print("id", id, " index", index)
    size = to_handle[id]
    #print("size :", size)
    for i in range(size):
        #print("We add :", id, "*", (index + i), " = ", id * (index + i))
        checksum += id * (index + i)

print("checksum :", checksum)