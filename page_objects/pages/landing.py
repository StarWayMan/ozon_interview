#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os
from typing import Final

from page_objects.elements.base_element import WebElement, WebElements
from page_objects.pages.base_page import WebPage

LANDING_URL: Final = 'https://mokasi.turbo.site/mokasi'

# Selectors
CONTACTS_BUTTON_SELECTOR: Final = '.lc-phone__content'
CONTACTS_MODAL_SELECTOR: Final = '.lc-phone__modal-wrapper'
CLOSE_MODAL_BUTTON_SELECTOR: Final = '.turbo-modal__close'
COMPANY_NAME_SELECTOR: Final = '.lc-phone__company-name'
COMPANY_PHONE_SELECTOR: Final = '.lc-phone__phones-container'
ANSWER_BUTTON_SELECTOR: Final = '.lc-phone__button'
CLEAR_TEXT_FIELD_BUTTON_SELECTOR: Final = '.lc-input__clear'
ADD_TO_CART_BUTTON_SELECTOR: Final = '.lc-add-to-cart'
HEADER_CART_BUTTON_SELECTOR: Final = '.lc-header__cart-button'


class Landing(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or LANDING_URL

        super().__init__(web_driver, url)

    # Elements on the page
    contacts_button = WebElement(css_selector=CONTACTS_BUTTON_SELECTOR)
    contacts_modal = WebElement(css_selector=CONTACTS_MODAL_SELECTOR)
    company_name = WebElement(css_selector=COMPANY_NAME_SELECTOR)
    company_phone = WebElement(css_selector=COMPANY_PHONE_SELECTOR)
    answer_buttons = WebElements(css_selector=ANSWER_BUTTON_SELECTOR)
    close_button = WebElement(css_selector=CLOSE_MODAL_BUTTON_SELECTOR)
    clear_button = WebElement(css_selector=CLEAR_TEXT_FIELD_BUTTON_SELECTOR)
    add_to_cart_button = WebElement(css_selector=ADD_TO_CART_BUTTON_SELECTOR)
    add_to_cart_buttons = WebElements(css_selector=ADD_TO_CART_BUTTON_SELECTOR)
    header_cart_button = WebElement(css_selector=HEADER_CART_BUTTON_SELECTOR)

    def open_contacts_modal(self):
        self.scroll_up()
        self.contacts_button.click()
        if not self.contacts_modal.is_visible():
            raise Exception('Contacts modal view is not visible')

    def close_modal_view(self):
        self.close_button.click()
        self.contacts_modal.wait_until_not_visible()

    def click_clear_button(self):  # TODO: Need to look for specific text field
        self.clear_button.click()

    def click_contacts_button_with_text(self, text='Да'):
        self.answer_buttons.get_element_with_text(text).click()
        self.contacts_modal.wait_until_not_visible()

    def get_contacts_company_name(self):
        return self.company_name.get_text()

    def get_contacts_company_phone(self):
        return self.company_phone.get_text()

    def count_products(self):
        return self.add_to_cart_buttons.count()

    def open_cart_popup(self):
        self.scroll_up()
        self.header_cart_button.click()

    def add_to_cart_first_product(self):
        self.add_to_cart_button.scroll_to_element()
        self.add_to_cart_button.click()
