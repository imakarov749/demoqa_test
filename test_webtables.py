from selene.support.shared import browser
import pytest
from selene import be, have


# добавил фикстуры в основной тест, чтобы не приходилось по 100 раз менять урлы
# открываем браузер, проверяем корректность url закрываем после теста
@pytest.fixture()
def demo_qa_open_browser():
    browser.config.hold_browser_open = True
    browser.config.base_url = 'https://demoqa.com'
    browser.open('/webtables')

    # проверяем, что открытый url корректный
    browser.should(have.url('https://demoqa.com/webtables'))
    browser.element('.main-header').should(be.visible)
    yield
    browser.close()


# задаем конфигурацию браузера
@pytest.fixture(autouse=True)
def browser_configure(demo_qa_open_browser):
    browser.driver.set_window_size(1920, 1080)


def test_change_table():
    # открываем форму для добавления строки
    browser.element('#addNewRecordButton').click()

    # заполняем поля в форме
    browser.element('#firstName').should(be.blank).click().type('Ivan')
    browser.element('#lastName').should(be.blank).click().type('Ivanov')
    browser.element('#userEmail').should(be.blank).click().type('ivanov@ivan.com')
    browser.element('#age').should(be.blank).click().type('190')
    browser.element('#salary').should(be.blank).click().type('1900')
    browser.element('#department').should(be.blank).click().type('Department of magic')

    # нажимаем на кнопку добавления строки, закрываем форму
    browser.element('#submit').click()

    # проверяем, что строка добавилась, так и не понял, как проверить через css-селектор
    # хотел посчитать элементы, чтобы выбрать нужный, но тоже не разобрался

    check_added_email_by_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[4]'
    browser.element(check_added_email_by_xpath).should(have.text('ivanov@ivan.com'))
    # browser.config.timeout = 10
    # browser.element('[class^=ReactTable]').element('.rt-tbody').all('[class$=-even]').should(have.size(5))
    # text('ivanov@ivan.com'))
    # browser.element('#edit-record-4').element('..').should(have.text('ivanov@ivan.com'))

    # открываем pop up для редактирования второй строки
    browser.element('#edit-record-2').click()

    # редактируем поля во второй строке
    browser.element('#firstName').click().clear().type('Elden')
    browser.element('#lastName').click().clear().type('Ring')
    browser.element('#userEmail').click().clear().type('elden_will_be_grea@1.com')
    browser.element('#age').click().clear().type('23')
    browser.element('#salary').click().clear().type('190000')
    browser.element('#department').click().clear().type('Interearth')

    # сохраняем изменения
    browser.element('#submit').click()

    # удаляем третью строку
    browser.element('#delete-record-3').click()
