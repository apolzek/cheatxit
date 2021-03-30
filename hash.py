import hashlib

text = 'apolzek'

m = hashlib.md5()
m.update(text.encode())
print(m.hexdigest())