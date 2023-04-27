import hashlib
import sys

h = hashlib.new("SHA256")
passw = sys.argv[1:]

# print(passw)
h.update(passw[0].encode())
hashed_pass = h.hexdigest()
print(hashed_pass)

# print(sys.argv, len(sys.argv))
# print(sys.argv[1], len(sys.argv[1]))