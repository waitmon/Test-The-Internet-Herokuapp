from pages.all_pages import AddRemoveElements, BasicAuth, BrokenImages, Checkboxes, ContextMenu, DisappearingElements, \
    DragAndDrop, DropdownList, DynamicContent, DynamicControls, DynamicLoading, EntryAd, ExitIntent, FileUploader, \
    FloatingMenu, FormAuthentication, Frames, HorizontalSlider, Hovers, InfiniteScroll, Inputs, JQueryUI, JSAlerts, \
    KeyPresses, MultipleWindows, NotificationMessage, StatusCodes, Typos


class TestAddRemoveElements:

    def test_add_elements(self, driver):
        page = AddRemoveElements(driver, 'https://the-internet.herokuapp.com/add_remove_elements/')
        page.open()
        page.check_add_element()

    def test_remove_elements(self, driver):
        page = AddRemoveElements(driver, 'https://the-internet.herokuapp.com/add_remove_elements/')
        page.open()
        page.check_remove_element()


class TestBasicAuth:

    def test_auth_success(self, driver):
        page = BasicAuth(driver, 'https://admin:admin@the-internet.herokuapp.com/basic_auth/')
        page.open()
        auth_msg = page.check_success_authorization()
        assert auth_msg == 'Congratulations! You must have the proper credentials.', 'Incorrect login'


class TestBrokenImages:

    def test_broken_images(self, driver):
        page = BrokenImages(driver, 'http://the-internet.herokuapp.com/broken_images')
        page.open()
        page.check_broken_images()

    def test_correct_image(self, driver):
        page = BrokenImages(driver, 'http://the-internet.herokuapp.com/broken_images')
        page.open()
        page.check_correct_image()

    def test_checkbox_checked(self, driver):
        page = Checkboxes(driver, 'http://the-internet.herokuapp.com/checkboxes')
        page.open()
        page.check_checked_checkboxes()


class TestContextMenu:

    def test_right_click_context_menu(self, driver):
        page = ContextMenu(driver, 'http://the-internet.herokuapp.com/context_menu')
        page.open()
        alert_msg = page.check_right_click()
        assert alert_msg == 'You selected a context menu', 'Context menu did not display'


class TestDisappearingElements:

    def test_visibility_elements(self, driver):
        page = DisappearingElements(driver, 'http://the-internet.herokuapp.com/disappearing_elements')
        page.open()
        page.check_element_visibility()


class TestDragAndDrop:

    def test_drag_box_moving(self, driver):
        page = DragAndDrop(driver, 'http://the-internet.herokuapp.com/drag_and_drop')
        page.open()
        page.check_drag_box_moving()


class TestDropdownList:

    def test_select_option_1(self, driver):
        page = DropdownList(driver, 'http://the-internet.herokuapp.com/dropdown')
        page.open()
        page.check_first_option_selected()

    def test_select_option_2(self, driver):
        page = DropdownList(driver, 'http://the-internet.herokuapp.com/dropdown')
        page.open()
        page.check_second_option_selected()


class TestDynamicContent:

    def test_content_changing(self, driver):
        page = DynamicContent(driver, 'http://the-internet.herokuapp.com/dynamic_content')
        page.open()
        page.check_content_changing()

    def test_static_content(self, driver):
        page = DynamicContent(driver, 'http://the-internet.herokuapp.com/dynamic_content')
        page.open()
        page.check_static_content()


class TestDynamicControls:

    def test_checkbox_remove(self, driver):
        page = DynamicControls(driver, 'http://the-internet.herokuapp.com/dynamic_controls')
        page.open()
        page.check_checkbox_remove()

    def test_checkbox_add(self, driver):
        page = DynamicControls(driver, 'http://the-internet.herokuapp.com/dynamic_controls')
        page.open()
        page.check_checkbox_appear()

    def test_enable_input(self, driver):
        page = DynamicControls(driver, 'http://the-internet.herokuapp.com/dynamic_controls')
        page.open()
        page.check_enable_input()

    def test_disable_input(self, driver):
        page = DynamicControls(driver, 'http://the-internet.herokuapp.com/dynamic_controls')
        page.open()
        page.check_disable_input()


class TestDynamicLoading:

    def test_element_is_rendered_after_click(self, driver):
        page = DynamicLoading(driver, 'http://the-internet.herokuapp.com/dynamic_loading/2')
        page.open()
        page.check_element_is_rendered_after_click()


class TestEntryAd:

    def test_entry_ad_content(self, driver):
        page = EntryAd(driver, 'http://the-internet.herokuapp.com/entry_ad')
        page.open()
        modal_msg, modal_content = page.check_entry_ad_content()
        assert modal_msg == 'THIS IS A MODAL WINDOW' and modal_content > 0, 'Modal window did not appear'


class TestExitIntent:

    def test_exit_intent(self, driver):
        page = ExitIntent(driver, 'http://the-internet.herokuapp.com/exit_intent')
        page.open()
        page.check_modal_appear()


class TestFileUploader:

    def test_file_uploading(self, driver):
        page = FileUploader(driver, 'http://the-internet.herokuapp.com/upload')
        page.open()
        upload_message = page.check_file_uploading()
        assert upload_message == 'File Uploaded!', 'File was not uploaded'


class TestFloatingMenu:

    def test_floating_menu_presence(self, driver):
        page = FloatingMenu(driver, 'http://the-internet.herokuapp.com/floating_menu')
        page.open()
        page.check_floating_menu_presence()


class TestFormAuthentication:

    def test_success_auth(self, driver):
        page = FormAuthentication(driver, 'http://the-internet.herokuapp.com/login')
        page.open()
        login_result = page.check_success_auth()
        assert 'You logged into a secure area!' in login_result, 'Invalid Login warning appeared'

    def test_invalid_username_auth(self, driver):
        page = FormAuthentication(driver, 'http://the-internet.herokuapp.com/login')
        page.open()
        login_result = page.check_invalid_username_auth()
        assert 'Your username is invalid!' in login_result, 'Successful login message appeared'

    def test_invalid_password_auth(self, driver):
        page = FormAuthentication(driver, 'http://the-internet.herokuapp.com/login')
        page.open()
        login_result = page.check_invalid_password_auth()
        assert 'Your password is invalid!' in login_result, 'Successful login message appeared'

    def test_empty_login(self, driver):
        page = FormAuthentication(driver, 'http://the-internet.herokuapp.com/login')
        page.open()
        login_result = page.check_empty_login_auth()
        assert 'Your username is invalid!' in login_result, 'Successful login message appeared'


class TestFrames:

    def test_nested_frames_content(self, driver):
        page = Frames(driver, 'http://the-internet.herokuapp.com/nested_frames')
        page.open()
        left_text, middle_text, right_text, bottom_text = page.check_nested_frames_content()
        assert left_text == 'LEFT', 'Nested frame does not exist'
        assert middle_text == 'MIDDLE', 'Nested frame does not exist'
        assert right_text == 'RIGHT', 'Nested frame does not exist'
        assert bottom_text == 'BOTTOM', 'Nested frame does not exist'

    def test_iframe_interaction(self, driver):
        page = Frames(driver, 'http://the-internet.herokuapp.com/iframe')
        page.open()
        page.check_iframe_interaction()


class TestHorizontalSlider:

    def test_slider_moving(self, driver):
        page = HorizontalSlider(driver, 'http://the-internet.herokuapp.com/horizontal_slider')
        page.open()
        before, after = page.check_slider_moving_by_mouse()
        assert before != after, 'The slider range value did not change'

    def test_slider_moving_arrows(self, driver):
        page = HorizontalSlider(driver, 'http://the-internet.herokuapp.com/horizontal_slider')
        page.open()
        before, after = page.check_slider_moving_by_arrow_keys()
        assert before != after, 'The slider range value did not change'


class TestHovers:

    def test_hovers(self, driver):
        page = Hovers(driver, 'http://the-internet.herokuapp.com/hovers')
        page.open()
        page.check_hovers()


class TestInfiniteScroll:

    def test_infinite_scroll(self, driver):
        page = InfiniteScroll(driver, 'http://the-internet.herokuapp.com/infinite_scroll')
        page.open()
        page.check_infinite_scroll()


class TestInputs:

    def test_input_numbers(self, driver):
        page = Inputs(driver, 'http://the-internet.herokuapp.com/inputs')
        page.open()
        page.check_input_numbers()

    def test_input_non_digit_char(self, driver):
        page = Inputs(driver, 'http://the-internet.herokuapp.com/inputs')
        page.open()
        page.check_non_digit_char()


class TestJQueryUI:

    def test_enabled_menu(self, driver):
        page = JQueryUI(driver, 'http://the-internet.herokuapp.com/jqueryui/menu')
        page.open()
        page.check_enabled_menu()

    def test_back_to_jquery_menu(self, driver):
        page = JQueryUI(driver, 'http://the-internet.herokuapp.com/jqueryui/menu')
        page.open()
        page.check_back_to_jquery_menu()

    def test_downloads_menu(self, driver):
        page = JQueryUI(driver, 'http://the-internet.herokuapp.com/jqueryui/menu')
        page.open()
        page.check_downloads_menu()

    def test_downloads_pdf(self, driver):
        page = JQueryUI(driver, 'http://the-internet.herokuapp.com/jqueryui/menu')
        page.open()
        page.check_downloads_pdf()

    def test_downloads_csv(self, driver):
        page = JQueryUI(driver, 'http://the-internet.herokuapp.com/jqueryui/menu')
        page.open()
        page.check_downloads_csv()

    def test_downloads_xsl(self, driver):
        page = JQueryUI(driver, 'http://the-internet.herokuapp.com/jqueryui/menu')
        page.open()
        page.check_downloads_xls()

    def test_disabled_menu(self, driver):
        page = JQueryUI(driver, 'http://the-internet.herokuapp.com/jqueryui/menu')
        page.open()
        page.check_disabled_menu()


class TestJSAlerts:

    def test_js_alert_click(self, driver):
        page = JSAlerts(driver, 'http://the-internet.herokuapp.com/javascript_alerts')
        page.open()
        alert_msg = page.check_js_alert_click()
        assert alert_msg == 'You successfully clicked an alert', 'Alert window did not appear'

    def test_js_confirm_accept_click(self, driver):
        page = JSAlerts(driver, 'http://the-internet.herokuapp.com/javascript_alerts')
        page.open()
        alert_msg = page.check_js_confirm_accept()
        assert alert_msg == 'You clicked: Ok', 'Alert window did not appear'

    def test_js_confirm_dismiss_click(self, driver):
        page = JSAlerts(driver, 'http://the-internet.herokuapp.com/javascript_alerts')
        page.open()
        alert_msg = page.check_js_confirm_dismiss()
        assert alert_msg == 'You clicked: Cancel', 'Alert window did not appear'

    def test_js_prompt_accept_click(self, driver):
        page = JSAlerts(driver, 'http://the-internet.herokuapp.com/javascript_alerts')
        page.open()
        text, prompt_text = page.check_js_prompt_click_accept()
        assert text in prompt_text, 'Alert window did not appear'

    def test_js_prompt_accept_dismiss(self, driver):
        page = JSAlerts(driver, 'http://the-internet.herokuapp.com/javascript_alerts')
        page.open()
        text_res = page.check_js_prompt_click_dismiss()
        assert text_res == "You entered: null", 'Alert window did not appear'


class TestKeyPresses:

    def test_key_presses(self, driver):
        page = KeyPresses(driver, 'http://the-internet.herokuapp.com/key_presses')
        page.open()
        page.check_key_presses()


class TestMultipleWindows:

    def test_multiple_windows(self, driver):
        page = MultipleWindows(driver, 'http://the-internet.herokuapp.com/windows')
        page.open()
        page.check_multiple_windows()


class TestNotificationMessage:

    def test_notification_message(self, driver):
        page = NotificationMessage(driver, 'http://the-internet.herokuapp.com/notification_message_rendered')
        page.open()
        page.check_notification_message()


class TestStatusCodes:

    def test_200_status_code(self, driver):
        page = StatusCodes(driver, 'https://the-internet.herokuapp.com/status_codes')
        page.open()
        page.check_200_status_code()

    def test_301_status_code(self, driver):
        page = StatusCodes(driver, 'https://the-internet.herokuapp.com/status_codes')
        page.open()
        page.check_301_status_code()

    def test_404_status_code(self, driver):
        page = StatusCodes(driver, 'https://the-internet.herokuapp.com/status_codes')
        page.open()
        page.check_404_status_code()

    def test_500_status_code(self, driver):
        page = StatusCodes(driver, 'https://the-internet.herokuapp.com/status_codes')
        page.open()
        page.check_500_status_code()


class TestTypos:

    def test_typos_finding(self, driver):
        page = Typos(driver, 'https://the-internet.herokuapp.com/typos')
        page.open()
        page.check_typos_finding()
