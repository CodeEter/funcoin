import hashlib

input_bytes = b"BACKPACK"

output = hashlib.sha256(input_bytes)

print(output.hexdigest())

