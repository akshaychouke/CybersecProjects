# !usr/bin/python



import hashlib

from secrets import choice

from termcolor import colored



#welcome

print(colored("-"*100,'yellow'))

print(colored("\t\t\t\t Welcome to Hash Generator \t\t\t\t\t",'red'))

print(colored("-"*100,'yellow'))





#To take text input from user

print(colored("[*] Enter text to be hashed","blue"))

hashval = str(input())



#To select the hash type

print(colored("[*] Enter the hash algorithm you want to use ",'blue'))

print(colored("1. MD5\n2. SHA1\n3. SHA224\n4. SHA256\n5. SHA512\n6. All\n7. Exit",'green'))

hash_choice = int(input())





if hash_choice == 1:

    md5obj = hashlib.md5()

    md5obj.update(hashval.encode())

    print(colored("Your hash is: "+ md5obj.hexdigest(),'yellow'))



elif hash_choice == 2:

    sha1obj = hashlib.sha1()

    sha1obj.update(hashval.encode())

    print(colored("Your hash is: "+ sha1obj.hexdigest(),'yellow'))



elif hash_choice == 3:

    sha224obj = hashlib.sha224()

    sha224obj.update(hashval.encode())

    print(colored("Your hash is: "+ sha224obj.hexdigest(),'yellow'))



elif hash_choice == 4:

    sha256obj = hashlib.sha256()

    sha256obj.update(hashval.encode())

    print(colored("Your hash is: "+ sha256obj.hexdigest(),'green'))



elif hash_choice == 5:

    sha512obj = hashlib.sha512()

    sha512obj.update(hashval.encode())

    print(colored("Your hash is: "+ sha512obj.hexdigest(),'yellow'))



elif hash_choice == 6:

    md5obj = hashlib.md5()

    md5obj.update(hashval.encode())

    print(colored("MD5 is: "+ md5obj.hexdigest(),'yellow'))

    sha1obj = hashlib.sha1() 

    sha1obj.update(hashval.encode())

    print(colored("SH1 is: "+ sha1obj.hexdigest(),'yellow'))

    sha224obj = hashlib.sha224()

    sha224obj.update(hashval.encode())

    print(colored("SHA224 is: "+ sha224obj.hexdigest(),'yellow'))

    sha256obj = hashlib.sha256()

    sha256obj.update(hashval.encode())

    print(colored("SHA256 is: "+ sha256obj.hexdigest(),'yellow'))

    sha512obj = hashlib.sha512()

    sha512obj.update(hashval.encode())

    print(colored("SHA512 is: "+ sha512obj.hexdigest(),'yellow'))

elif hash_choice == 7:

    exit()

else:

    print(colored("Please Enter from the above mentioned Options!"))