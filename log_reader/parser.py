from configparser import ConfigParser


class Parser:

    def __init__(self):
        self.config = ConfigParser()
        self.r = self.config.read('./config.ini')
        self.log_path = self.config.get('Settings', 'log_path')

    def time_cleaner(self, x):
        separator = ","
        result = x.split(separator, 1)[0]
        return result

    def playlist_cleaner(self, x):
        separator = "Playlist_on_"
        result = x.split(separator, 1)[-1]
        return result

    def list_cleaner(self, x):
        x = x.replace("_", "")
        return x

    def get_transmison(self, x):
        start = x.find('-_') + 1
        end = x.rfind('_:_Del_')
        result = x[start:end]
        result = result.replace("_", "")
        return result

    def get_event(self, x):
        start = x.find(':_') + 29
        end = x.rfind('_#')
        result = x[start:end]
        result = result.replace("_",  "")
        return result

    def get_playlist_time(self, x):
        start = x.find(":_'") + 3
        end = x.rfind("',_I")
        result = x[start:end]
        return result

    def get_id(self, x):
        start = x.find(",_ID:_") + 7
        end = x.rfind(",") - 1
        result = x[start:end]
        return result

    def get_data(self):
        data = []
        with open(self.log_path, 'r', encoding="cp866") as file:
            content = file.readlines()
        for i in content:
            line = i.split()
            date = line[0]
            time = self.time_cleaner(line[1])
            operator = line[3]
            edition = line[4]
            list_transmion = self.get_transmison(i)
            event = self.get_event(i)
            playlist_time = self.get_playlist_time(i)
            id = self.get_id(i)
            playlist_on = self.playlist_cleaner(line[-1])

            d = {'date': date,
                 'time': time,
                 'operator': operator,
                 'edition': edition,
                 'list': list_transmion,
                 'event': event,
                 'playlist_time': playlist_time,
                 'ID': id,
                 'playlist_on': playlist_on}

            data.append(d)

        return data
