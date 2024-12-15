file_name = 'input.txt'
#file_name = 'i2'

with open(file_name, 'r') as f:
    data = f.read()

# Is the last number a file or a free space ?
#is_file = True if len(data)%2 == 1  else False

# IT IS A FILE (both for i2 and input.txt)

# bunch of pointers
reading = 0
virtual_index = 0
file_id = 0
last_file = len(data) - 1
last_file_id = len(data)//2
print(last_file_id)
size_last_file = int(data[last_file])


to_handle = {}
for i in range(0,len(data),2):
    to_handle[i//2] = int(data[i])

print(to_handle)
checksum = 0

while reading <= last_file:
    print("--------------------------------")
    print("reading :", reading)
    print("last_file :", last_file)
    print("file_id :", file_id)
    print("last_file_id :", last_file_id)
    print("virtual_index :", virtual_index)
    print("checksum :", checksum)

    #Check if we are reading a block or a free_space
    if reading%2 == 0:
        # REDING A BLOCK
        size_of_block = int(data[reading])
        size_to_handle = to_handle[file_id]
        print(size_of_block, "block file of id :", file_id)
        print("size_to_handle :", size_to_handle)
        for _ in range(size_to_handle):
            print("adding : ",file_id, "*", virtual_index, end="=")
            print(file_id * virtual_index)
            checksum += file_id * virtual_index
            virtual_index += 1
            to_handle[file_id] -= 1
        print("incr file_id")
        file_id += 1
    else:
        # READING A FREE SPACE
        size_of_free_space = int(data[reading])
        print(size_of_free_space, "free space")
        
        # HANDELING THE LAST FILE MOVEMENT
        for i in range(size_of_free_space):
            print(" -> i = ", i)
            print("size_last_file = ", size_last_file)
            print("adding : ",last_file_id, "*", virtual_index, end=" = ")
            print(last_file_id * virtual_index)
            checksum += last_file_id * virtual_index
            size_last_file -= 1
            to_handle[last_file_id] -= 1
            virtual_index += 1
            if size_last_file == 0:
                print("ICI")
                last_file -= 2
                size_last_file = int(data[last_file])
                last_file_id -= 1
    reading += 1

print("checksum = ", checksum)
