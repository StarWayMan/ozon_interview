from page_objects.pages.base_page import WebPage
from page_objects.elements.base_element import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'http://petfriends1.herokuapp.com/login'
        super().__init__(web_driver, url)

    email = WebElement(id='email')

    password = WebElement(id='pass')

    btn = WebElement(class_name='btn.btn-success')
