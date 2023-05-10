# Final_progect_28

В финальном проекте тестировался продукт https://b2c.passport.rt.ru. Регистрация/авторизация пользователя. 
Для выявления багов, были составлены негативные и позитивные тест кейсы и баг репорты на основе требований - https://docs.google.com/spreadsheets/d/1VHgWBnVTqBGTeRkg_1aY4W9I0c66KaQ3/edit?usp=sharing&ouid=106437759474687022453&rtpof=true&sd=true
 Были актуализированы требования - https://docs.google.com/document/d/1F8gGa6_6WMgJSarfmnxpcHnAbLqnK04N/edit?usp=sharing&ouid=106437759474687022453&rtpof=true&sd=true

Для тестирования были составлены автотесты с  использованием  языка Python https://github.com/tatianasu/Final_progect_28

Для поиска нужных элементов на Веб-странице - Devtools,
Для эмуляции ручного тестирования модуль Selenium, 
Для упрощения понимания кода патерн - Page Obgect,

Ход регистрации отображен в функциональном тестировании

Тесты запускаются командой: python -m pytest -v --driver Chrome --driver-path C:\chromedriver C:\Users\User\PycharmProjects\final_project_SF_28/Tests.py

Тесты запускаются при установленной библиотеки Python Selenium
