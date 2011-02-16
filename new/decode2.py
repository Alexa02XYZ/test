# # cu input si output
# import hashlib
# import itertools
#
#
# def encrypt_string(hash_string):
#     sha_signature = \
#         hashlib.sha256(hash_string.encode()).hexdigest()
#     return sha_signature
#
#
# g = open("output", "rb")
# ls = "M p q w e r t y u i o a s d f g h j k l z x c v b n m Q W E R T Y U I O P A S D F G H J K L Z X C V B N 1 2 3 4 5 6 7 8 9 0".rsplit(' ')
# k = 0
# ls2 = []
# ls3 = []
# parola = ""
# text = ""
#
# sir_intrare = g.read(1)
# while k < 15:
#     parola = ""
#     text = ""
#     for i in range(len(ls)):
#         for j in range(len(ls)):
#             if i < j and ord(sir_intrare) == ord(ls[i]) ^ ord(ls[j]):
#                 parola += ls[i]
#                 parola += ' '
#                 text += ls[j]
#                 text += ' '
#     ls3.append(text.split())
#     ls2.append(parola.split())
#     sir_intrare = g.read(1)
#     k += 1
#
# ls = []
# for k in range(len(ls2)):
#     parola = ''
#     for i in range(len(ls2[k])):
#         parola += ls2[k][i]
#         parola += ' '
#         parola += ls3[k][i]
#         parola += ' '
#     ls.append(parola.split())
# parola = ' '
#
# i = 10
# while i < 16:
#     permutations = list(itertools.permutations(ls[k]))
#     if encrypt_string(parola) == '3f1a2bcaca2f02a8cd826b57caa7fa8a3214da1856aedb1a2c24ef29c3ea3771':
#         print(parola)
#     if encrypt_string(text) == '3f1a2bcaca2f02a8cd826b57caa7fa8a3214da1856aedb1a2c24ef29c3ea3771':
#         print(text)
#     i += 1
#
#
# g.close()
import sys
import math


def check_character(ch):
    if ch in all_characters:
        return True
    return False


if len(sys.argv) != 2:
    print("Incorrect arguments")
    sys.exit()

input_name = sys.argv[1]


with open(input_name, 'rb') as input_file:
    text = input_file.read()
text = text.decode('utf8')

pos_dict = {}

for i in range(len(text)):
    if text[i] in pos_dict:
        pos_dict[text[i]].append(i)
    else:
        pos_dict[text[i]] = [i]

len_key = 0
for ch in pos_dict:
    sz = 0
    for i in range(1, len(pos_dict[ch])):
        diff = pos_dict[ch][i] - pos_dict[ch][i - 1]
        sz = math.gcd(sz, diff)

    if 10 <= sz <= 15:
        len_key = sz

# print(len_key)
possible_keys = ["" for i in range(len_key)]
allowed_characters = ""
for i in range(26):
    allowed_characters += chr(i + ord('a'))
    allowed_characters += chr(i + ord('A'))
for i in range(10):
    allowed_characters += chr(i + ord('0'))
all_characters = allowed_characters
all_characters += "\'\" ,.?!;:-_+=()[]\n"

# print(text)
for start in range(len_key):
    block = ""
    for i in range(start, len(text), len_key):
        block += text[i]
    # print(block, end="\n\n\n\n\n")
    for ch_key in allowed_characters:
        good = True
        for j in range(len(block)):
            possible_ch = chr(ord(ch_key) ^ ord(block[j]))
            # print(ch_key, end=" ")
            # print(block[j], end=" ")
            # print(possible_ch, end=" ")

            if check_character(possible_ch) == False:
                good = False
                break
        # print(good, end="\n")
        if good == True:
            possible_keys[start] += ch_key
# print(possible_keys)
answer = ''.join(possible_keys)
print(answer)