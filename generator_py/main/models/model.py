
#Models.py

class Covid(object):

    def __init__(self,province_state,country_region,latitude,longitude,date,number_cases,status_cases_type):
        self.province_state=province_state
        self.country_region=country_region
        self.latitude=latitude
        self.longitude=longitude
        self.date=date
        self.number_cases=number_cases
        self.status_cases_type=status_cases_type
    
    def toString(self):
        print("Province State:" , self.province_state,  "Country Region:",  self.country_region)
        print("Latitude:" , self.latitude, " Longitude: " , self.longitude)
        
    