'''
chr(unicode) ===> The corresponding character
chr(unicode) ===> The corresponding character
Q  ord('a') -> return 97
   chr(65) -> return A

   s = 'a5b2c9'
   output-> afbdcl
'''

# s = 'a5b2c9'
s = input("Enter Some String:")
output = ''

for i in s:
    if i.isalpha():
        output = output+i
        prev = i
    else:
        output = output+chr(ord(prev)+int(i))

print(output)
