import os
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Basic methods for tests composing: locating and handling web-elements, actions emulation (mouse clicking,
    dragging and dropping, moving to page elements)."""

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=15):
        self.scroll_to_element(self.element_is_present(locator))
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def action_drag_and_drop_by_offset(self, element, x_coords, y_coords):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coords, y_coords)
        action.perform()

    def action_drag_and_drop_to_element(self, what, where):
        action = ActionChains(self.driver)
        action.drag_and_drop(what, where)
        action.perform()

    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def action_click_and_hold(self, element):
        action = ActionChains(self.driver)
        action.click_and_hold(element)
        action.perform()

    def action_release(self, element):
        action = ActionChains(self.driver)
        action.release(element)
        action.perform()

    def js_script_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def extract_text_from_element(self, element):
        self.driver.execute_script("return arguments[0].textContent", element)

    def action_mouse_out_of_the_viewport(self):
        action = ActionChains(self.driver)
        action.move_by_offset(550, 550)
        action.perform()

    def latest_download_file(self):
        path = r'/Users/anton/Downloads'
        os.chdir(path)
        files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
        newest = files[-1]
        return newest

    def action_key_down(self):
        action = ActionChains(self.driver)
        action.key_down(Keys.TAB)
        action.perform()
