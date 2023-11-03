# -*- coding: utf-8 -*-
from src.Types import DataType
from src.CalcQuartile import CalcQuartile
import pytest

RatingsType = dict[str, float]


class TestCalcQuartile:
    @pytest.fixture()
    def input_data(self) -> tuple[DataType, RatingsType]:
        data: DataType = {'Иванов Иван Иванович': [('математика', 80),
                                                   ('литература', 76),
                                                   ('программирование', 90)],
                          'Петров Петр Петрович': [('математика', 100),
                                                   ('химия', 61),
                                                   ('социология', 90)],
                          'Алексеев Петр Петрович': [('математика', 10),
                                                   ('химия', 31),
                                                   ('социология', 30)]
                          }
        rating_scores: RatingsType = {
            "Иванов Иван Иванович": 82.0,
            "Петров Петр Петрович": 83.66666666666667,
            "Алексеев Петр Петрович": 23.666666666666668
        }
        return data, rating_scores

    def test_init_calc_quartile(self,
                              input_data: tuple[DataType, RatingsType]
                              ) -> None:
        calc_rating = CalcQuartile(input_data[0])
        assert input_data[0] == calc_rating.data

    def test_calc(self,
                  input_data: tuple[DataType, RatingsType]) -> None:
        rating = CalcQuartile(input_data[0]).calc()
        for student in rating:
            rating_score = rating[student]
            assert pytest.approx(rating_score,
                                 abs=0.001) == input_data[1][student]
