#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from page_objects.pages.base_page import WebPage
from page_objects.elements.base_element import WebElement
from page_objects.elements.base_element import WebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://market.yandex.ru/'

        super().__init__(web_driver, url)

    # Main search field
    search = WebElement(id='header-search')

    # Search button
    search_run_button = WebElement(xpath='//button[@type="submit"]')

    # Titles of the products in search results
    products_titles = WebElements(xpath='//a[contains(@href, "/product-") and @title!=""]')

    # Button to sort products by price
    sort_products_by_price = WebElement(css_selector='button[data-autotest-id="dprice"]')

    # Prices of the products in search results
    products_prices = WebElements(xpath='//div[@data-zone-name="price"]//span/*[1]')
