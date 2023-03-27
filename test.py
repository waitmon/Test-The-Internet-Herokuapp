from pages.all_pages import AddRemoveElements, BasicAuth, BrokenImages, Checkboxes, ContextMenu, DisappearingElements, \
    DragAndDrop, DropdownList, DynamicContent, DynamicControls


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

    def test_enable_field(self, driver):
        page = DynamicControls(driver, 'http://the-internet.herokuapp.com/dynamic_controls')
        page.open()
        page.check_enable_input()
