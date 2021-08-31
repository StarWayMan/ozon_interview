#!/usr/bin/python3
# -*- encoding=utf8 -*-

import pytest

from page_objects.pages.landing import Landing


def test_count_products(web_browser):
    number_of_products = 3

    landing = Landing(web_browser)

    assert landing.count_products() == number_of_products


def test_adding_products(web_browser):
    landing = Landing(web_browser)

    landing.add_to_cart_first_product()
    landing.open_cart_popup()
    landing.screenshot()
    #  TODO: Add screenshot comparison
