import os
import string
from idlelib.iomenu import encoding

class WordsFinder:
    def __init__(self, *file_name):
        self.file_name = file_name


    def get_all_words(self):
        all_words = {}
        words = []
        for name in self.file_name:
            with open (name, encoding = 'utf - 8') as file:
                for i in file:
                    i = i.lower()
                    string.punctuation
                    for p in string.punctuation:
                        if i == '`':
                            i = i.replace(p,' ')
                    words.extend(i.split())
        all_words [self.file_name] = words
        return all_words

    def find(self,word):
        word = word.lower()
        other_words = {}
        # list_words = []
        for name, words in self.get_all_words().items():
            if word in words:
                other_words[name] = words.index(word)+1
                return other_words

    def count(self,word):
        word = word.lower()
        other_words = {}
        for name, words in self.get_all_words().items():
            # list_words.append(words)
            if word in words:
                other_words[name] = len(word)
                return other_words

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
# # os.getcwd()


# line = '- Мама мыла раму, а Маша помогала. (из прописи 1 класса)'
# import string
# string.punctuation
# # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
#
# # пунктуацию будем удалять в цикле
# for p in string.punctuation:
#     if p in line:
#         # банальная замена символа в строке
#         line = line.replace(p, '')
#
# line.strip()