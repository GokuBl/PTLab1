from CalcRating import CalcRating
from DataJsonReader import DataJsonReader
from Types import DataType
import numpy


class CalcQuartile:
    def __init__(self, data: DataType):
        self.data = data
        self.debt_count = 0

    def calc(self):
        rating = CalcRating(self.data).calc()
        ratingSortedByKeyValue = sorted(rating.values())
        quartile = numpy.percentile(ratingSortedByKeyValue, 75)
        dict1 = {}
        for student in rating:
            if rating[student] > quartile:
                dict1[student] = rating[student]
        return dict1


if __name__ == "__main__":
    data = DataJsonReader().read('../data/data2.json')
