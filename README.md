###  Скачиваешь 
```bash
git clone https://github.com/gipsypunk/log_reader.git
```

### Запускаешь виртуалку
```bash
cd log_reader
pipenv shell 
# если pipenv не стоит на машине установить
```

### Подтягиваешь зависимости
```bash
pip install -r requirements.txt
```

### В корне есть конфигурационный файл (config.ini), надо заменить на путь к твоему логу или скопировать лог и закинуть в папку logs
```bash
[Settings]
log_path = /your/log/path
```

### Запускаешь парсер 
```bash
 python3 log_reader
```

### Все новые логи сохраняются в папке output_data


