import hashlib, binascii

# try to get password
def get_password(dict, hashed, salt):
    for password in dict:  # look through all words in dict
        for algo in hashlib.algorithms_available:  # use all algos available
            if algo.startswith('shake_'): # shake requires variable size, ignore it.
                continue
            h = hashlib.new(algo)
            h.update(binascii.unhexlify(salt) + password.encode())  # decode salt from hex format and encode password
            if hashed == h.hexdigest(): # if hashed is same as hash calculated
                print(algo)
                return password  # return password


if __name__ == '__main__':
    file = open("dic-0294.txt", 'r')
    dict = []
    for line in file.readlines():  # populate list with words from file
        dict.append(line.strip("\n"))

    files = ["pw1.hex", "pw2.hex", "pw3.hex", "spw1.hex", "spw2.hex", "spw3.hex"] # files available
    salt = open("salt.hex").readline().strip("\n")  # read salt

    for file in files: # for each password file
        hashed = open(file).readline().strip("\n")
        if 's' == file[0]:  # if it starts with s, need salt to get password
            found = get_password(dict, hashed, salt)
        else: # else normal
            found = get_password(dict, hashed, '')

        if not found: # if not found give error message
            print("Could not find password for file ", file)
        else: # else print the password
            print("The password for file " ,file, " is ", found)