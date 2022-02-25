import unittest

from src.transliterator.transliterator import Transliteration


class TransliteratorTest(unittest.TestCase):
    tr = Transliteration()

    def test_transliterate(self):
        self.assertEqual(self.tr.transliterate('Абрамович'), "Abramovich")
        self.assertEqual(self.tr.transliterate('Abramovich'), "Абрамович")
        self.assertEqual(self.tr.transliterate(
            'Пэня Абрамович. 1998-йил январда туғулган.'),
            "Penya Abramovich. 1998-yil yanvarda tug'ulgan.")
        self.assertEqual(self.tr.transliterate(
            "Penya Abramovich. 1998-yil yanvarda tug'ulgan."),
            "Пэня Абрамович. 1998-йил январда туғулган.")
        self.assertEqual(self.tr.transliterate(
            'АБДЭФГҲИЖКЛМНОПҚРСТУВХЙЗабдэфгҳижклмнопҚрстувхйз'),
            'ABDEFGHIJKLMNOPQRSTUVXYZabdefghijklmnopQrstuvxyz')

    def test_transliterator(self):
        l2c_comp = {'Ts': 'Ц', 'ts': 'ц', 'Ya': 'Я'}
        c2l_comp = {'Ц': 'Ts', 'ц': 'ts', 'Я': 'Ya'}
        l2c = {'a': 'а', 'b': 'б', 'A': 'А', 'B': 'Б'}
        c2l = {'а': 'a', 'б': 'b', 'А': 'A', 'Б': 'B'}
        self.assertEqual(
            self.tr.transliterator('aa', l2c_comp, l2c), 'аа')
        self.assertEqual(
            self.tr.transliterator('bTs AYa', l2c_comp, l2c), 'бЦ АЯ')
        self.assertEqual(
            self.tr.transliterator('бЦ', c2l_comp, c2l), 'bTs')
        self.assertEqual(
            self.tr.transliterator('бЦ АЯ', c2l_comp, c2l), 'bTs AYa')

    def test_islang(self):
        self.assertTrue(self.tr.isLang('salom', self.tr.latins))
        self.assertFalse(self.tr.isLang('salom', self.tr.cyrillics))


unittest.main()
