from selenium.webdriver.common.by import By

provider_city_radioButton = (By.XPATH, "//div[@id='provider_search_form']//span[contains(text(), 'Provider city')]")
city_field = (By.XPATH, '//input[@name="city"]')
search_button = (By.XPATH, '//div[@id="provider_search_form"]//button[@class = "button loading-button"]')
import pandas as pd
df = pd.read_excel('city_lst.xlsx')
# print(list(df['City'][:289].itertuples(index=False)))
# print(list(df['City'][:289].items()))
d=[i for i in list(df['City'][:289])]
result = []
for i in d:

    result.append(tuple)

# d=list(map(tuple,d))
# print(d)