#!/usr/bin/python3
# -*- encoding=utf8 -*-

import pytest

from page_objects.pages.landing import Landing


def test_company_name(web_browser):
    company_name = 'ООО "Мокасы"'

    landing = Landing(web_browser)

    landing.open_contacts_modal()
    assert landing.get_contacts_company_name() == company_name


def test_company_phone(web_browser):
    company_phone = '+7 123 456-78-90'

    landing = Landing(web_browser)

    landing.open_contacts_modal()
    assert landing.get_contacts_company_phone() == company_phone


@pytest.mark.xfail(reason="Attribute is_displayed still returns true after element disappears")
def test_contacts_answer(web_browser):
    landing = Landing(web_browser)

    landing.open_contacts_modal()
    landing.click_contacts_button_with_text()
    assert not landing.contacts_modal.is_visible()


