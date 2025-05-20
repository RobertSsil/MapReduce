import re
import json
from mrjob.job import MRJob
from mrjob.step import MRStep

class WordCounter(MRJob):

    def mapper(self, _, line):
        # Cada linha é um objeto JSON
        review = json.loads(line)
        review_text = review.get('reviewText', "")

        # Tokenização simples (palavras alfanuméricas em minúsculas)
        tokens = re.findall(r"\b\w+\b", review_text.lower())

        for token in tokens:
            yield token, 1

    def combiner(self, word, counts):
        yield word, sum(counts)

    def reducer(self, word, counts):
        yield word, sum(counts)

    def steps(self):
        return [
            MRStep(
                mapper=self.mapper,
                combiner=self.combiner,
                reducer=self.reducer
            )
        ]

if __name__ == '__main__':
    WordCounter.run()
