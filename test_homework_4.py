def func_text(func_name, *args):
    func_name = func_name.__name__.replace("_", " ").title()
    print(func_name, *args)


def open_browser(browser_name):
    func_text(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    func_text(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    func_text(find_registration_button_on_login_page, page_url, button_text)


open_browser(browser_name="In you PC (Recommendation Firefox or Chrome)")
go_to_companyname_homepage(page_url="https://www.blizzard.com/ru-ru/")
find_registration_button_on_login_page(page_url="https://eu.battle.net/login/ru/", button_text="Registration")
