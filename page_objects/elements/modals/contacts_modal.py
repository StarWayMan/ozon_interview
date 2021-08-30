#!/usr/bin/python3
# -*- encoding=utf8 -*-

from typing import Final

from page_objects.elements.base_element import WebElement, WebElements
from page_objects.elements.modals.base_modal import ModalView

COMPANY_NAME_SELECTOR: Final = 'lc-phone__company-name'
COMPANY_PHONE_SELECTOR: Final = 'lc-phone__phone'
ANSWER_BUTTON_SELECTOR: Final = 'lc-phone__button'


class ContactsModal(ModalView):

    company_name = WebElement(css_selecor=COMPANY_NAME_SELECTOR)
    company_phone = WebElement(css_selecor=COMPANY_PHONE_SELECTOR)
    answer_buttons = WebElements(css_selector=ANSWER_BUTTON_SELECTOR)

    def click_yes(self):
        self.answer_buttons.get_element_with_text('Да').click()

    def click_no(self):
        self.answer_buttons.get_element_with_text('Пока нет').click()

    def click_not_yet(self):
        self.answer_buttons.get_element_with_text('Не взяли трубку').click()
