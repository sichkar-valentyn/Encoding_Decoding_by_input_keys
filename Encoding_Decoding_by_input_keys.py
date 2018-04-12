# File: Encoding_Decoding_by_input_keys.py
# Description: Encoding and Decoding messages by input keys
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Encoding and Decoding messages by input keys // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Encoding_Decoding_by_input_keys (date of access: XX.XX.XXXX)

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
