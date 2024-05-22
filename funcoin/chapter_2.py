import hashlib

input_bytes = b"backpack"

output = haslib.sha256(input_bytes)

print(output.hexdigest())
