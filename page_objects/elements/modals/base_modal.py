#!/usr/bin/python3
# -*- encoding=utf8 -*-

from typing import Final
from page_objects.elements.base_element import WebElement


class ModalView(WebElement):

    CLOSE_BUTTON_SELECTOR: Final = 'turbo-modal__close'

    close_button = WebElement(css_selector='turbo-modal__close')

    def close(self):
        self.close_button.click()
        self.wait_until_not_visible()
