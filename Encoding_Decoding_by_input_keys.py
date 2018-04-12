# Implementing the task
# Encoding - decoding by input keys
key1 = input()  # Key to encode
key2 = input()  # Key to decode
message1 = input()  # message to encode
message2 = input()  # message to decode
encoded = ''
decoded = ''

for i in range(len(message1)):  # Encoding
    e = key1.find(message1[i])
    encoded += key2[e]
    
for i in range(len(message2)):  # Decoding
    d = key2.find(message2[i])
    decoded += key1[d]

# Showing the results
print(encoded)
print(decoded)
