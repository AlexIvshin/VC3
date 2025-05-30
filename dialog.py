model_name: str = 'первая'
title_app = 'VCom3'

# model_says fraze
answer_ok = ['О,кей!', 'Выполняю!', 'Хорошо', 'Секунду!', 'Легко!', 'Делаю!', 'Ун момент!']
answer_thanks = ['Всегда пожалуста!', 'Пожалуста!', 'Рада стараться!', 'На здоровье!']
answer_goodby = ['Пока, Хозяин!', 'Пока, Бос!', 'До новых встреч!', 'Всего хорошего!']
hello_answer = ['Здравствуйте, хозяин!', 'Привет, Бос!', 'Приветствую!', 'Привет!', 'Привет, Алекс!']
enter_pass_answer = ['Жду ввода пароля!', 'Введите пароль!', 'Необходимо ввести пароль!', 'Жду Ваш пароль!']
i_answer = ['Меня зовут Первая.', 'Моё имя Первая.', 'Я Первая.']
i_answer_other = ['Я начинающий секретарь.', 'Пытаюсь помогать создателю.', 'Я только учусь.']
qustion_replay = ['Ещё?', 'Как вам? Может ещё?', 'Понравилось? Может ещё?', 'Может ещё?', 'Могу ещё!',
                  'Повторить?', 'Могу повторить!']
qustion_confirmation = ['Вы уверены?', 'Уверены?', 'Точно?', 'Подтверждаете?']
done = ['Готово!', 'Выполнено!', 'Сделано!', 'Исполнено!']

actions_dict: dict = {
    'calculate': (
        1, 'посчитай', 'считай', 'посчитать', 'считать', 'подсчитать', 'пожалуйста', 'быстро'),
    'i_am_output': (
        2, 'кто', 'ты', 'что', 'как', 'тебя', 'зовут', 'звать', 'твоё имя'),
    'search': (
        2, 'поиск', 'найди', 'найти', 'ищи', 'окей', 'гугл', 'гугле', 'вопрос', 'запрос',
        'вики', 'википедия', 'википедии', 'что', 'такое', 'короткий', 'быстрый', 'ручной',
        'клавиатура', 'клавиатуры', 'ввод', 'вот', 'ручную'),
    'sys_down': (
        2, 'отключить', 'отключи', 'выключить', 'выключи', 'заверши', 'завершить',
        'выход', 'выйди', 'работу', 'компьютер', 'систему', 'системы'),
    'sys_reboot': (
        2, 'перезагрузить', 'перезагрузи', 'перегрузить', 'перегрузи', 'перезагрузка',
        'компьютер', 'компьютера', 'систему', 'системы', 'система'),
    'app_reboot': (
        1, 'перезапуск', 'перезапустись'),
    'conf_settings': (
        2, 'настройка', 'настройки', 'настроить', 'настрой', 'голос', 'голоса', 'микрофон', 'микрофона'),
    'volume_settings': (
        2, 'сделай', 'тише', 'громче', 'громкость'),
    'weather': (
        2, 'погода', 'погоду', 'в', 'во'),
    'mode_anonim': (
        2, 'анонимность', 'режим', 'анонимности', 'анонимный', 'анонимные'),
    'thanks_output': (
        1, 'спасибо', 'пасибо', 'благодарю', 'дякую'),
    'hello': (
        1, 'привет', 'здравствуй', 'здорово', 'добрый'),
    'stop_app': (
        1, 'стоп', 'отключись'),
    'random_joke': (
        2, 'расскажи', 'интересный', 'анекдот', 'факт', 'мочи', 'поведай', 'пословицу', 'поговорку', 'скажи'),
    'show_sys_info': (
        3, 'покажи', 'информацию', 'информации', 'информация', 'системе',
        'системную', 'системная', 'системы', 'инфу', 'выведи'),
    'exchange_rates': (
        2, 'курс', 'валюты', 'курсы', 'доллара', 'доллар', 'евро', 'злотого',
        'злотый', 'обмена', 'обмен', 'валют', 'покажи', 'скажи', 'польского', 'польский'),

    #  Bash скрипты
    'start_script_sudo_Xterm_sysfullupgrade': (
        2, 'апгрейд', 'обновление', 'обновить', 'обнови', 'системы', 'систему', 'систем'),
    'start_script_sudo_Xterm_ifacetool': (
        3, 'настройка', 'настройки', 'настроить', 'настрой',
        'беспроводной', 'интерфейс', 'беспроводного', 'интерфейса'),
    'start_script_sudo_XtermSmall_nmstart': (
        3, 'нетворк', 'менеджер', 'рестарт'),
    'start_script_sudo_XtermSmall_cleancashe': (
        2, 'очисти', 'очистить', 'почисти', 'почистить', 'кэш', 'кеш')
}
on_off_dict: dict = {
    'on': (
        'открой', 'открыть', 'запуск', 'запустить', 'запусти', 'активировать',
        'активируй', 'включить', 'включи', 'старт'),
    'off': (
        'отключить', 'отключи', 'выключить', 'выключи', 'закрой', 'закрыть',
        'убери', 'убрать', 'заверши', 'завершить', 'выход', 'выйти', 'выйди')
}
yes_no_dict: dict = {
    'yes': (
        'да', 'можно', 'давай', 'ага', 'хорошо', 'ещё', 'yes', 'Yes', 'y', 'Y'),
    'no': (
        'нет', 'не', 'надо', 'не', 'достаточно', 'хватит', 'No', 'no', 'N', 'n'),
    'cancel': (
        'отмена', 'отбой', 'отменить')
}
programs_dict: dict = {
    'google-chrome': ('хром', 'браузер'),
    'dolphin': ('долфин', 'проводник'),
    'kate': ('редактор', 'кат'),
    'code': ('код', 'майкрософт'),
    'konsole': ('терминал', 'консоль'),
    'kcalc': ('калькулятор', 'счёты'),
    'tor': ('тор', 'онион')
}
notebook_action_dict: dict = {
    'create_file': (
        2, 'создай', 'создать', 'файла', 'файл', 'файлы', 'файлу',
        'ручной', 'клавиатура', 'клавиатуры', 'ввод', 'вот', 'ручную'
    ),
    'edit_file': (
        2, 'редактируй', 'редактировать', 'отредактируй', 'измени', 'изменить', 'файла', 'файл', 'файлы', 'файлу'
    ),
    'read_file': (
        2, 'открой', 'отткрыть', 'прочти', 'покажи', 'показать', 'файла', 'файл', 'файлы', 'файлу'
    ),
    'save_file': (
        2, 'сохрани', 'сохранить', 'файла', 'файл', 'файлы', 'файлу'
    ),
    'choice_file': (
        2, 'выбрать', 'выбери', 'выбор', 'файла', 'файл', 'файлы', 'файлу'
    ),
    'delete_file': (
        2, 'удали', 'удалить', 'сотри', 'стереть', 'файла', 'файл', 'файлы', 'файлу'
    ),
    'rename_file': (
        2, 'переименуй', 'переименовать', 'файла', 'файл', 'файлы', 'файлу'
    ),
    'create_memo_file': (
        2, 'запомни', 'запомнить', 'запиши', 'пиши', 'инфу', 'информацию', 'дату'
    )
}
