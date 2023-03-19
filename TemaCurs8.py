"""
Alege-ți unuul sau mai multe din sugestiile de site-uri de mai jos
- https://www.phptravels.net/
- http://automationpractice.com/index.php
- https://formy-project.herokuapp.com/
- https://the-internet.herokuapp.com/
- https://www.techlistic.com/p/selenium-practice-form.html
- jules.app
Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
● Id
● Link text
● Parțial link text
● Name
● Tag*
● Class name*
● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
observație:
- Probabil nu vei găsi un singur website care să cuprindă toate variantele
de mai sus, astfel că îți recomandăm să folosești mai multe site-uri.

- Opțional: La tag și class name vei folosi find elementS! - salvează în listă.
Interactionează cu un element la alegere din listă.

Pentru xpath identifică elemente după criteriile de mai jos:
● 3 după atribut valoare
● 3 după textul de pe element
● 1 după parțial text
● 1 cu SAU, folosind pipe |
● 1 cu *
● 1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci
cu (xpath)[1]
● 1 în care să folosești parent::
● 1 în care să folosești fratele anterior sau de după (la alegere)
● 1 funcție ca și cea de la clasă prin care să pot alege eu prin parametru cu
ce element vreau să interacționez.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)



"""
ID
"""
chrome.get("https://formy-project.herokuapp.com/form")

first_name = chrome.find_element(By.ID, "first-name")
first_name.send_keys('Lavi')

last_name = chrome.find_element(By.ID, "last-name")
last_name.send_keys('POP')

last_name = chrome.find_element(By.ID, "job-title")
last_name.send_keys('Asistent')


"""
Link Test
"""
chrome.get("https://formy-project.herokuapp.com")
chrome.find_element(By.LINK_TEXT, "Autocomplete").click()

chrome.find_element(By.LINK_TEXT, "Buttons").click()

chrome.find_element(By.LINK_TEXT, "Checkbox").click()

"""
Partial Link test
"""
chrome.find_element(By.PARTIAL_LINK_TEXT, "complete").click()

chrome.find_element(By.PARTIAL_LINK_TEXT, "odal").click()

chrome.find_element(By.PARTIAL_LINK_TEXT, "File").click()

"""
Name
"""
chrome.get("https://phptravels.net/")
chrome.find_element(By.NAME, "to").send_keys('Hawai')
chrome.find_element(By.NAME, "from").send_keys('Romania')

"""
Tag
"""
chrome.get("https://formy-project.herokuapp.com/form")
# input_list = chrome.find_elements(By.TAG_NAME, "input")
# input_list[0].send_keys('Lavi')
# input_list[1].send_keys('Pop')
# input_list[2].send_keys('Asistent')

"""
Class name
"""

# chrome.get("https://formy-project.herokuapp.com/form")
# chrome.find_element(By.CLASS_NAME, "form-control").send_keys("Lavi")
#
# chrome.find_elements(By.CLASS_NAME, "form-control")[1].send_keys("POP")
#
# chrome.find_elements(By.CLASS_NAME, "form-control")[2].send_keys("Asistent")

"""
CSS
"""

chrome.find_element(By.CSS_SELECTOR, "input#first-name").send_keys("La")

chrome.find_element(By.CSS_SELECTOR, "input.form-control").send_keys("vi")

chrome.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter last name"]').send_keys("P")

chrome.find_element(By.CSS_SELECTOR, 'div input[placeholder*="last name"]').send_keys('op')



chrome.get('https://formy-project.herokuapp.com/form')

# selector by Xpath - atribut=valoare
chrome.find_element(By.XPATH, '//input[@id="first-name"]').send_keys('L')

# selector by Xpath - * toate elementele care respecta regula
chrome.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('a')

# selector by Xpath - navigare in jos - trecem prin fiecare element
chrome.find_element(By.XPATH, '//div/div/input[@id="first-name"]').send_keys('v')

# selector by Xpath - navigare in jos - skip tags _ cautam oriunde sub forma un input care sa respecte regula
chrome.find_element(By.XPATH, '//form//input[@id="first-name"]').send_keys('i')

#selector by Xpath - selectare elem din lista - index incepe de la 1
chrome.find_element(By.XPATH, '(//input[@class="form-control"])[2]').send_keys('P')

# selector by Xpath - OR primul gasit dintre variante
s = chrome.find_element(By.XPATH, '//input[@id="last-name1"] | //input[@id="last-name2"] | //input[@id="last-name"]')

#stergem valorile
s.clear()
s.send_keys('Pop')

#selector by Xpath - in f de textul partial + luam textul de pe el cu proprietatea text
full_text = chrome.find_element(By.XPATH, '//a[contains(text(), "Sub")]').text
print(full_text)

#selector by Xpath - in f de textul vizibil
chrome.find_element(By.XPATH, '//a[text()="Submit"]').click()

#parent si sibling
chrome.find_element(By.XPATH, '//label[text()="First name"]/parent::strong/following-sibling::input/preceding-sibling::strong')

# cu ajutorul unei functii cand avem foarte multe elemente de acelasi tip si vrem sa parametrizam selectorul



def formy_input(placeholder_text, input_value):
    input = chrome.find_element(By.XPATH, f'//input[@placeholder="{placeholder_text}"]')
    input.clear()
    input.send_keys(input_value)


chrome.get('https://formy-project.herokuapp.com/form')

formy_input('Enter first name', 'LAVI')
formy_input('Enter last name', 'POP')
formy_input('Enter your job title', 'ASISTENT')








