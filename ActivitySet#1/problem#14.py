# Using Web Services
# https://www.py4e.com/lessons/servces

class ceaser:
    def __init__(self, shift, text):
        self.shift = int(shift)
        self.text = text
    
    def encrypt(self):
        d = ''
        for i in self.text:
            if (i == ' '):
                d += ' '
            else:
                d += (chr(ord(i) + self.shift))
        return d

    def decrypt(self):
        d = ''
        for i in self.text:
            if (i == ' '):
                d += ' '
            else:
                d += (chr(ord(i) - self.shift))
        return d

text = 'What do you want to encrypt'
a = ceaser(3, text)
print(a.encrypt())
a.text ='Zkdw gr |rx zdqw wr hqfu|sw'
print(a.decrypt())