from hillcipher import decryptionKey

test = [[11, 8], [3, 7]]

new = decryptionKey(test)

if new == None:
    print("Fails")
else:
    print(new)
