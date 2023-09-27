import hashlib

hash = hashlib.new("SHA256")
myHashString = str(input("Enter what you would like to hash: "))
hash.update(myHashString.encode())

hashedString = hash.hexdigest()

print(hashedString)