import crypt

def encrypt(pwd):
 ''' encrypt password using SHA encryption'''
  return crypt.crypt(pwd,"$6$HUZAx.Dp$")

xorWord = lambda ss,cc: ''.join(chr(ord(s)^ord(c)) for s,c in zip(ss,cc*100)) # encrypt a string using other string by xor'ing them
  	


