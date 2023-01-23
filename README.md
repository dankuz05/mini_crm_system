
Программа предназнчена для внесения информации в базу данных с фиксированной формой, для проведения ежедневных планерок.
Для примера. В компании условно есть 10 руководителей групп продаж, каждая группа  имеет наименование, и в каждой группе работает определенное кол-во менеджеров.
Задача этой программы, вносить клиентов, по которым ведется работа в части продажи им определнного продукта на определенную дату. Дальше эти данные попадают в очтет, где ежедневно отслеживается, сколько у нас на сегодня запланировано закрыть продаж, кого мы ведем итд

Окно логина:
![image](https://user-images.githubusercontent.com/81446183/214002593-0b56f175-ee0e-4421-9025-4f16d2b10379.png)


Само окно программы:
![image](https://user-images.githubusercontent.com/81446183/214002684-52938d50-2ceb-457e-8a9b-c4223716c7a5.png)


Результат, вот такая небольшая табличка:
![image](https://user-images.githubusercontent.com/81446183/214003410-35a95a29-cbd9-4dd5-a684-647dececf893.png)



По внутрянке:
Все функции прописаны в файле DataBaseForm, к каждой функции прописана документация и комментарии, для использования там необходимо только вставить в файл passwords: 

-  название сервера
-  название бд
-  Ваш логин
Эти данные забиты в переменные на листе датабейз



В файле Narabotki_ap по сути солянка из бэкенда и фротенда, с перевесом в сторону второго.
Там прописано создание двух окон и вызываемые функции на кнопки. Как обновляется внутренняя таблица в ококшке итд...

Здесь мы сначала создаем окно для входа, куда нужно заполнить логин и пароль, можно было создать форму регистрации, но я решил, что сам создам всем пароли, ибо так будет надежнее (просто выгружаем таблицу с сотрудниками и каждой ячейке рандомно присваимваем число от 10000 до 1000000)
Далее, заходим по логину и паролю  и у нас открывается само окно с внесением данных.
- в верхнем блоке, соответственно, окна для внесения данных. В некоторых есть виджеты типо выпадающего списка или календаря.
- Во втором блоке кнопки. "Внести наработку" означает внести данные в базу.
- В третьем блоке построена интерактивная табличка, которая обновляется при внесении и удалении строк!
- И внизу блок с удалением строки по номеру, в случае ошибки при внесении данных.


Далее, у меня есть функция execer - она просто выполняет процедуру в базе (агрегирующую для итогового отчета), ее я через pyinstaller вывожу в .exe файл и через утилиту в Windows 'планировщике заданий' обновляю ее каждые пол часа.
И далее у меня есть отчет, в который эти данные подтянуты, на него написан скрипт на vba, который также обновляет его каждые пол часа
