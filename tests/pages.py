__author__ = 'anis'

import urlparse
from components import *


class Page(object):
    BASE_URL = 'https://target.mail.ru'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)


class AuthPage(Page):
    PATH = '/login'

    @property
    def form(self):
        return AuthForm(self.driver)


class CreatePage(Page):
    PATH = '/ads/create'

    @property
    def top_menu(self):
        return TopMenu(self.driver)

    @property
    def slider(self):
        return Slider(self.driver)

    @property
    def advertised_object(self):
        return AdvertisedObject(self.driver)

    @property
    def advert(self):
        return Advert(self.driver)

    @property
    def family_income(self):
        return FamilyIncome(self.driver)

    @property
    def professional_area(self):
        return ProfessionalArea(self.driver)

    @property
    def creating(self):
        return Creating(self.driver)


class CompaniesPage(Page):
    PATH = '/ads/campaigns/'

    @property
    def new_campaign(self):
        return NewCompany(self.driver)