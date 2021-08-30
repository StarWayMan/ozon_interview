#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os
from typing import Final
from page_objects.pages.base_page import WebPage


class Landing(WebPage):

    LANDING_URL: Final = 'https://mokasi.turbo.site/mokasi'

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or Landing.LANDING_URL

        super().__init__(web_driver, url)

