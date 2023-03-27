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
