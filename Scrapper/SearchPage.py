import time

from Utilities.common_utilities import CommonUtilites
import Locators.SearchPageLocators as Spl
import Locators.ResultPageLocators as Rpl
import pytest


@pytest.mark.usefixtures('initiate_driver')
class TestSearchPage:

    def test_perform_search(self):
        cu = CommonUtilites()
        cu.click_element(element_locator=Spl.provider_city_radioButton)
        cu.send_text(element_locator=Spl.city_field, text= 'New York')
        cu.click_element(element_locator=Spl.search_button)

        doctor_name_lst = cu.get_multiple_button(element_locator=Rpl.doctor_name)
        doctor_details = cu.get_multiple_button(element_locator=Rpl.doctor_address)

        print("doctor name")
        for i in doctor_name_lst:
            print(i.text)

        print("doctor detials")
        counter = 0
        for i in doctor_details:
            try:
                print(i.text, '\n','--'*5)


                counter +=1
            except:
                pass


        print(counter, len(doctor_name_lst),len(doctor_details))
