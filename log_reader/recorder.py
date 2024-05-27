import json
import time
import pandas as pd
from pathlib import Path
from parser import Parser


class DataRecorder:

    def __init__(self):
        self.data = Parser().get_data()
        self.p = Path('./output_data')

    def foo(self):
        print(self.data)

    def data_record(self):
        start = time.time()
        self.p.mkdir(parents=True, exist_ok=True)
        print("\x1b[38;5;76mХюстон, начинаю обработку!!!")
        with open('./output_data/my_log.json', 'w') as json_file:
            json.dump(self.data, json_file, ensure_ascii=False, indent=4)

        df = pd.read_json('./output_data/my_log.json')

        # txt
        df.to_csv('./output_data/my_log.txt', encoding='utf-8', index=False, header=None, sep=' ')

        # csv
        df.to_csv('./output_data/my_log.csv', encoding='utf-8', index=False)

        # xml
        df.to_xml('./output_data/my_log.xml', encoding='utf-8', index=False)

        # exel
        df.to_excel('./output_data/my_log.xlsx', index=False)


        with open('./output_data/my_log.txt', 'r', encoding="cp866") as file:
            content = file.readlines()
            content_len = len(content)

        end = time.time() - start
        print(f"Обработка завершена. \nОбработанно: \x1b[38;5;247m{content_len} строк за {end} сек.")
        

