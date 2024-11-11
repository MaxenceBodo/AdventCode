import hashlib

input = "iwrupvqb"
hash =""
i=0

while True :
    hash = f"{input}{i}"
    hash_result = hashlib.md5(hash.encode()).hexdigest()
    if hash_result.startswith("000000") :
        break
    i+=1

print(hash)

