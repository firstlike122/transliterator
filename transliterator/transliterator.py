"""
Date: 24.02.2022
Author: H. Ismoilov
Module: transliterator
Version: 0.0.1
What does it do: This module is used to transliterate cyrillic text to latin. Or vice versa.
"""

class Transliteration:
    # latin and cyrillic letters
    latins = ['A', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z',
              'a', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    cyrillics = ['А', 'Б', 'Д', 'Э', 'Ф', 'Г', 'Ҳ', 'И', 'Ж', 'К', 'Л', 'М',
                 'Н', 'О', 'П', 'Қ', 'Р', 'С', 'Т', 'У', 'В', 'Х', 'Й', 'З',
                 'а', 'б', 'д', 'э', 'ф', 'г', 'ҳ', 'и', 'ж', 'к', 'л', 'м',
                 'н', 'о', 'п', 'қ', 'р', 'с', 'т', 'у', 'в', 'х', 'й', 'з']
    # compounds of latin and cyrillic letters
    latin_compounds = ['Ts', 'Yo', 'Ya', 'Ye', 'Sh', 'Ch', "O'", "G'",
                       "ts", "yo", "ya", "ye", "sh", "ch", "o'", "g'"]
    cyrillic_compounds = ["Ц", 'Ё', 'Я', 'Е', 'Ш', 'Ч', 'Ў', 'Ғ',
                          "ц", "ё", "я", "е", "ш", "ч", "ў", "ғ"]
    # dictionary of latin and cyrillic letters
    l2c = dict(zip(latins, cyrillics))
    c2l = dict(zip(cyrillics, latins))
    l2c_compounds = dict(zip(latin_compounds, cyrillic_compounds))
    c2l_compounds = dict(zip(cyrillic_compounds, latin_compounds))

    def __init__(self, text=''):
        self.text = text
        self.tr_text = self.transliterate(text)

    def transliterate(self, word):
        if self.isLang(word, self.latins):
            return self.transliterator(word, self.l2c_compounds, self.l2c)
        elif self.isLang(word, self.cyrillics):
            return self.transliterator(word, self.c2l_compounds, self.c2l)
        else:
            return word

    def transliterator(self, text, dictionary2, dictionary1=[]):
        for char in dictionary1.keys():
            text = text.replace(char, dictionary1[char])
        for i in text:
            if i in dictionary2:
                text = text.replace(i, dictionary2[i])
        return text

    def isLang(self, text, langlist):
        for i in langlist:
            if i in text:
                return True
        return False

    def from_file(self, filename):
        with open(filename, 'r') as f:
            self.text += f.read()
        self.tr_text = self.transliterate(self.text)
        return self.tr_text

    def to_file(self, text, filename):
        self.tr_text = self.transliterate(text)
        with open(filename, 'w') as f:
            f.write(self.tr_text)

    def f2f(self, filename1, filename2):
        self.tr_text = self.from_file(filename1)
        with open(filename2, 'w') as f:
            f.write(self.tr_text)

    def to_self(self, filename):
        self.tr_text = self.from_file(filename)
        with open(filename, 'w') as f:
            f.write(self.tr_text)