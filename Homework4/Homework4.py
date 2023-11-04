from math import log


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


class TfidfTransformer:

    def __init__(self):
        self.tf = []
        self.idf = []

    def fit_transform(self, count_matrix: list) -> list:
        """Term Frequency - Inverse Document Frequency is a measurement of how important a word is to a document.
        The tf-idf value increases with the number of times a word appears in a document (tf)
        and is offset by the frequency of the word in the corpus (idf)"""
        self.tf = self.tf_transform(count_matrix)
        self.idf = self.idf_transform(count_matrix)
        for tf_vector in self.tf:
            for tf in range(len(tf_vector)):
                tf_vector[tf] = round(tf_vector[tf] * self.idf[tf], 3)
        return self.tf

    def tf_transform(self, count_matrix: list) -> list:
        """Converts the text into a matrix of the frequency of use of the term"""
        tf_matrix = []
        for words_list in count_matrix:
            tf_vector = []
            for word_count in words_list:
                tf = round(word_count / sum(words_list), 3)
                tf_vector.append(tf)
            tf_matrix.append(tf_vector)
        return tf_matrix

    def idf_transform(self, count_matrix: list) -> list:
        """Converts text to vector by the inverse frequency of the document"""
        doc_with_word = [0] * len(count_matrix[0])
        for words_list in count_matrix:
            for word in range(len(words_list)):
                if words_list[word] > 0:
                    doc_with_word[word] += 1
        idf = [round(log((len(count_matrix) + 1) / (doc_with_word[word] + 1)) + 1, 1) for word in doc_with_word]
        return idf


class TfidfVectorizer(CountVectorizer):

    def __init__(self):
        self.transform = []
        super().__init__()

    def fit_transform(self, text: list) -> list:
        """Convert the text into a tf-idf matrix"""
        count_matrix = super().fit_transform(text)
        transformer = TfidfTransformer()
        self.transform = transformer.fit_transform(count_matrix)
        return self.transform


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(tfidf_matrix)
