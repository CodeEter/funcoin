import hashlib

input_bytes = b"backpack"

output = hashlib.sha256(input_bytes)

print(output.hexdigest())
