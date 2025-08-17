# Jackett HAOS Add-on (через HACS)

⚡ Установка Jackett в Home Assistant OS с полной интеграцией.

## Возможности
- Установка через HACS
- Автоматический запуск Docker-контейнера Jackett
- Добавление популярных трекеров (1337x, TPB, YTS, EZTV)
- API-ключ подтягивается автоматически
- Интеграция с Sonarr и Radarr (в будущем)

## Установка
1. Установите [HACS](https://hacs.xyz/).
2. В HACS → Integrations → Custom repositories добавьте:
   https://github.com/yourusername/hacs-jackett
3. Установите интеграцию **Jackett**.
4. Через **Developer Tools → Services** можно вызвать:
   - `jackett.start` → запустить Jackett
   - `jackett.stop` → остановить Jackett
