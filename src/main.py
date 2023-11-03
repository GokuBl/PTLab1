# -*- coding: utf-8 -*-
import argparse
from DataJsonReader import DataJsonReader
from CalcRating import CalcRating
from TextDataReader import TextDataReader
from CalcQuartile import CalcQuartile


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = "../data/data.TXT"
    print("path: ", path)
    reader = TextDataReader()
    students = reader.read(path)
    print("Students: ", students)
    rating = CalcRating(students).calc()
    print("Rating: ", rating)

    path = "../data/data2.json"
    jsonReader = DataJsonReader()
    jsonData = jsonReader.read(path)
    print("Json: ", CalcRating(jsonData).calc())
    rating2 = CalcQuartile(jsonData).calc()
    print("JsonQuartile: ", rating2)


if __name__ == "__main__":
    main()
