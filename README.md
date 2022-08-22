# mini_crm_system
Small crm system for data input into a sql table.   .
Для чего эта программа?
Программа предполагает определение веротяности сбываемости продаж, и рассчет вероятных продаж к концу периода.
Для примера. В компании условно есть 10 руководителей групп продаж, каждая группа продаж имеет наименование, и в каждой группе работает определенное кол-во менеджеров.
Задача этой программы, вносить предполагаемые продажи по менеджерам через форму, чтобы эти данные попадали в таблицу в бд. Далее, данные агрегируются нужным для нас образом, процедурой написаной в ms sql, которые по итогу попадают в новую таблицу из которой мы строим отчет (в моем случае это отчет в excel). И далее в этом отчете мы видим, какая сбываемость продаж у каждого руководителя и видим  цифру сколько продаж мы прогнозируем под конец выбранного периода, с учетом сбываемости. Вот и подвел к конкретной задаче это программы!  
То есть последовательность действий такая: 
- Руководитель входит в программу
- вносит предполагаемые продажи по менеджеру, вносит клиентов, кто отказался от покупки, и тех, кто по итогу  по итогу оформил заказ
- У меня в ms sql management studio написана процедура, которая обрабатывает исходные данные и агрегирует нужным нам образом, присваивая каждому руководителю % сбываемости продаж и тем самым прогнозируя, сколько продаж у нас будет к концу выбранного периода, в принципе для чего эта программа и была нужна, как я уже сказал выше.
- Далее данные из это процедуры просто попадают в отчет, и вуоля, смотрим, анализируем, делаем выводы.

По внутрянке:
Все функции прописаны в файле DataBaseForm, к кажой функции прописана документация и комментарии, для использования там необходимо только вставить 
-  название сервера
-  название бд
-  Ваш логин
-  Ваш пароль
Можно упростить жизнь и создать переменные с этими значениями.
И также необходимо переписать запросы под ваши нужды! 

В файле Narabotki_ap по сути солянка из бэкенда и фротенда, с перевесом в сторону второго.
Там прописано создание двух окон и вызываемые функции на кнопки. Как обновляется внутренняя таблица итд...

Здесь мы сначала создаем окно для входа, куда нужно заполнить логин и пароль, можно было создать форму регистрации, но я решил, что сам создам всем пароли, ибо так будет надежнее (просто выгружаем таблицу с сотрудниками и каждой ячейке рандомно присваимваем число от 10000 до 1000000)
Далее по логину и паролю входим и у нас открывается само окно с внесением данных 
- в верхнем блоке соответственно окна для внесения данных, в некоторых есть виджеты типо выпадающего списка или календаря
- Во втором блоке кнопки. "Внести наработку" означает внести данные в базу
- В третьем блоке построена интерактивная табличка, которая обновляется при внесении и удалении строк!
- И внизу блок с удалением строки по номеру, в случае ошибки при внесении данных
Далее, у меня есть функция execer - она просто выполняет процедуру в базе (агрегирующую для итогового отчета), ее я через pyinstaller вывожу в .exe файл и через утилиту в Windows 'планировщике заданий' обновляю ее каждые пол часа.
И далее у меня есть отчет, в который эти данные подтянуты, на него написан скрипт на vba, который также обновляет его каждые пол часа
