# Сайт про времена года

Это учебный веб-проект на Django, посвящённый временам года. У каждого времени года своя страница с оформлением. Сайт включает регистрацию пользователей, отправку отзывов в Telegram и систему лайков/дизлайков в реальном времени.

## Функционал

- Отдельные страницы для **весны**, **лета**, **осени** и **зимы**
- Система **регистрации и входа** пользователей
- Форма для отправки **отзывов**, которые приходят в **Telegram-бот** создателю
- **Лайки/дизлайки** с обновлением в **реальном времени** через **WebSocket**
- Фронт на `HTML`, `CSS`, `JavaScript`
- Бэк на `Django`, с использованием `Django Channels` для WebSocket

## Запуск проекта

- Запуск происходит при помощи команды `python manage.py runserver` в терминале

