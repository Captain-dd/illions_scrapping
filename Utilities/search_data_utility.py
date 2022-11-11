import time

import pandas as pd

import Locators.ResultPageLocators as Rpl
import Locators.SearchPageLocators as Spl
from Utilities.common_utilities import CommonUtilites


class Util:

    def get_all_data(self, city):
        doctor_lst=[]
        doctor_details_lst=[]
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
            for i in range(len(doctor_name_lst)):
                doctor_lst.append(doctor_name_lst[i].text)
            for i in range(len(doctor_details)):
                doctor_details_lst.append(doctor_details[i].text)
            return doctor_lst, doctor_details_lst
        except:
            return [], []

    def save_csv(self, city, doctor_name_lst, doctor_details):
        columns = ['name',  'city','address','mobile_number']
        df = pd.DataFrame(columns=columns)
        for i in range(len(doctor_name_lst)):
            try:
                temp = doctor_name_lst[i]
                df.at[i, 'name'] = temp
                df.at[i,'city']=city[i]

            except:
                print(i)

        for i in range(len(doctor_details)):
            try:
                temp = doctor_details[i]
                if i % 2 == 0:
                    x = (temp.replace('Driving directions', '')).replace('\n', '')
                    df.at[i // 2, 'address'] = x

                else:
                    df.at[i // 2, 'mobile_number'] = temp[7:21]

            except:
                pass

        df.to_csv('data.csv', index=False)
