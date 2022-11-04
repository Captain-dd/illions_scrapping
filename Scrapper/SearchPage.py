import time
import pandas as pd
from Utilities.common_utilities import CommonUtilites
import Locators.SearchPageLocators as Spl
import Locators.ResultPageLocators as Rpl
import pytest


@pytest.mark.usefixtures('initiate_driver')
class TestSearchPage:

    def test_perform_search(self):

        columns = ['name','address' ,'mobile_number' ]

        df = pd.DataFrame(columns = columns)

        cu = CommonUtilites()
        cu.click_element(element_locator=Spl.provider_city_radioButton)
        cu.send_text(element_locator=Spl.city_field, text= 'New York')
        cu.click_element(element_locator=Spl.search_button)
        time.sleep(4)
        cu.scroll_down()
        doctor_name_lst = cu.get_multiple_button(element_locator=Rpl.doctor_name)
        doctor_details = cu.get_multiple_button(element_locator=Rpl.doctor_address)


        print("doctor name")
        for i in range(len(doctor_name_lst)):
            try:
                temp = doctor_name_lst[i].text

                df.at[i, 'name'] = temp
            except:
                print(i)


        for i in range(len(doctor_details)):
            try:
                temp  = doctor_details[i].text
                if i%2==0:
                    df.at[i//2, 'address'] = temp

                else:
                    df.at[i//2, 'mobile_number'] = temp

            except:
                pass


        print(len(doctor_name_lst),len(doctor_details))


        df.to_csv(f'jindal.csv',index=False)
