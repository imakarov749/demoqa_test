from selene.support.shared import browser
from selenium.webdriver import Keys
from selene import be, have
import os, re


def test_fill_form():
    # зададим переменные для теста
    # надеюсь, что это не избыточно
    f_name_for_type = 'Ivan'
    l_name_for_type = 'Ivanov'
    email_for_type = 'ivan.ivanov@kljh.com'
    number_for_type = '7123456789'
    birth_for_type = '12 Dec 1912'
    adress_for_type = 'Moscow'
    file_path = os.path.abspath("files_for_test/photo_image.jpg")

    # вводим имя
    first_name = browser.element('#firstName')
    first_name.should(be.blank).type(f_name_for_type)

    # вводим фамилию
    last_name = browser.element('#lastName')
    last_name.should(be.blank).type(l_name_for_type)

    # вводим email
    email = browser.element('#userEmail')
    email.should(be.blank).type(email_for_type)

    # выбираем пол
    input_gender = browser.element("[for='gender-radio-1']")
    input_gender.click()

    # вводим номер телефона
    number = browser.element('#userNumber')
    number.should(be.blank).type(number_for_type)

    # вводим дату рождения
    birth = browser.element('#dateOfBirthInput')
    # тут мб зря использовал Keys, но через clear не получилось
    # birth.clear().set_value('12 Dec 1912').press_enter()
    birth.send_keys(Keys.CONTROL + 'a').type(birth_for_type).press_enter()

    # выбираем хобби
    checkbox_hobbies = browser.element("[for='hobbies-checkbox-1']")
    checkbox_hobbies.click()

    # вводим адрес
    adress = browser.element('#currentAddress')
    adress.should(be.blank).type(adress_for_type)

    # выбираем предмет
    subject = browser.element('#subjectsInput')
    subject.should(be.blank).type('Math').press_enter()

    # загружаем фото
    upload_picture_input = browser.element('#uploadPicture')
    upload_picture_input.send_keys(file_path)

    # выбираем штат
    state_dropdown = browser.element('#react-select-3-input')
    state_dropdown.type('NCR').press_enter()

    # выбираем город
    sity_dropdown = browser.element('#react-select-4-input')
    sity_dropdown.type('Del').press_enter()

    # нажимаем кнопку подтверждения
    submit = browser.element('#submit')
    submit.click()

    submitting_window = browser.element('#example-modal-sizes-title-lg')
    submitting_window.should(be.visible).should(have.text('Thanks for submitting the form'))

    def test_check_form():
        check_fields = browser.element('.table-responsive')
        check_fields.should(have.text(f_name_for_type))
        check_fields.should(have.text(l_name_for_type))
        check_fields.should(have.text(email_for_type))
        check_fields.should(have.text('Male'))
        check_fields.should(have.text(number_for_type))

        # проверяем дату
        # все равно) как текст - это просто указать текст, который мы ожидаем, в проверке но!
        # кажется, что правильнее было бы запоминать то, что ввели в начале, а потом искать по частичному совпадению
        check_fields.re.findall(birth_for_type)
        check_fields.should(have.text('12December,1912'))

        check_fields.should(have.text('photo_image.jpg'))

    close_button = browser.element('#closeLargeModal')
    close_button.click()
