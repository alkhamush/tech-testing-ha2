# coding=utf-8
__author__ = 'anis'

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By


def find_element(driver, css_selector):
    return (WebDriverWait(driver, 30, 1).until(
        lambda d: d.find_element_by_css_selector(css_selector)
    ))


def find_elements(driver, css_selector):
    return (WebDriverWait(driver, 30, 1).until(
        lambda d: d.find_elements_by_css_selector(css_selector)
    ))


def find_element_by_xpath(driver, css_selector):
    return (WebDriverWait(driver, 30, 1).until(
        lambda d: d.find_element_by_xpath(css_selector)
    ))


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class AuthForm(Component):
    LOGIN = '#id_Login'
    PASSWORD = '#id_Password'
    DOMAIN = '#id_Domain'
    SUBMIT = '#gogogo>input'

    def set_login(self, login):
        self.driver.find_element_by_css_selector(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_css_selector(self.PASSWORD).send_keys(pwd)

    def set_domain(self, domain):
        select = self.driver.find_element_by_css_selector(self.DOMAIN)
        Select(select).select_by_visible_text(domain)

    def submit(self):
        self.driver.find_element_by_css_selector(self.SUBMIT).click()


class TopMenu(Component):
    EMAIL = '#PH_user-email'

    def get_email(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.EMAIL).text
        )


class Slider(Component):
    SLIDER = '.price-slider__begunok'

    def move(self, offset):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.SLIDER)
        )
        ac = ActionChains(self.driver)
        ac.click_and_hold(element).move_by_offset(offset, 0).perform()


class AdvertisedObject(Component):
    COMPANY = '.base-setting__campaign-name__input'
    ADVERTISING_TYPE = 'product-type-5205'
    ADVERTISING_FIELD = 'pad-social_abstact'

    def set_company(self, company_name):
        company = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.COMPANY)
        )
        company.clear()
        company.send_keys(company_name)

    def set_advertis_type(self):
        advertis_type = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.ADVERTISING_TYPE)
        )
        advertis_type.click()

    def set_advertis_field(self):
        advertis_type = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.ADVERTISING_FIELD)
        )
        advertis_type.click()


class Advert(Component):
    TITLE = ".banner-form__input[data-name='title']"
    TEXT = ".banner-form__input[data-name='text']"
    URL = ".banner-form__input[data-name='url']"
    IMAGE = ".banner-form__input[data-name='image']"

    VALUE_TITLE = "/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div[3]/div/div[1]/div/div/div[1]/span/span[1]"
    # VALUE_TEXT
    # VALUE_URL

    def set_title(self, title_name):
        title_field = find_element(self.driver, self.TITLE)
        title_field.send_keys(title_name)

    def set_text(self, text):
        text_field = find_element(self.driver, self.TEXT)
        text_field.send_keys(text)

    def set_url(self, url):
        url_field = find_elements(self.driver, self.URL)
        url_field[1].send_keys(url)

    def set_image(self, image):
        image_field = find_element(self.driver, self.IMAGE)
        image_field.send_keys(image)

    def get_title(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.VALUE_TITLE).text
        )


    def get_text(self):
        text_field = find_element(self.driver, self.TEXT)
        return text_field.text

    def get_url(self):
        url_field = find_elements(self.driver, self.URL)
        return url_field[1].text


class FamilyIncome(Component):

    FAMILY_INCOME = "[data-valid-flag='income_group'] [data-name='income_group'] .campaign-setting__value"
    HIGH = "input#income_group-9288.campaign-setting__input.js-setting-input"
    MEDIUM = "input#income_group-9287.campaign-setting__input.js-setting-input"
    LOW = "input#income_group-9286.campaign-setting__input.js-setting-input"

    def click_on_family_income(self):
        family_income = find_element(self.driver, self.FAMILY_INCOME)
        family_income.click()

    def click_on_high(self):
        high = find_element(self.driver, self.HIGH)
        high.click()

    def click_on_medium(self):
        medium = find_element(self.driver, self.MEDIUM)
        medium.click()

    def click_on_low(self):
        low = find_element(self.driver, self.LOW)
        low.click()

    def get_high(self):
        high = find_element(self.driver, self.HIGH)
        return high.is_selected()

    def get_medium(self):
        medium = find_element(self.driver, self.MEDIUM)
        return medium.is_selected()

    def get_low(self):
        low = find_element(self.driver, self.LOW)
        return low.is_selected()


class ProfessionalArea(Component):

    INTERESTS = "[data-node-id='interests']"
    PROFESSIONAL_AREA = "[data-node-id='Профессиональнаяобласть']"
    ALL_PROFESSIONAL_AREA = "//*[@id='interests237']/input"
    BANKS = "//*[@id='interests241']/input"

    def click_on_interests(self):
        interests = find_element(self.driver, self.INTERESTS)
        interests.click()

    def click_on_professional_area(self):
        professional_area = find_element(self.driver, self.PROFESSIONAL_AREA)
        professional_area.click()

    def click_on_all_professional_area(self):
        all_professional_area = find_element_by_xpath(self.driver, self.ALL_PROFESSIONAL_AREA)
        all_professional_area.click()

    def click_on_all_banks(self):
        banks = find_element_by_xpath(self.driver, self.BANKS)
        banks.click()

    def get_professional_area(self):
        professional_area = find_element(self.driver, self.PROFESSIONAL_AREA)
        return professional_area.is_selected()

    def get_all_professional_area(self):
        all_professional_area = find_element_by_xpath(self.driver, self.ALL_PROFESSIONAL_AREA)
        return all_professional_area.is_selected()

    def get_all_banks(self):
        banks = find_element_by_xpath(self.driver, self.BANKS)
        return banks.is_selected()


class Creating(Component):

    CREATING_BUTTON = ".main-button-new"

    def create(self):
        creating_button = find_element(self.driver, self.CREATING_BUTTON)
        creating_button.click()




