#to use, save login credentials in .env file in ./directory

from simple_salesforce import Salesforce
from decouple import config
from arcgis import GIS

sf = Salesforce(username=config('SALESFORCE_USER'), 
                password=config('SALESFORCE_PASS'),
                security_token=config("SALESFORCE_TOKEN")
                )

gis = GIS("https://dlba.maps.arcgis.com", config('AGO_USER'), config("AGO_PASS"))