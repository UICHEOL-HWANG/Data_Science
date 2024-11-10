import os
class Setconfig:
    def __init__(self):
        self.months = [f'2023{mth:02}' for mth in range(1, 13)]
        self.ages = [x for x in range(10, 90, 10)]
        self.gender = ['M', 'F']

        file_path = os.path.join(os.path.dirname(__file__), '.natcode')
        with open(file_path, 'r', encoding='UTF-8') as file:
            self.natcode = eval(file.read())

