class WordsFinder:
    def __init__(self, *names):
        self.name_file = names
    def get_all_words(self):
        all_words = dict()
        symbols = [',', '.', '=', '!', '?', ';', ':', '-']
        for file in self.name_file:
            with open(file, encoding='utf-8') as f:
                line1 = ''
                for line in f:
                    line = line.lower()
                    for symbol in symbols:
                        if symbol in line:
                            line = line.replace(symbol, '')
                    line1 += line
                    all_words[file] = line1.split()

        return all_words
    def find(self, word):
        finder = dict()
        for name, words in self.get_all_words().items():
            for i in words:
                if word.lower() in i:
                    finder[name] = words.index(word.lower()) + 1
        return finder
    def count(self, word):
        count = 0
        counter = dict()
        for name, words in self.get_all_words().items():
            for j in range(len(words)):
                if word.lower() == words[j]:
                    count += 1
                    counter[name] = count
        return counter




result = WordsFinder('test_file1.txt', 'test_file2.txt')
print(result.get_all_words())
print(result.find('рыбки'))
print(result.count('text'))
