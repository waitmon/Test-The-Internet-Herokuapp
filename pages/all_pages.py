import random
import string
import time

import pyautogui
import requests
from selenium.common import UnexpectedAlertPresentException
from selenium.webdriver import Keys

from src.locators import PageLocators
from pages.base_page import BasePage
import allure


class AddRemoveElements(BasePage):
    locators = PageLocators()

    @allure.step('Check if element has been added')
    def check_add_element(self):
        with allure.step('clicking remove button'):
            self.element_is_present(self.locators.ADD_ELEMENT).click()
            added_element = self.element_is_present(self.locators.DELETE_ELEMENT)
            added_element_option = added_element.get_attribute('class')
        assert 'added-manually' in added_element_option, 'Element was not added'

    @allure.step('Check if element has been deleted')
    def check_remove_element(self):
        with allure.step('clicking add and delete buttons'):
            self.element_is_present(self.locators.ADD_ELEMENT).click()
            added_element = self.element_is_present(self.locators.DELETE_ELEMENT)
            added_element.click()
        assert self.element_is_not_visible(added_element), 'Element was not deleted'


class BasicAuth(BasePage):
    locators = PageLocators()

    @allure.step('Check if credentials sent are correct')
    def check_success_authorization(self):
        auth_message = self.element_is_present(self.locators.SUCCESSFUL_AUTH).text
        return auth_message


class BrokenImages(BasePage):
    locators = PageLocators()

    @allure.step('Check if both images are not displayed')
    def check_broken_images(self):
        with allure.step('Locating both broken images on the page'):
            images_list = self.elements_are_present(self.locators.IMAGES_LIST)
            images_status = []
            with allure.step('Looping through the images attributes, searching for 0 width values'):
                for image in images_list:
                    image_status = image.get_attribute('naturalWidth')
                    images_status.append(image_status)
                    assert '0' in images_status, 'Broken images displayed'

    @allure.step('Check if image is displayed')
    def check_correct_image(self):
        image = self.element_is_present(self.locators.VALID_IMAGE)
        with allure.step('Getting image attribute, searching for non null width values'):
            image_status = image.get_attribute('naturalWidth')
        assert image_status != 0, 'Correct image did not display'


class Checkboxes(BasePage):
    locators = PageLocators()

    @allure.step('Check if checkboxes are available for being checked')
    def check_checked_checkboxes(self):
        with allure.step('Locating elements on the page, randomly clicking one of them'):
            checkboxes = [self.locators.CHECKBOX_LIST]
            self.element_is_present(random.choice(checkboxes)).click()
            with allure.step('Looping through attributes after clicking, searching for values refers to checked '
                             'statement'):
                selected_checkboxes = []
                checkboxes_selected = self.elements_are_present(self.locators.CHECKED_STATUS)
                for checkbox in checkboxes_selected:
                    checkbox_checked = checkbox.get_attribute('value')
                    selected_checkboxes.append(checkbox_checked)
        assert 'on' in selected_checkboxes, 'Checkboxes were not selected'


class ContextMenu(BasePage):
    locators = PageLocators()

    @allure.step('Check the appearance of js alert')
    def check_right_click(self):
        with allure.step('Performing right clicking, extracting alert message'):
            self.action_right_click(self.element_is_present(self.locators.CONTEXT_MENU))
            try:
                alert_window = self.driver.switch_to.alert
                return alert_window.text
            except UnexpectedAlertPresentException:
                alert_window = self.driver.switch_to.alert
                return alert_window.text


class DisappearingElements(BasePage):
    locators = PageLocators()

    @allure.step('Check elements visibility after each page reloading')
    def check_element_visibility(self):
        elements_qty_before_refreshing = self.elements_are_present(self.locators.ELEMENTS)
        self.driver.refresh()
        elements_qty_after_refreshing = self.elements_are_present(self.locators.ELEMENTS)
        assert elements_qty_before_refreshing != elements_qty_after_refreshing, 'Quantity of elements did not changed ' \
                                                                                'after page reloading'


class DragAndDrop(BasePage):
    locators = PageLocators()

    def get_before_and_after_position(self, drag_element):
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0, 50), random.randint(0, 50))
        before_position = drag_element.get_attribute('style')
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0, 50), random.randint(0, 50))
        after_position = drag_element.get_attribute('style')
        return before_position, after_position

    @allure.step('Performing moving of Column A with an usage of drag and drop action')
    def check_drag_box_moving(self):
        drag_box = self.element_is_visible(self.locators.COLUMN_A)
        before_position, after_position = self.get_before_and_after_position(drag_box)
        return before_position, after_position, 'Drag box did not move'


class DropdownList(BasePage):
    locators = PageLocators()

    @allure.step('Selecting option 1')
    def check_first_option_selected(self):
        option = self.element_is_present(self.locators.OPTION_1)
        option.click()
        assert option.is_selected(), 'First option was not selected'

    @allure.step('Selecting option 2')
    def check_second_option_selected(self):
        option = self.element_is_present(self.locators.OPTION_2)
        option.click()
        assert option.is_selected(), 'Second option was not selected'


class DynamicContent(BasePage):
    locators = PageLocators()

    @allure.step('Refreshing page / checking text contents both before and after refreshing')
    def check_content_changing(self):
        content_before_refreshing = self.elements_are_present(self.locators.PAGE_CONTENT)
        self.driver.refresh()
        content_after_refreshing = self.elements_are_present(self.locators.PAGE_CONTENT)
        assert content_before_refreshing != content_after_refreshing, 'Content did not change after page reloading'

    @allure.step('Pressing static button / checking that text contents are being static after page refreshing')
    def check_static_content(self):
        self.element_is_present(self.locators.STATIC_BUTTON).click()
        content_before_refreshing = [self.element_is_present(self.locators.COLUMN_1),
                                     self.element_is_present(self.locators.COLUMN_2)]
        self.driver.refresh()
        content_after_refreshing = [self.element_is_present(self.locators.COLUMN_1),
                                    self.element_is_present(self.locators.COLUMN_2)]
        assert content_before_refreshing != content_after_refreshing, 'Some of the content did not turn to static'


class DynamicControls(BasePage):
    locators = PageLocators()

    @allure.step('Clicking Remove button / verifying checkbox is not visible')
    def check_checkbox_remove(self):
        checkbox = self.element_is_present(self.locators.CHECKBOX_LIST)
        self.element_is_present(self.locators.ACTION_BUTTON).click()
        button_msg = self.element_is_present(self.locators.BUTTON_MESSAGE).text
        assert self.element_is_not_visible(checkbox) and button_msg == "It's gone!", 'Checkbox was not remove'

    @allure.step('Clicking add button / verifying checkbox is visible again')
    def check_checkbox_appear(self):
        checkbox = self.element_is_present(self.locators.CHECKBOX_LIST)
        self.element_is_present(self.locators.ACTION_BUTTON).click()
        self.element_is_not_visible(checkbox)
        self.element_is_present(self.locators.ACTION_BUTTON).click()
        checkbox_appear = self.element_is_present(self.locators.CHECKBOX_APPEAR)
        button_msg = self.element_is_visible(self.locators.BUTTON_MESSAGE).text
        assert checkbox_appear.is_displayed() and button_msg == "It's back!", 'Checkbox did not display'

    @allure.step('Clicking enable button / Verifying input field is enabled')
    def check_enable_input(self):
        self.element_is_present(self.locators.ENABLE_DISABLE).click()
        input_field = self.element_is_clickable(self.locators.INPUT_FIELD)
        input_field.click()
        input_field.send_keys('test')
        assert input_field.is_enabled(), 'Input field is disabled'

    @allure.step('Clicking disable button / Verifying input field is disabled')
    def check_disable_input(self):
        input_field = self.element_is_present(self.locators.INPUT_FIELD)
        assert input_field.get_attribute('disabled'), 'Input field is enabled'


class DynamicLoading(BasePage):
    locators = PageLocators()

    @allure.step('Check that element is rendered after pressing start button')
    def check_element_is_rendered_after_click(self):
        self.element_is_present(self.locators.START_BUTTON).click()
        hidden_element = self.element_is_visible(self.locators.HIDDEN_TEXT)
        assert hidden_element.is_displayed(), 'Hidden element did not display'


class EntryAd(BasePage):
    locators = PageLocators()

    @allure.step('Checking that modal window appears on a page load')
    def check_entry_ad_content(self):
        modal_title = self.element_is_visible(self.locators.MODAL_TITLE).text
        modal_content = self.element_is_visible(self.locators.MODAL_CONTENT).text
        return modal_title, len(modal_content)


class ExitIntent(BasePage):
    locators = PageLocators()

    @allure.step('Check that modal window is appearing after mouse moving out of the view pane')
    def check_modal_appear(self):
        time.sleep(5)
        with allure.step('Imitating mouse moving / moving mouse out of the user view pane'):
            self.action_mouse_out_of_the_viewport()
            pyautogui.moveTo(1000, 200)
        with allure.step('Waiting for modal window to appear'):
            modal_window = self.element_is_present(self.locators.MODAL_WINDOW)
        assert modal_window.is_displayed(), 'Modal window did not appear'


class FileUploader(BasePage):
    locators = PageLocators()

    @allure.step('Uploading file with upload button')
    def check_file_uploading(self):
        self.element_is_present(self.locators.CHOSE_FILE_BUTTON).send_keys('/Users/anton/PycharmProjects/Test-The'
                                                                           '-Internet-Herokuapp/src/test_file.txt')
        self.element_is_present(self.locators.UPLOAD_BUTTON).click()
        upload_msg = self.element_is_present(self.locators.UPLOADED_MSG).text
        return upload_msg


class FloatingMenu(BasePage):
    locators = PageLocators()

    @allure.title('Performing scrolling / verifying floating menu is visible all the time')
    def check_floating_menu_presence(self):
        floating_menu = self.element_is_present(self.locators.FLOATING_MENU)
        random_destination = str(random.randint(0, 999))
        self.driver.execute_script("window.scrollBy(0," + random_destination + ");")
        assert floating_menu.is_displayed(), 'Floating menu did not appear'


class FormAuthentication(BasePage):
    locators = PageLocators()

    @allure.step('Submitting valid credentials')
    def check_success_auth(self):
        username = 'tomsmith'
        password = 'SuperSecretPassword!'
        self.element_is_present(self.locators.USERNAME_FIELD).send_keys(username)
        self.element_is_present(self.locators.PASSWORD_FIELD).send_keys(password)
        self.element_is_present(self.locators.LOGIN_BUTTON).click()
        login_msg = self.element_is_present(self.locators.LOGIN_MSG).text
        return login_msg

    @allure.step('Submitting invalid username')
    def check_invalid_username_auth(self):
        username = 'johnsmith'
        password = 'SuperSecretPassword!'
        self.element_is_present(self.locators.USERNAME_FIELD).send_keys(username)
        self.element_is_present(self.locators.PASSWORD_FIELD).send_keys(password)
        self.element_is_present(self.locators.LOGIN_BUTTON).click()
        login_msg = self.element_is_present(self.locators.LOGIN_MSG).text
        return login_msg

    @allure.step('Submitting invalid password')
    def check_invalid_password_auth(self):
        username = 'tomsmith'
        password = '1234qw!'
        self.element_is_present(self.locators.USERNAME_FIELD).send_keys(username)
        self.element_is_present(self.locators.PASSWORD_FIELD).send_keys(password)
        self.element_is_present(self.locators.LOGIN_BUTTON).click()
        login_msg = self.element_is_present(self.locators.LOGIN_MSG).text
        return login_msg

    @allure.step('Submitting empty login form')
    def check_empty_login_auth(self):
        self.element_is_present(self.locators.LOGIN_BUTTON).click()
        login_msg = self.element_is_present(self.locators.LOGIN_MSG).text
        return login_msg


class Frames(BasePage):
    locators = PageLocators()

    def check_nested_frames_content(self):
        with allure.step('Locating & switching to Top Frame'):
            frame_top = self.element_is_present(self.locators.FRAME_TOP)
            self.driver.switch_to.frame(frame_top)
        with allure.step('Locating & switching to Left Frame / extracting frame text'):
            left_frame = self.element_is_present(self.locators.LEFT_FRAME)
            self.driver.switch_to.frame(left_frame)
            left_text = self.element_is_present(self.locators.FRAME_TEXT).text
        with allure.step('Switching to default content'):
            self.driver.switch_to.default_content()
        with allure.step('Switching to Top Frame'):
            self.driver.switch_to.frame(frame_top)
        with allure.step('Locating & switching to Middle Frame / extracting frame text'):
            middle_frame = self.element_is_present(self.locators.MIDDLE_FRAME)
            self.driver.switch_to.frame(middle_frame)
            middle_text = self.element_is_present(self.locators.FRAME_TEXT).text
        with allure.step('Switching to default content'):
            self.driver.switch_to.default_content()
        with allure.step('Switching to Top Frame'):
            self.driver.switch_to.frame(frame_top)
        with allure.step('Locating & switching to Right Frame / extracting frame text'):
            right_frame = self.element_is_present(self.locators.RIGHT_FRAME)
            self.driver.switch_to.frame(right_frame)
            right_text = self.element_is_present(self.locators.FRAME_TEXT).text
        with allure.step('Switching to default content'):
            self.driver.switch_to.default_content()
        with allure.step('Locating & switching to Bottom Frame / extracting frame text'):
            frame_bottom = self.element_is_present(self.locators.BOTTOM_FRAME)
            self.driver.switch_to.frame(frame_bottom)
            bottom_text = self.element_is_present(self.locators.FRAME_TEXT).text
        return left_text, middle_text, right_text, bottom_text

    def check_iframe_interaction(self):
        with allure.step('Iframe locating & switching'):
            iframe = self.element_is_present(self.locators.IFRAME)
            self.driver.switch_to.frame(iframe)
        with allure.step('Interaction with TinyMCE WYSIWYG Editor after switching to Iframe'):
            iframe_text_field = self.element_is_present(self.locators.IFRAME_INPUT_TEXT)
            iframe_text_field.click()
            iframe_text_field.send_keys(' Mine too')
        assert iframe_text_field.is_displayed(), 'Driver could not switch to iframe'


class HorizontalSlider(BasePage):
    locators = PageLocators()

    @allure.step('Clicking slider and moving by mouse')
    def check_slider_moving_by_mouse(self):
        range_value_before = self.element_is_visible(self.locators.SLIDER_FIELD).text
        slider = self.element_is_present(self.locators.SLIDER)
        self.action_drag_and_drop_by_offset(slider, random.randint(1, 100), 0)
        range_value_after = self.element_is_visible(self.locators.SLIDER_FIELD).text
        return range_value_before, range_value_after

    @allure.step('Moving slider by arrow keys')
    def check_slider_moving_by_arrow_keys(self):
        range_value_before = self.element_is_visible(self.locators.SLIDER_FIELD).text
        slider = self.element_is_present(self.locators.SLIDER)
        slider.click()
        slider.send_keys(Keys.RIGHT)
        slider.send_keys(Keys.LEFT)
        range_value_after = self.element_is_visible(self.locators.SLIDER_FIELD).text
        return range_value_before, range_value_after


class Hovers(BasePage):
    locators = PageLocators()

    @allure.step('Hovering over the images and checking if user info is appearing')
    def check_hovers(self):
        user = self.element_is_present(self.locators.USER)
        self.action_move_to_element(user)
        user_caption = self.element_is_present(self.locators.USER_CAPTION)
        assert user_caption.is_displayed(), 'Hover text did not appear'


class InfiniteScroll(BasePage):
    @allure.step('Performing infinite scrolling / verifying the process is running')
    def check_infinite_scroll(self):
        scroll_pause_time = 0.5
        current_scrolling_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause_time)
            new_scrolling_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_scrolling_height != current_scrolling_height:
                break
            assert current_scrolling_height != new_scrolling_height, 'Infinite scrolling did not reproduce'


class Inputs(BasePage):
    locators = PageLocators()

    @allure.step('Input random number value')
    def check_input_numbers(self):
        input_field = self.element_is_present(self.locators.NUMBER_INPUT_FIELD)
        input_field.click()
        input_field.send_keys(random.randint(-1000, 1000))
        input_opt = input_field.get_attribute('value')
        assert input_opt.isdigit(), 'Impossible to input digital characters'

    @allure.step('Input text value')
    def check_non_numeric_chars(self):
        input_field = self.element_is_present(self.locators.NUMBER_INPUT_FIELD)
        input_field.click()
        input_field.send_keys('ui')
        input_opt = input_field.get_attribute('value')
        assert '' in input_opt, 'Non-numeric characters are possible for input'


class JQueryUI(BasePage):
    locators = PageLocators()

    def check_enabled_menu(self):
        with allure.step('Locating enabled menu'):
            enabled_menu = self.element_is_present(self.locators.JQ_ENABLED)
        with allure.step('Performing JS click on the menu button'):
            self.js_script_click(enabled_menu)
        with allure.step('Asserting that menu is enabled and displayed'):
            assert enabled_menu.is_enabled() and enabled_menu.is_displayed(), 'Enabled menu is not clickable'

    def check_back_to_jquery_menu(self):
        with allure.step('Locating current url and menu button'):
            current_url = self.driver.current_url
            enabled_menu = self.element_is_present(self.locators.JQ_ENABLED)
        with allure.step('Performing JS click on the menu button'):
            self.js_script_click(enabled_menu)
        with allure.step('Clicking on the back button and locating new current url'):
            back_to_jquery = self.element_is_present(self.locators.BACK_TO_JQUERY_UI)
            self.js_script_click(back_to_jquery)
            new_url = self.driver.current_url
        assert current_url != new_url, 'Button link did not refer to http://the-internet.herokuapp.com/jqueryui'

    def check_downloads_menu(self):
        with allure.step('Locating enabled menu'):
            enabled_menu = self.element_is_present(self.locators.JQ_ENABLED)
        with allure.step('Performing JS click on the menu button'):
            self.js_script_click(enabled_menu)
        with allure.step('Locating downloads menu'):
            downloads_menu = self.element_is_present(self.locators.JQ_DOWNLOADS)
        with allure.step('Performing JS click on the menu button'):
            self.js_script_click(downloads_menu)
        assert downloads_menu.is_enabled() and downloads_menu.is_displayed(), 'Downloads menu is not clickable'

    @allure.step('Performing clicking on the PDF button / Checking that file has been downloaded ')
    def check_downloads_pdf(self):
        enabled_menu = self.element_is_present(self.locators.JQ_ENABLED)
        self.js_script_click(enabled_menu)
        downloads_menu = self.element_is_present(self.locators.JQ_DOWNLOADS)
        self.js_script_click(downloads_menu)
        pdf_menu = self.element_is_present(self.locators.JQ_PDF)
        self.js_script_click(pdf_menu)
        fileends = "crdownload"
        while "crdownload" == fileends:
            time.sleep(1)
            newest_file = self.latest_download_file()
            if "crdownload" in newest_file:
                fileends = "crdownload"
            else:
                fileends = "none"
        assert '.pdf' in self.latest_download_file(), 'PDF file was not downloaded'

    @allure.step('Performing clicking on the CSV button / Checking that file has been downloaded ')
    def check_downloads_csv(self):
        enabled_menu = self.element_is_present(self.locators.JQ_ENABLED)
        self.js_script_click(enabled_menu)
        downloads_menu = self.element_is_present(self.locators.JQ_DOWNLOADS)
        self.js_script_click(downloads_menu)
        csv_menu = self.element_is_present(self.locators.JQ_CSV)
        self.js_script_click(csv_menu)
        fileends = "crdownload"
        while "crdownload" == fileends:
            time.sleep(1)
            newest_file = self.latest_download_file()
            if "crdownload" in newest_file:
                fileends = "crdownload"
            else:
                fileends = "none"
        assert '.csv' in self.latest_download_file(), 'CSV file was not downloaded'

    @allure.step('Performing clicking on the Excel button / Checking that file has been downloaded ')
    def check_downloads_xls(self):
        enabled_menu = self.element_is_present(self.locators.JQ_ENABLED)
        self.js_script_click(enabled_menu)
        downloads_menu = self.element_is_present(self.locators.JQ_DOWNLOADS)
        self.js_script_click(downloads_menu)
        xls_menu = self.element_is_present(self.locators.JQ_EXCEL)
        self.js_script_click(xls_menu)
        fileends = "crdownload"
        while "crdownload" == fileends:
            time.sleep(1)
            newest_file = self.latest_download_file()
            if "crdownload" in newest_file:
                fileends = "crdownload"
            else:
                fileends = "none"
        assert '.xls' in self.latest_download_file(), 'XLS file was not downloaded'

    @allure.step('Checking that disabled menu is not clickable')
    def check_disabled_menu(self):
        disabled_menu = self.element_is_present(self.locators.JQ_DISABLED)
        self.js_script_click(disabled_menu)
        assert disabled_menu.is_enabled(), 'Disabled menu is enabled'


class JSAlerts(BasePage):
    locators = PageLocators()

    def check_js_alert_click(self):
        with allure.step('Clicking on alert button'):
            self.element_is_present(self.locators.JS_ALERT).click()
        with allure.step('Switching & accepting alert window'):
            alert_window = self.driver.switch_to.alert
            alert_window.accept()
        with allure.step('Extract text from "Result" field'):
            alert_text = self.element_is_present(self.locators.ALERT_RESULT).text
        return alert_text

    def check_js_confirm_accept(self):
        with allure.step('Clicking on alert button'):
            self.element_is_present(self.locators.JS_CONFIRM).click()
        with allure.step('Switching & accepting alert window'):
            alert_window = self.driver.switch_to.alert
            alert_window.accept()
        with allure.step('Extract text from "Result" field'):
            alert_text = self.element_is_present(self.locators.ALERT_RESULT).text
        return alert_text

    def check_js_confirm_dismiss(self):
        with allure.step('Clicking on alert button'):
            self.element_is_present(self.locators.JS_CONFIRM).click()
        with allure.step('Switching & dismissing alert window'):
            alert_window = self.driver.switch_to.alert
            alert_window.dismiss()
        with allure.step('Extract text from "Result" field'):
            alert_text = self.element_is_present(self.locators.ALERT_RESULT).text
        return alert_text

    def check_js_prompt_click_accept(self):
        with allure.step('Generating random text'):
            text = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
        with allure.step('Clicking on alert button'):
            self.element_is_present(self.locators.JS_PROMPT).click()
        with allure.step('Switching & sending text to alert window'):
            prompt = self.driver.switch_to.alert
            prompt.send_keys(text)
            prompt.accept()
        with allure.step('Extract text from "Result" field'):
            text_prompt = self.element_is_present(self.locators.ALERT_RESULT).text
        return text, text_prompt

    def check_js_prompt_click_dismiss(self):
        with allure.step('Clicking on alert button'):
            self.element_is_present(self.locators.JS_PROMPT).click()
        with allure.step('Switching & dismissing alert window'):
            prompt = self.driver.switch_to.alert
            prompt.dismiss()
        with allure.step('Extract text from "Result" field'):
            text_prompt = self.element_is_present(self.locators.ALERT_RESULT).text
        return text_prompt


class KeyPresses(BasePage):
    locators = PageLocators()

    @allure.step('Performing key pressing & asserting result in text field')
    def check_key_presses(self):
        self.action_key_down()
        key_pressed = 'TAB'
        key_press_result = self.element_is_present(self.locators.KEY_RESULT).text
        assert key_pressed in key_press_result, 'Key was not pressed'


class MultipleWindows(BasePage):
    locators = PageLocators()

    @allure.step('Opening a new window / Comparing initial and following link')
    def check_multiple_windows(self):
        initial_url = self.driver.current_url
        self.element_is_present(self.locators.OPEN_NEW_WINDOW).click()
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        current_url = self.driver.current_url
        assert initial_url != current_url, 'New window did not appear'


class NotificationMessage(BasePage):
    locators = PageLocators()

    @allure.step('Checking that notification message is changing after pressing special button')
    def check_notification_message(self):
        self.element_is_present(self.locators.NEW_NOTIFY_MSG).click()
        new_notification_msg = self.element_is_present(self.locators.NOTIFICATION_MSG)
        assert new_notification_msg.is_displayed(), 'Notification Message did not appear'


class StatusCodes(BasePage):
    locators = PageLocators()

    @allure.step('Requesting status code / Verifying response is 200')
    def check_200_status_code(self):
        page_200 = self.element_is_present(self.locators.PAGE_200)
        page_200.click()
        response = requests.get(self.driver.current_url)
        assert response.status_code == 200, 'Expected 200, got different status code'

    @allure.step('Requesting status code / Verifying response is 301')
    def check_301_status_code(self):
        page_301 = self.element_is_present(self.locators.PAGE_301)
        page_301.click()
        response = requests.get(self.driver.current_url)
        assert response.status_code == 301, 'Expected 301, got different status code'

    @allure.step('Requesting status code / Verifying response is 404')
    def check_404_status_code(self):
        page_404 = self.element_is_present(self.locators.PAGE_404)
        page_404.click()
        response = requests.get(self.driver.current_url)
        assert response.status_code == 404, 'Expected 404, got different status code'

    @allure.step('Requesting status code / Verifying response is 500')
    def check_500_status_code(self):
        page_500 = self.element_is_present(self.locators.PAGE_500)
        page_500.click()
        response = requests.get(self.driver.current_url)
        assert response.status_code == 500, 'Expected 500, got different status code'


class Typos(BasePage):
    locators = PageLocators()

    @allure.step('Checking that typo is being introduced on each page load')
    def check_typos_finding(self):
        initial_text = self.element_is_present(self.locators.TYPOS_TEXT).text
        self.driver.refresh()
        loaded_text = self.element_is_present(self.locators.TYPOS_TEXT).text
        assert initial_text != loaded_text, 'Both texts are the same'
