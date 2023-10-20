class CountVectorizer:
    """Convert a set of text into a matrix of unique words
    and a calculated vector of the number of each word in the phrase"""
    def __init__(self):
        self.feature_names = []
        self.count_matrix = []

    def fit_transform(self, corp: list) -> list:
        """Convert the text into a calculated vector of the number of each word in the phrase"""
        self.feature_names = []
        self.count_matrix = []
        for word in ' '.join(corp).lower().split(' '):
            if word not in self.feature_names:
                self.feature_names.append(word)
        for i, text in enumerate(corp):
            self.count_matrix.append([])
            for word in self.feature_names:
                self.count_matrix[i].append(text.lower().split(' ').count(word))
        return self.count_matrix

    def get_feature_names(self) -> list:
        """Convert a set of text into a list of unique words"""
        return self.feature_names


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
