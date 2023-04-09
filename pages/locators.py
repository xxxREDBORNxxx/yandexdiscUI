from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_LINK = (By.CSS_SELECTOR, '.user-account[aria-label="Аккаунт"]')
    LOGOUT_LINK = (By.XPATH, '//li[@class="menu__list-item"]/a/span[contains(text(), "Выйти")]')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "a.home-link2.headline__personal-enter.home-link2_color_black")
    USER_MENU = (By.CSS_SELECTOR, 'span.avatar__image-wrapper')
    DISK_LINK = (By.XPATH, '//span[contains(text(), "Диск")]')


class LoginPageLocators:
    MAIL_LINK = (By.CSS_SELECTOR, 'button[data-type="login"]')
    EMAIL = (By.CSS_SELECTOR, 'input#passp-field-login[name="login"]')
    PASSWORD = (By.CSS_SELECTOR, 'input#passp-field-passwd[name="passwd"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button#passp\\:sign-in[type="submit"]')


class DiskPageLocators:
    CREATE_LINK = (By.CSS_SELECTOR, 'button.Button2.Button2_view_raised.Button2_size_m.Button2_width_max')
    UPLOAD_LINK = (By.CSS_SELECTOR, 'input[type="file"].upload-button__attach')

    CREATE_FOLDER_LINK = (By.CSS_SELECTOR, 'button.create-resource-button[aria-label="Папку"]')
    INPUT_FOLDER_NAME_LINK = (By.CSS_SELECTOR, 'span.Textinput input[text="Новая папка"]')
    SAVE_FOLDER_NAME_BUTTON = (By.CSS_SELECTOR, '.confirmation-dialog__footer button[type="button"]')

    OPEN_FOLDER_LINK = (By.CSS_SELECTOR, '.listing-item__info [aria-label={}]')

    UPLOAD_STATUS = (By.XPATH, '//h3[contains(text(), "Все файлы загружены")]')
    CLOSE_UPLOAD_TABLE = (By.CSS_SELECTOR, '.uploader-progress__controls button[aria-label="Закрыть"]')
    FIND_FILE_LINK = (By.CSS_SELECTOR, '.listing-item_type_file .listing-item__info [aria-label="{}"]')

    CONTEXT_RENAME_LINK = (By.CSS_SELECTOR, '.resources-actions-popup__wrapper [value="rename"]')
    INPUT_FILE_NAME = (By.CSS_SELECTOR, '.Modal-Content input')
    SAVE_FILE_NAME_BUTTON = (By.CSS_SELECTOR, '.Modal-Content .confirmation-dialog__footer button')

