from Utilities.search_data_utility import *
import pytest
from config.control import *

@pytest.mark.usefixtures('initiate_driver')
class TestSearchPage:

    def test_perform_search(self):
        df = pd.read_excel(excel_location)
        d = [i for i in list(df['City'][:1])]
        lis = [(i, x) for i, x in enumerate(d)]
        final_doctor_name=[]
        final_doctor_detail = []
        all_city=[]
        for temp in lis:
            x, city = temp
            city_temp=[]
            doctor_name_lst, doctor_details = Util().get_all_data('Glendale')
            if doctor_name_lst == [] and doctor_details == []:
                continue
            else:
                city_temp+=[city for i in range(len(doctor_name_lst))]
                final_doctor_name+=doctor_name_lst
                final_doctor_detail+=doctor_details
            all_city+=city_temp
        Util().save_csv(all_city, final_doctor_name, final_doctor_detail)
