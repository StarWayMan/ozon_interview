#!/usr/bin/python3
# -*- encoding=utf8 -*-

from typing import Final
from page_objects.elements.base_element import WebElement

CLEAR_BUTTON_SELECTOR: Final = 'lc-input__clear'


class TextInput(WebElement):

    CLOSE_BUTTON_SELECTOR: Final = 'turbo-modal__close'

    clear_button = WebElement(css_selector=CLEAR_BUTTON_SELECTOR)

    def click_clear_button(self):
        self.clear_button.click()
        self.wait_until_not_visible()
