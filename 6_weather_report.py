#6) implement a python program to perform weather reporting. Ask user to provide station #name, start date and end date. Export weather details in csv file
# import the package and function

import wwo_hist

#1. api1=retrieve_this_location(api_key, location, start_date, end_date, frequency, response_cache_path)

#api_key="mykey"
##location="singapore"
##start_date="09-SEP-2020"
##end_date="11-SEP-2020"
#print("Enter the station name:")
#location=input()
#print("Enter the start date:")
#start_date=input()
#print("Enter the end date")
#end_date=input()
#frequency="3"
#response_cache_path=None
#wwo_hist.retrieve_this_location(api_key, location, start_date, end_date, frequency,response_cache_path)


#2. api2=retrieve_hist_data(api_key, location_list, start_date, end_date, frequency, location_label=False, export_csv=True, store_df=False, response_cache_path=None)

api_key="mykey"
print("Enter the station name:")
location=input()
location_list=[]
location_list.append(location)
print("Enter the start date:")
start_date=input()
print("Enter the end date")
end_date=input()
frequency=3

wwo_hist.retrieve_hist_data(api_key, location_list, start_date, end_date, frequency, location_label=False, export_csv=True, store_df=False, response_cache_path=None)

