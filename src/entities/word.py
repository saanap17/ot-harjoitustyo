class Word:

    def __init__(self, user, word, transl, language):
        self.user = user
        self.word = word
        self.translation = transl
        self.language = language

    def __str__(self):
        return f'{self.user},{self.word},{self.translation},{self.language}'
