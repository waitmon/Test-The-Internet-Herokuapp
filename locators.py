from selenium.webdriver.common.by import By


class PageLocators:
    ADD_ELEMENT = (By.CSS_SELECTOR, 'button[onclick="addElement()"]')
    DELETE_ELEMENT = (By.CSS_SELECTOR, 'button[onclick="deleteElement()"]')
    ELEMENTS_ADDED = (By.CSS_SELECTOR, 'div[id="elements"]')

    BASIC_AUTH_LINK = (By.CSS_SELECTOR, 'a[href="/basic_auth"]')
    SUCCESSFUL_AUTH = (By.CSS_SELECTOR, '#content > div > p')

    IMAGES_LIST = (By.CSS_SELECTOR, 'div[class="example"]>img')
    VALID_IMAGE = (By.CSS_SELECTOR, 'img[src="img/avatar-blank.jpg"]')

    CHECKBOX_LIST = (By.CSS_SELECTOR, 'input[type="checkbox"]')
    CHECKED_STATUS = (By.CSS_SELECTOR, 'input[checked]')

    CONTEXT_MENU = (By.CSS_SELECTOR, 'div[id="hot-spot"]')

    ELEMENTS = (By.CSS_SELECTOR, 'li>a[href]')

    COLUMN_A = (By.CSS_SELECTOR, 'div[id="column-a"]')
    COLUMN_B = (By.CSS_SELECTOR, 'div[id="column-b"]')

    OPTION_1 = (By.CSS_SELECTOR, 'option[value="1"]')
    OPTION_2 = (By.CSS_SELECTOR, 'option[value="2"]')

    PAGE_CONTENT = (By.CSS_SELECTOR, 'div[class="large-10 columns"]')
    STATIC_BUTTON = (By.CSS_SELECTOR, 'a[href="/dynamic_content?with_content=static"]')
    COLUMN_1 = (By.CSS_SELECTOR, '#content > div:nth-child(1) > div.large-10.columns')
    COLUMN_2 = (By.CSS_SELECTOR, '#content > div:nth-child(4) > div.large-10.columns')

    ACTION_BUTTON = (By.CSS_SELECTOR, 'button[onclick="swapCheckbox()"]')
    BUTTON_MESSAGE = (By.CSS_SELECTOR, 'p[id="message"]')
    CHECKBOX_APPEAR = (By.CSS_SELECTOR, 'input[id="checkbox"]')

    ENABLE_DISABLE = (By.CSS_SELECTOR, 'button[onclick="swapInput()"]')
    INPUT_FIELD = (By.CSS_SELECTOR, 'input[type="text"]')

    HIDDEN_TEXT = (By.CSS_SELECTOR, 'div[id="finish"]')
    START_BUTTON = (By.CSS_SELECTOR, '#start > button')

    MODAL_TITLE = (By.CSS_SELECTOR, 'div[class="modal-title"]')
    MODAL_CONTENT = (By.CSS_SELECTOR, 'div[class="modal-body"]')
    MODAL_CLOSE = (By.CSS_SELECTOR, '#modal > div.modal > div.modal-footer > p')
    MODAL_WINDOW = (By.CSS_SELECTOR, 'div[class="modal"]')

    CHOSE_FILE_BUTTON = (By.CSS_SELECTOR, '#file-upload')
    UPLOAD_BUTTON = (By.CSS_SELECTOR, '#file-submit')
    UPLOADED_MSG = (By.CSS_SELECTOR, '#content > div > h3')

    FLOATING_MENU = (By.CSS_SELECTOR, 'div[id="menu"]')

    USERNAME_FIELD = (By.CSS_SELECTOR, '#username')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    LOGIN_MSG = (By.CSS_SELECTOR, '#flash')

    FRAME_TOP = (By.CSS_SELECTOR, 'frame[name="frame-top"]')
    LEFT_FRAME = (By.CSS_SELECTOR, 'frame[name="frame-left"]')
    FRAME_TEXT = (By.CSS_SELECTOR, 'body')
    MIDDLE_FRAME = (By.NAME, 'frame-middle')
    RIGHT_FRAME = (By.NAME, 'frame-right')
    BOTTOM_FRAME = (By.NAME, 'frame-bottom')

    IFRAME = (By.CSS_SELECTOR, 'iframe[id="mce_0_ifr"]')
    IFRAME_INPUT_TEXT = (By.CSS_SELECTOR, '#tinymce>p')

    SLIDER = (By.CSS_SELECTOR, 'input[type="range"]')
    SLIDER_FIELD = (By.CSS_SELECTOR, 'span[id="range"]')

    USER_CAPTION = (By.CLASS_NAME, 'figcaption')
    USER = (By.CLASS_NAME, 'figure')

    NUMBER_INPUT_FIELD = (By.CSS_SELECTOR, 'input[type="number"]')

    JQ_MENU = (By.CSS_SELECTOR, 'ul[id="menu"]')
    JQ_ENABLED = (By.CSS_SELECTOR, 'a[id="ui-id-2"]')
    JQ_DOWNLOADS = (By.CSS_SELECTOR, 'a[id="ui-id-4"]')
    BACK_TO_JQUERY_UI = (By.CSS_SELECTOR, 'a[id="ui-id-5"]')
    JQ_PDF = (By.CSS_SELECTOR, 'a[id="ui-id-6"]')
    JQ_CSV = (By.CSS_SELECTOR, 'a[id="ui-id-7"]')
    JQ_EXCEL = (By.CSS_SELECTOR, 'a[id="ui-id-8"]')
    JQ_DISABLED = (By.CSS_SELECTOR, 'a[id="ui-id-1"]')

    JS_ALERT = (By.CSS_SELECTOR, 'button[onclick="jsAlert()"]')
    JS_CONFIRM = (By.CSS_SELECTOR, 'button[onclick="jsConfirm()"]')
    JS_PROMPT = (By.CSS_SELECTOR, 'button[onclick="jsPrompt()"]')
    ALERT_RESULT = (By.CSS_SELECTOR, '#result')

    KEY_RESULT = (By.CSS_SELECTOR, '#result')

    OPEN_NEW_WINDOW = (By.CSS_SELECTOR, 'a[href="/windows/new"]')

    NOTIFICATION_MSG = (By.CSS_SELECTOR, '#flash')
    NEW_NOTIFY_MSG = (By.CSS_SELECTOR, 'a[href="/notification_message"]')

    PAGE_200 = (By.CSS_SELECTOR, 'a[href="status_codes/200"]')
    PAGE_301 = (By.CSS_SELECTOR, 'a[href="status_codes/301"]')
    PAGE_404 = (By.CSS_SELECTOR, 'a[href="status_codes/404"]')
    PAGE_500 = (By.CSS_SELECTOR, 'a[href="status_codes/500"]')

    TYPOS_TEXT = (By.CSS_SELECTOR, 'div[class="example"]')
