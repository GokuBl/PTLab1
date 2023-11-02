# -*- coding: utf-8 -*-
import os
import pytest
from src.Types import DataType
from src.DataJsonReader import DataJsonReader


class TestJsonReader:
    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        root_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = f'{root_dir}/test_data.json'

        data = {'Иванов Иван Иванович': [('математика', 80),
                                         ('литература', 76),
                                         ('программирование', 90)],
                'Петров Петр Петрович': [('математика', 100),
                                         ('химия', 61),
                                         ('социология', 90)]}

        return file_path, data

    def test_read(self, file_and_data_content: tuple[str, DataType]) -> None:
        file_content = DataJsonReader().read(file_and_data_content[0])
        assert file_content == file_and_data_content[1]
