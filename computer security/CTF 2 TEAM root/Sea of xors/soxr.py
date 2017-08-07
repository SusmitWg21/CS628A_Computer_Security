# # a = "cs628a{bcaaaaffa44dv"

# a = "cs628a{bcaaaaffa44d"
# # a= "cs628a{bcaaaaffa44d0d8f3"
# a= "cs628a{bcaaaaffa44d0d8d"
a = "give u a very difficult problem"
# a = "first time.You know m going to"
ass = "".join("{:02x}".format(ord(c)) for c in a)

# b = "2b1a16614c141f070d15124d2846070c14560b431757095e0d0617430e041a405718145b034317041318460208525e0d54425c1217131358550d180e5359541802091b13150e06130716094d1802584510125f064141521304051a44414c410f0b0e044f380e13460a5a57131740581f1701045456140e06535f12540e0d0743180e1441070a0d1a6c0c56595b464e0c141907514a"
b= "2b1a16614c141f070d15124d2846070c14560b431757095e0d0617430e"
b1 = "041a405718145b034317041318460208525e0d54425c1217131358550d18"
b3 = "0e5359541802091b13150e06130716094d1802584510125f064141521304"
b4 = "051a44414c410f0b0e044f380e13460a5a57131740581f1701045456140e"
b5 = "06535f12540e0d0743180e1441070a0d1a6c0c56595b464e0c141907514a"
print len(b)
# print len(b1)
binary_a = ass.decode("hex")
binary_b = b.decode("hex")
binary_b1 = b1.decode("hex")
binary_b2 = b3.decode("hex")
binary_b3 = b4.decode("hex")
binary_b4 = b5.decode("hex")
def xor_strings(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))

xored = xor_strings(binary_a, binary_b).encode("hex")
ans = ''.join(chr(int(xored[i:i+2], 16)) for i in range(0, len(xored), 2))
print ans


xored = xor_strings(binary_a, binary_b3).encode("hex")
ans = ''.join(chr(int(xored[i:i+2], 16)) for i in range(0, len(xored), 2))
print ans
xored = xor_strings(binary_a, binary_b1).encode("hex")
ans = ''.join(chr(int(xored[i:i+2], 16)) for i in range(0, len(xored), 2))
print ans

xored = xor_strings(binary_a, binary_b2).encode("hex")
ans = ''.join(chr(int(xored[i:i+2], 16)) for i in range(0, len(xored), 2))
print ans

xored = xor_strings(binary_a, binary_b4).encode("hex")
ans = ''.join(chr(int(xored[i:i+2], 16)) for i in range(0, len(xored), 2))
print ans

# # # a  =


# def xor_crypt_string(data, key='cs628a{', encode=False, decode=False):
#     from itertools import izip, cycle
#     import base64
#     if decode:
#         data = base64.decodestring(data)
#     xored = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))
#     if encode:
#         return base64.encodestring(xored).strip()
#     return xored


# secret_data = "2b1a16614c141f070d15124d2846070c14560b431757095e0d0617430e041a405718145b034317041318460208525e0d54425c1217131358550d180e5359541802091b13150e06130716094d1802584510125f064141521304051a44414c410f0b0e044f380e13460a5a57131740581f1701045456140e06535f12540e0d0743180e1441070a0d1a6c0c56595b464e0c141907514a"
# print xor_crypt_string(secret_data, encode=True)
# xored =  xor_crypt_string(xor_crypt_string(secret_data, encode=True), decode=True)
# ans = ''.join(chr(int(xored[i:i+2], 16)) for i in range(0, len(xored), 2))
