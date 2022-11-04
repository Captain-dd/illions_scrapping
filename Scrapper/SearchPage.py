from Utilities.search_data_utility import *


@pytest.mark.usefixtures('initiate_driver')
class TestSearchPage:

    def test_perform_search(self):
        df = pd.read_excel('city_lst.xlsx')
        d = [i for i in list(df['City'][:288])]
        lis = [(i, x) for i, x in enumerate(d)]

        for temp in lis:
            x, city = temp
            doctor_name_lst, doctor_details = Util().get_all_data(city)
            Util().save_csv(city, doctor_name_lst, doctor_details)
