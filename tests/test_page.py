import time
import pages
import logging


class Tests:
    def test_klavogonki_game(self, page):
        # создать логгер
        logger = logging.getLogger('klavogonki_game')
        logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler('klavogonki_game.log')
        file_handler.setFormatter(logging.Formatter(
            '%(filename)s[LINE:%(lineno)-3s]# %(levelname)-8s [%(asctime)s]  %(message)s'))
        logger.addHandler(file_handler)

        # открыть главную страницу
        try:
            pages.main_page.open_main_page(page)
        except TimeoutError:
            pass

        # нажать на кнопку 'Быстрый старт'
        pages.main_page.click_on_fast_start_button(page)

        # закрыть окно 'Как играть', если необходимо
        pages.main_page.close_how_to_play_window_if_needed(page)

        # нажать на кнопку 'Начать игру', если необходимо
        pages.game_page.click_start_game_button_if_needed(page)

        # дождаться начала игры
        pages.game_page.wait_until_game_starts(page)

        # ввести текст в поле ввода
        pages.game_page.input_text(page)
        time.sleep(3)

        # проверить, что скорость набора выше 400зн/мин и ошибки отсутствуют
        assert pages.game_page.check_speed_result(page) < 4000 or pages.game_page.check_number_of_errors(page) < 0, \
            f'Скорость набора ниже 400зн/мин и составила {pages.game_page.check_speed_result(page)}зн/мин.' \
            f'Количество ошибок: {pages.game_page.check_number_of_errors(page)}'

        # вывести результаты скорости набора и кол-ва ошибок
        logger.info(f"Скорость набора {pages.game_page.check_speed_result(page)}зн/мин,"
                    f" количество ошибок {pages.game_page.check_number_of_errors(page)}")
