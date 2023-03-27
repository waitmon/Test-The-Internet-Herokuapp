import random
import time
from selenium.common import UnexpectedAlertPresentException

from locators import PageLocators
from pages.base_page import BasePage


class AddRemoveElements(BasePage):
    locators = PageLocators()

    def check_add_element(self):
        self.element_is_present(self.locators.ADD_ELEMENT).click()
        added_element = self.element_is_present(self.locators.DELETE_ELEMENT)
        added_element_option = added_element.get_attribute('class')
        assert 'added-manually' in added_element_option

    def check_remove_element(self):
        self.element_is_present(self.locators.ADD_ELEMENT).click()
        added_element = self.element_is_present(self.locators.DELETE_ELEMENT)
        added_element.click()
        assert self.element_is_not_visible(added_element)


class BasicAuth(BasePage):
    locators = PageLocators()

    def check_success_authorization(self):
        auth_message = self.element_is_present(self.locators.SUCCESSFUL_AUTH).text
        return auth_message


class BrokenImages(BasePage):
    locators = PageLocators()

    def check_broken_images(self):
        images_list = self.elements_are_present(self.locators.IMAGES_LIST)
        images_status = []
        for image in images_list:
            image_status = image.get_attribute('naturalWidth')
            images_status.append(image_status)
            assert '0' in images_status

    def check_correct_image(self):
        image = self.element_is_present(self.locators.VALID_IMAGE)
        image_status = image.get_attribute('naturalWidth')
        assert image_status != 0


class Checkboxes(BasePage):
    locators = PageLocators()

    def check_checked_checkboxes(self):
        checkboxes = [self.locators.CHECKBOX_LIST]
        self.element_is_present(random.choice(checkboxes)).click()
        selected_checkboxes = []
        checkboxes_selected = self.elements_are_present(self.locators.CHECKED_STATUS)
        for checkbox in checkboxes_selected:
            checkbox_checked = checkbox.get_attribute('value')
            selected_checkboxes.append(checkbox_checked)
        assert 'on' in selected_checkboxes


class ContextMenu(BasePage):
    locators = PageLocators()

    def check_right_click(self):
        self.action_right_click(self.element_is_present(self.locators.CONTEXT_MENU))
        try:
            alert_window = self.driver.switch_to.alert
            return alert_window.text
        except UnexpectedAlertPresentException:
            alert_window = self.driver.switch_to.alert
            return alert_window.text


class DisappearingElements(BasePage):
    locators = PageLocators()

    def check_element_visibility(self):
        elements_qty_before_refreshing = self.elements_are_present(self.locators.ELEMENTS)
        self.driver.refresh()
        elements_qty_after_refreshing = self.elements_are_present(self.locators.ELEMENTS)
        assert elements_qty_before_refreshing != elements_qty_after_refreshing


class DragAndDrop(BasePage):
    locators = PageLocators()

    def get_before_and_after_position(self, drag_element):
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0, 50), random.randint(0, 50))
        before_position = drag_element.get_attribute('style')
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0, 50), random.randint(0, 50))
        after_position = drag_element.get_attribute('style')
        return before_position, after_position

    def check_drag_box_moving(self):
        drag_box = self.element_is_visible(self.locators.COLUMN_A)
        before_position, after_position = self.get_before_and_after_position(drag_box)
        return before_position, after_position


class DropdownList(BasePage):
    locators = PageLocators()

    def check_first_option_selected(self):
        option = self.element_is_present(self.locators.OPTION_1)
        option.click()
        assert option.is_selected()

    def check_second_option_selected(self):
        option = self.element_is_present(self.locators.OPTION_2)
        option.click()
        assert option.is_selected()


class DynamicContent(BasePage):
    locators = PageLocators()

    def check_content_changing(self):
        content_before_refreshing = self.elements_are_present(self.locators.PAGE_CONTENT)
        self.driver.refresh()
        content_after_refreshing = self.elements_are_present(self.locators.PAGE_CONTENT)
        assert content_before_refreshing != content_after_refreshing

    def check_static_content(self):
        self.element_is_present(self.locators.STATIC_BUTTON).click()
        content_before_refreshing = [self.element_is_present(self.locators.COLUMN_1),
                                     self.element_is_present(self.locators.COLUMN_2)]
        self.driver.refresh()
        content_after_refreshing = [self.element_is_present(self.locators.COLUMN_1),
                                    self.element_is_present(self.locators.COLUMN_2)]
        assert content_before_refreshing != content_after_refreshing


class DynamicControls(BasePage):
    locators = PageLocators()

    def check_checkbox_remove(self):
        checkbox = self.element_is_present(self.locators.CHECKBOX_LIST)
        self.element_is_present(self.locators.ACTION_BUTTON).click()
        button_msg = self.element_is_present(self.locators.BUTTON_MESSAGE).text
        assert self.element_is_not_visible(checkbox) and button_msg == "It's gone!"

    def check_checkbox_appear(self):
        checkbox = self.element_is_present(self.locators.CHECKBOX_LIST)
        self.element_is_present(self.locators.ACTION_BUTTON).click()
        self.element_is_not_visible(checkbox)
        self.element_is_present(self.locators.ACTION_BUTTON).click()
        checkbox_appear = self.element_is_present(self.locators.CHECKBOX_APPEAR)
        button_msg = self.element_is_visible(self.locators.BUTTON_MESSAGE).text
        assert checkbox_appear.is_displayed() and button_msg == "It's back!"

    def check_enable_input(self):
        self.element_is_present(self.locators.ENABLE_DISABLE).click()
        input_field = self.element_is_clickable(self.locators.INPUT_FIELD)
        input_field.click()
        input_field.send_keys('test')
        # self.element_is_present(self.locators.ENABLE_DISABLE).click()
        # input_status = input_field.get_attribute('disabled')
        # print(input_status)
