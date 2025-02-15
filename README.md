# Тестовое задание Avito

Здравствуйте! Меня зовут Степан, здесь я опишу как я выполнил тестовое задание и как можно запустить автотесты.

## Структура проека

```
├── img              # папка со с скриншотами багов
├── BUGS.md          # файл с описанием найденных багов
├── README.md        # описание проекта и инструкция 
├── requests_api.py  # методы для создания запросов к API
├── requirements.txt # зависимости
├── task1.md         # файл с описанием найденных багов
├── test_1.py        # 
├── test_2.py        #
├── test_3.py        #
├── test_4.py        #
├── test_5.py        #
├── test_6.py        #
├── test_7.py        # автотесты
└── TESTCASES.md     # тесткейсы ко 2 заданию
```

## Задание №1
В первом задании необходимо перечислить баги, найденные на скриншоте страницы сайта и расставить их приоритеты. Решение задания предложено в файле [task1.md](./task1.md)

## Задание №2

Задание выполнено в рекомендуемой связке `Python + Pytest`.  

В файле [TESTCASES.md](./TESTCASES.md) приведены тесткейсы для автотестов. В файле [BUGS.md](./BUGS.md) приведены найденные баги.

### Инструкция по запуску тестов
1. Склонируйте к себе репозиторий, в котором хранится проект тестового задания, через выполнение команды в терминале
    ```
    git clone 
    ```
    Или скачайте zip архив по [ссылке]() и распакуйте его


2. Убедитесь, что на Вашем компьютере установлен Python. В командной строке/терминале выполните команду
    ```
    python -v
    ```  

    Если он не установлен, то установите с официального [сайта Python](https://www.python.org/downloads/), выбрав подходящую версию для Вашей операционной системы, и пройдите шаг сначала.  
    >В процессе установки обязательно поставьте галочку в чекбоксе "Add python.exe to PATH". Иначе, у Вас не будет корректно отображаться версия Python


3. Через командную строку/терминал перейдите в директорию второго задания, выполнив команду
   ```
   cd /здесь укажите путь до директории с проектом
   ```


4. Установите необходимые зависимости из файла `requirements.txt`, выполнив команду  
   ```
   pip install -r requirements.txt
   ```
   если она не выполняется, то попробуйте
   ```
   pip3 install -r requirements.txt
   ```

5. Наконец, запустите тесты, выполнив команду  
   ```
   pytest -v
   ```