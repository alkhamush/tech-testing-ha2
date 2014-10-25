__author__ = 'anis'

import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from pages import AuthPage, CreatePage


class Test(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_email(self):
        USERNAME = 'tech-testing-ha2-33@bk.ru'
        PASSWORD = os.environ['TTHA2PASSWORD']
        DOMAIN = '@bk.ru'

        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_domain(DOMAIN)
        auth_form.set_login(USERNAME)
        auth_form.set_password(PASSWORD)
        auth_form.submit()

        create_page = CreatePage(self.driver)
        create_page.open()
        email = create_page.top_menu.get_email()


        create_page.advert.set_title('test_headline')
        create_page.advert.set_text('test_text')
        create_page.advert.set_url('http://www.vlad.aif.ru/culture/details/1367981')
        create_page.advert.set_image("img.jpg")

        create_page.professional_area.click_on_interests()
        create_page.professional_area.click_on_professional_area()
        create_page.professional_area.click_on_all_banks()

        create_page.family_income.click_on_family_income()
        create_page.family_income.click_on_high()
        create_page.family_income.click_on_medium()
        create_page.family_income.click_on_low()

        create_page.creating.create()

        self.assertEqual(USERNAME, email)

    def test_family_income1(self):
        USERNAME = 'tech-testing-ha2-33@bk.ru'
        PASSWORD = os.environ['TTHA2PASSWORD']
        DOMAIN = '@bk.ru'

        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_domain(DOMAIN)
        auth_form.set_login(USERNAME)
        auth_form.set_password(PASSWORD)
        auth_form.submit()

        create_page = CreatePage(self.driver)
        create_page.open()

        create_page.advert.set_title('test_headline')
        create_page.advert.set_text('test_text')
        create_page.advert.set_url('http://www.vlad.aif.ru/culture/details/1367981')
        create_page.advert.set_image("img.jpg")

        create_page.professional_area.click_on_interests()
        create_page.professional_area.click_on_professional_area()
        create_page.professional_area.click_on_all_banks()

        create_page.family_income.click_on_family_income()
        create_page.family_income.click_on_high()
        create_page.family_income.click_on_medium()
        create_page.family_income.click_on_low()

        assert create_page.family_income.get_high()
        assert create_page.family_income.get_medium()
        assert create_page.family_income.get_low()

        create_page.creating.create()

    def test_family_income2(self):
        USERNAME = 'tech-testing-ha2-33@bk.ru'
        PASSWORD = os.environ['TTHA2PASSWORD']
        DOMAIN = '@bk.ru'

        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_domain(DOMAIN)
        auth_form.set_login(USERNAME)
        auth_form.set_password(PASSWORD)
        auth_form.submit()

        create_page = CreatePage(self.driver)
        create_page.open()

        create_page.advert.set_title('test_headline')
        create_page.advert.set_text('test_text')
        create_page.advert.set_url('http://www.vlad.aif.ru/culture/details/1367981')
        create_page.advert.set_image("img.jpg")

        create_page.professional_area.click_on_interests()
        create_page.professional_area.click_on_professional_area()
        create_page.professional_area.click_on_all_banks()

        create_page.family_income.click_on_family_income()
        create_page.family_income.click_on_medium()
        create_page.family_income.click_on_low()

        assert not create_page.family_income.get_high()
        assert create_page.family_income.get_medium()
        assert create_page.family_income.get_low()

        create_page.creating.create()

    def test_professional_area1(self):
        USERNAME = 'tech-testing-ha2-33@bk.ru'
        PASSWORD = os.environ['TTHA2PASSWORD']
        DOMAIN = '@bk.ru'

        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_domain(DOMAIN)
        auth_form.set_login(USERNAME)
        auth_form.set_password(PASSWORD)
        auth_form.submit()

        create_page = CreatePage(self.driver)
        create_page.open()

        create_page.advert.set_title('test_headline')
        create_page.advert.set_text('test_text')
        create_page.advert.set_url('http://www.vlad.aif.ru/culture/details/1367981')
        create_page.advert.set_image("img.jpg")

        create_page.professional_area.click_on_interests()
        create_page.professional_area.click_on_professional_area()
        create_page.professional_area.click_on_all_banks()

        create_page.family_income.click_on_family_income()
        create_page.family_income.click_on_high()
        create_page.family_income.click_on_medium()
        create_page.family_income.click_on_low()

        assert create_page.professional_area.get_all_banks()

        create_page.creating.create()

    def test_professional_area2(self):
        USERNAME = 'tech-testing-ha2-33@bk.ru'
        PASSWORD = os.environ['TTHA2PASSWORD']
        DOMAIN = '@bk.ru'

        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_domain(DOMAIN)
        auth_form.set_login(USERNAME)
        auth_form.set_password(PASSWORD)
        auth_form.submit()

        create_page = CreatePage(self.driver)
        create_page.open()

        create_page.advert.set_title('test_headline')
        create_page.advert.set_text('test_text')
        create_page.advert.set_url('http://www.vlad.aif.ru/culture/details/1367981')
        create_page.advert.set_image("img.jpg")

        create_page.professional_area.click_on_interests()
        create_page.professional_area.click_on_professional_area()
        create_page.professional_area.click_on_all_professional_area()

        create_page.family_income.click_on_family_income()
        create_page.family_income.click_on_high()
        create_page.family_income.click_on_medium()
        create_page.family_income.click_on_low()

        assert create_page.professional_area.get_all_professional_area()
        assert create_page.professional_area.get_all_banks()

        create_page.creating.create()

