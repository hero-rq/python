import string
from itertools import product
from passlib.hash import md5_crypt

text=string.ascii_lowercase+string.digits
password='G4HeulB'
salt='7xoI5SJz'
hash_value='WkHWfPAu7Fj7y6NoiOt7n/'
fail=1

for len in range(1,20) :
    checks=product(text,repeat=len)
    
    for t in checks :
        input=''.join(t)
        trying=password+input
        attack=md5_crypt.using(salt=salt).hash(trying)
        print("trying ... "+trying, " length : ",len)
        crypted_val=attack.split('$')[3]
    
        if crypted_val == hash_value :
            print("success! passwd is ",trying, "hash value is ",crypted_val)
            fail=0
            break
    
    if fail == 0 :
        break
