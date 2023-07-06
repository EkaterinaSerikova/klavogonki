import time
import config
from playwright.sync_api import Page


class MainPage:

    _FAST_START_BUTTON = 'div.col2 > div > a.title'
    _HOW_TO_PLAY_WINDOW = '#howtoplay table'
    _HOW_TO_PLAY_CLOSE_BUTTON = '#howtoplay input'

    def open_main_page(self, page: Page) -> None:  # noqa
        page.goto(config.url.DOMAIN)

    def click_on_fast_start_button(self, page: Page):
        page.locator(self._FAST_START_BUTTON).click()
        time.sleep(2)

    def close_how_to_play_window_if_needed(self, page: Page):
        if page.locator(self._HOW_TO_PLAY_WINDOW).is_visible():
            page.locator(self._HOW_TO_PLAY_CLOSE_BUTTON).click()
