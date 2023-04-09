import os
import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.disk_page import YadiskPage


@pytest.mark.ui
@pytest.mark.parametrize('folder_name, file_name, new_file_name',
                         [('test_ui', 'UI_workfile.pdf', 'UI_workfile_new.pdf')])
def test_task_ui_yandex_disk(browser, action, login, password, folder_name, file_name, new_file_name):
    """
    Описание теста по заданию в файле UI_workfile.pdf
    Перед запуском теста необходимо:ь
     1. проверить, что папка folder_name: 'test_ui_8' отсутствует на яндекс-диске,
    т.к. тест уйдет в except при попытке создания файла с тем же именем.
     2. или изменить имя папки в parametrize.
    Это сделано для защиты от переполнения диска, т.к. отсутствует метод удаления создаваемых ресурсов.

    """
    page = MainPage(browser, action)
    page.open()
    page.go_to_login_page()

    login_page = LoginPage(browser, action)
    login_page.login(login, password)

    page.get_user_menu()
    page.go_to_disk_page(1)

    yadisk_page = YadiskPage(browser, action)
    yadisk_page.create_folder(folder_name)
    yadisk_page.open_folder(folder_name)
    yadisk_page.upload_resource(f'{os.getcwd()}\\{file_name}')
    yadisk_page.status_upload()
    yadisk_page.rename_file(file_name, new_file_name)
    yadisk_page.find_file(new_file_name)

    page.logout_user()
