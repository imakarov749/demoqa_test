from selene.support.shared import browser
from selenium.webdriver import Keys
from selene import be, have
import os, re

from model.controls import dropdown, modal


def set_first_name(name):
    browser.element('#firstName').should(be.blank).type(name)


def set_last_name(last_name):
    browser.element('#lastName').should(be.blank).type(last_name)


def set_email(email):
    browser.element('#userEmail').should(be.blank).type(email)


def choose_gender():
    browser.element("[for='gender-radio-1']").click()


def set_phone_number(phone_number):
    browser.element('#userNumber').should(be.blank).type(phone_number)


def choose_birth_date_from_calendar():
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('[value="11"]').click()
    browser.element('.react-datepicker__year-select').click().element('[value="1912"]').click()
    browser.element('.react-datepicker__day--012').click()


# v2.можно ввести дату рождения вручную
# def set_birth_from_controls(birth_for_type):
# birth_for_type = '12 Dec 1912' - больше не нужна, но я оставлю для второго варианта ввода даты рождения
# birth = browser.element('#dateOfBirthInput').click()
# birth.clear().set_value(birth_for_type).press_enter()
# birth.send_keys(Keys.CONTROL + 'a').type(birth_for_type).press_enter()

def choose_hobbies():
    browser.element("[for='hobbies-checkbox-1']").click()


def set_address(address_for_type):
    browser.element('#currentAddress').should(be.blank).type(address_for_type)


def set_subject(subject):
    browser.element('#subjectsInput').should(be.blank).type(subject).press_enter()


def upload_image():
    file_path = os.path.abspath("resources/photo_image.jpg")
    browser.element('#uploadPicture').send_keys(file_path)


def choose_state(value):
    dropdown.select(browser.element('#state'), value)


def choose_city(value):
    dropdown.select(browser.element('#city'), value)


def click_submitting_button():
    browser.element('#submit').click()


def check_open_submitting_window():
    browser.element('#example-modal-sizes-title-lg').should(be.visible).should(
        have.text('Thanks for submitting the form'))


def close_submitting_window():
    browser.element('#closeLargeModal').click()


def check_fields_in_submitting_window(data):
    rows = modal.dialog.all('tbody tr')
    for row, value in data:
        rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))
