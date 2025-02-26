import unittest
import Test_2
# вывести сроку в обратном порядке
class py_test(unittest.TestCase):
    def test_string(self):
       self.assertEqual(Test_2.back_string('Hello'),'olleH')

    def test_string(self):
       self.assertEqual(Test_2.back_string('Car'),'raC')

    def test_string(self):
       self.assertEqual(Test_2.back_string('Tools'),'slooT')

    def test_string(self):
       self.assertEqual(Test_2.back_string('World'),'dlroW')

    def test_string(self):
       self.assertEqual(Test_2.back_string('Dogs'),'sgoD')
#-------------------------------------------------------------------------
# Полиндром
    def test_polindroms(self):
        self.assertEqual(Test_2.polindrome('Anna'),('Anna'))

    def test_polindroms(self):
        self.assertEqual(Test_2.polindrome('stats'),('stats'))

    def test_polindroms(self):
        self.assertEqual(Test_2.polindrome('refer'),('refer'))

    def test_polindroms(self):
        self.assertEqual(Test_2.polindrome('madam'),('madam'))

    def test_polindroms(self):
        self.assertEqual(Test_2.polindrome('level'),('level'))
#---------------------------------------------------------------
    # проверяет количество гласных
    def test_vowels(self):
       self.assertEqual(Test_2.vowels('Шла'),1)

    def test_vowels(self):
        self.assertEqual(Test_2.vowels('Машина'), 3)

    def test_vowels(self):
       self.assertEqual(Test_2.vowels('Собака'),3)

    def test_vowels(self):
       self.assertEqual(Test_2.vowels('Кошка'),2)

    def test_vowels(self):
       self.assertEqual(Test_2.vowels('Школа'),2)

    #def test_symbols(self):
     #   self.assertEqual(Test_2.symbol('Hello world'),('Helo wrd')
#-------------------------------------------------------------------------
    def test_remove_duplicates(self):
        self.assertEqual(Test_2.remove_duplicates("Hello world"), "Helo wrd")

    def test_remove_duplicates(self):
        self.assertEqual(Test_2.remove_duplicates("he knows Inglish"), "he knows gli")

    def test_remove_duplicates(self):
        self.assertEqual(Test_2.remove_duplicates("qweqweqwe"), "qwe")

    def test_remove_duplicates(self):
        self.assertEqual(Test_2.remove_duplicates("asdasdasd"), "asd")

    def test_remove_duplicates(self):
        self.assertEqual(Test_2.remove_duplicates("zxczxczxc"), "zxc")


if __name__ == 'main':
    unittest.main()