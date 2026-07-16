import hashlib  # noqa: F401
a = ''
print(hashlib.sha256(a.encode()).hexdigest())
