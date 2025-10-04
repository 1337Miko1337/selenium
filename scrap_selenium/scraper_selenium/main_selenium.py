import sys
from time import sleep
import os
import django
from selenium import webdriver

sys.path.append("C:\\Users\\Vin Disel\\Desktop\\Work_selenium\\scrap_selenium")
os.environ["DJANGO_SETTINGS_MODULE"] = "scrap_selenium.settings"
django.setup()
from scraper_selenium.models import Phone

url = 'https://brain.com.ua/'

driver = webdriver.Chrome()

driver.get(url)
sleep(3)
# input_find = driver.find_element('xpath',
#                                 "//div[@class='header-top-in']/div[@class ='search-form header-search-form']/form/input[@type='search']")
input_find = driver.find_element('xpath',
                                 "//div[@class='header-bottom']/div/div/div[@class ='search-form header-search-form']/form/input[@type='search']")

input_find.send_keys('Apple iPhone 15 128GB Black')
input_button = driver.find_element('xpath',
                                   "//div[@class='header-bottom']/div/div/div[@class ='search-form header-search-form']/form/input[@type='submit']")

input_button.click()
first_phone = driver.find_element('xpath',
                                  "//div[@class='description-wrapper']/div[@class='br-pp-desc br-pp-ipd-hidden ']/a")

first_phone.click()
name = driver.find_element('xpath', "//*[@id='br-pr-1']/h1").text.replace('\n', '')
print(name)
sleep(3)
color_elements = driver.find_elements('xpath', '//div[@class="series-colors-column"]//div[@class="slice"]')
colors = []
for el in color_elements:
    bg_color = el.get_attribute('style').replace('background: ', '')
    colors.append(bg_color)
print(colors)
print(len(colors))
memory = driver.find_elements('xpath',
                              '//div[@class="stuff-series stuff-series-characteristics main-stuff-series-block current-product-series "]//div[@class="series-items series-characteristics-container"]//a')
memory_all = []
for m in memory:
    memory_all.append(m.text)
print(memory_all)
code = driver.find_elements('xpath', '//div[@class="product-code-num"]/span[@class="br-pr-code-val"]')
for c in code:
    if c.text != '':
        code_text = c.text
print(code_text)
reviews = driver.find_element('xpath', '//a[@class="forbid-click"]').text
print(reviews)
price = driver.find_element('xpath', "//div[@class='br-pr-price main-price-block']/div[@class='br-pr-np']/div").text
all_char = driver.find_element('xpath', '//button[@type="button" and contains (@class, "br-prs-button")]')
# sleep(1)
# all_char.click()
characteristics = driver.find_elements('xpath', '//div[@class="br-pr-chr-item"]')
print('len all: ', len(characteristics))
characteristics_res = dict()
j = 0
for char in characteristics:
    j += 1
    print('j: ', j)
    charact = char.find_elements('xpath', './/div/div/span')
    for i in range(1, len(charact) + 1):
        print('i: ', i)
        if i % 2 == 0:
            value = charact[i - 1].get_attribute("textContent").strip().replace('\n', '').replace('\t', '').replace(' ',
                                                                                                                    '')
            print('value: ', charact[i - 1].get_attribute("outerHTML"))
            characteristics_res.update({key: value})
        else:
            key = charact[i - 1].get_attribute("textContent").strip().replace('\n', '').replace('\t', '').replace(' ',
                                                                                                                  '')
            print('key: ', charact[i - 1].get_attribute("outerHTML"))
print(characteristics_res)
div_img = driver.find_element('xpath', '//div[@class="slick-track"]')
img_all = div_img.find_elements('xpath', './/img')
img = []
for i in img_all:
    img.append(i.get_attribute('src'))

print('img: ', img)
phone = Phone.objects.create(
    name=name,
    color=colors,
    memory=memory_all,
    price=price,
    photo=img,
    code=code_text,
    fb=reviews,
    characteristics=characteristics_res,
)
