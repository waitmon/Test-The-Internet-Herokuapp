from pages.all_pages import AddRemoveElements, BasicAuth, BrokenImages, Checkboxes, ContextMenu, DisappearingElements, \
    DragAndDrop, DropdownList, DynamicContent, DynamicControls, DynamicLoading, EntryAd, ExitIntent, FileUploader, \
    FloatingMenu, FormAuthentication, Frames, HorizontalSlider, Hovers, InfiniteScroll, Inputs, JQueryUI


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
        assert auth_msg == 'Congratulations! You must have the proper credentials.'


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
        assert alert_msg == 'You selected a context menu'


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
        assert modal_msg == 'THIS IS A MODAL WINDOW' and modal_content > 0


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
        assert upload_message == 'File Uploaded!'


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
        assert 'You logged into a secure area!' in login_result, 'Invalid Login warning appears'

    def test_invalid_username_auth(self, driver):
        page = FormAuthentication(driver, 'http://the-internet.herokuapp.com/login')
        page.open()
        login_result = page.check_invalid_username_auth()
        assert 'Your username is invalid!' in login_result, 'Successful login message appears'

    def test_invalid_password_auth(self, driver):
        page = FormAuthentication(driver, 'http://the-internet.herokuapp.com/login')
        page.open()
        login_result = page.check_invalid_password_auth()
        assert 'Your password is invalid!' in login_result, 'Successful login message appears'

    def test_empty_login(self, driver):
        page = FormAuthentication(driver, 'http://the-internet.herokuapp.com/login')
        page.open()
        login_result = page.check_empty_login_auth()
        assert 'Your username is invalid!' in login_result, 'Successful login message appears'


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
        assert before != after, 'the slider range value does not change'

    def test_slider_moving_arrows(self, driver):
        page = HorizontalSlider(driver, 'http://the-internet.herokuapp.com/horizontal_slider')
        page.open()
        before, after = page.check_slider_moving_by_arrow_keys()
        assert before != after, 'the slider range value does not change'


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
