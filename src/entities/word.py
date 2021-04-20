class Word:

    def __init__(self, user, word, transl):
        self.user = user
        self.word = word
        self.translation = transl

    def __str__(self):
        return f'{self.user},{self.word},{self.translation}'
