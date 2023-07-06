from playwright.sync_api import Page


class GamePage:
    _START_GAME_BUTTON = '#host_start'
    _RACING_TIME = '#racing'
    _INPUT_TEXT_FIELD = '#inputtext'
    _SPEED_RESULT = '//div[@class="player you ng-scope"]/div/div[3]/div[2]/span[1]'
    _TEXT = '//*[@id="typefocus"]'
    _AFTER_FOCUS = '//*[@id="afterfocus"]'
    _NUMBER_OF_ERRORS = '//div[@class="player you ng-scope"]/div/div[3]/div[3]/span[1]'
    _CYR_DICT = {
        'c': 'с',
        'o': 'о',
        'a': 'а',
        'x': 'х',
        'e': 'е',
        'p': 'р',
        'k': 'к',
        'H': 'Н',
        'B': 'В',
        'M': 'М',
        'K': 'К',
        'C': 'С',
        'A': 'А',
        'T': 'Т',
        'O': 'О',
        'X': 'Х',
        'E': 'Е',
        'P': 'Р',
    }

    def click_start_game_button_if_needed(self, page: Page):
        if page.is_visible(self._START_GAME_BUTTON):
            page.locator(self._START_GAME_BUTTON).click()

    def click_start_game_button(self, page: Page):
        page.locator(self._START_GAME_BUTTON).click()

    def wait_until_game_starts(self, page: Page):
        page.locator(self._RACING_TIME).is_visible()

    def input_text(self, page: Page):
        while page.locator(self._AFTER_FOCUS).inner_text() != '.':
            text = page.locator(self._TEXT).inner_text().strip()
            for latin, cyr in self._CYR_DICT.items():
                text = text.replace(latin, cyr)
            page.locator(self._INPUT_TEXT_FIELD).fill(text)
            page.keyboard.press('Space')

        text = page.locator(self._TEXT).inner_text().strip()
        for latin, cyr in self._CYR_DICT.items():
            text = text.replace(latin, cyr)
        page.locator(self._INPUT_TEXT_FIELD).fill(text + '.')
        page.keyboard.press('Space')

    def check_speed_result(self, page: Page):
        return int(page.locator(self._SPEED_RESULT).text_content())

    def check_number_of_errors(self, page: Page):
        return int(page.locator(self._NUMBER_OF_ERRORS).text_content())
