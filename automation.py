from selenium import webdriver
from pprint import pprint
from selenium import webdriver


LINK = 'должна быть ссылка'
settings = webdriver.ChromeOptions()
settings.add_argument('--start-maximized')
settings.add_argument('--incognito')

browser = webdriver.Chrome(options=settings)
browser.get(LINK)

element_1 = browser.find_elements_by_class_name('docssharedWizToggleLabeledLabelWrapper')
element_1[2].click()

form_input = browser.find_element_by_class_name('quantumWizTextinputPaperinputInput')

form_input.send_keys('kek')

#select_list = browser.find_element_by_class_name("quantumWizMenuPaperselectOptionList")
#select_list.click()
#options = browser.find_element_by_class_name('exportSelectPopup')
#option_text = options.find_element_by_class_name('quantumWizMenuPaperselectContent')
#[element.click() for element in option_text if element.text == 'Вариант 4']
browser.get_screenshot_as_file('fullscreen.png')
pic = browser.find_element_by_class_name('freebirdFormviewerViewItemsEmbeddedobjectImage')
pic.screenshot('from cyberpunk.png')
