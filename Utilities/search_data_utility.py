import time

import pandas as pd

import Locators.ResultPageLocators as Rpl
import Locators.SearchPageLocators as Spl
from Utilities.common_utilities import CommonUtilites


class Util:

    def get_all_data(self, city):
        cu = CommonUtilites()
        cu.click_element(element_locator=Spl.provider_city_radioButton)
        cu.clear_input(element_locator=Spl.city_field)
        cu.send_text(element_locator=Spl.city_field, text=city)
        cu.click_element(element_locator=Spl.search_button)
        time.sleep(3)
        cu.scroll_down()
        try:
            doctor_name_lst = cu.get_multiple_button(element_locator=Rpl.doctor_name)
            doctor_details = cu.get_multiple_button(element_locator=Rpl.doctor_address)
            return doctor_name_lst, doctor_details
        except:
            return [], []

    def save_csv(self, city, doctor_name_lst, doctor_details):
        columns = ['name', 'address', 'mobile_number']
        df = pd.DataFrame(columns=columns)
        for i in range(len(doctor_name_lst)):
            try:
                temp = doctor_name_lst[i].text

                df.at[i, 'name'] = temp
            except:
                print(i)

        for i in range(len(doctor_details)):
            try:
                temp = doctor_details[i].text
                if i % 2 == 0:
                    df.at[i // 2, 'address'] = temp

                else:
                    df.at[i // 2, 'mobile_number'] = temp

            except:
                pass

        df.to_csv(f'./result/{city}.csv', index=False)
