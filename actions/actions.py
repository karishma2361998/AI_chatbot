# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker,FormValidationAction
from rasa_sdk.events import SlotSet
from rasa_sdk.types import DomainDict
from rasa_sdk.executor import CollectingDispatcher
from database_connectivity4 import DataUpdate
from datetime import date
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from rasa_sdk.executor import CollectingDispatcher
import requests
from bs4 import BeautifulSoup


class ActionCarHatchback(Action):

     def name(self) -> Text:
         return "action_car_hatchback"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
         r = requests.get('https://www.marutisuzuki.com/')
         soup = BeautifulSoup(r.text,'html.parser')
         result1 = soup.find("li",id="0-thirdLevel-1")
         hatch1 = result1.text[1:]
         result2 = soup.find("li",id="1-thirdLevel-1")
         hatch2 = result2.text[1:]
         result3 = soup.find("li",id="2-thirdLevel-1")
         hatch3 = result3.text[1:]
         result4 = soup.find("li",id="3-thirdLevel-1")
         hatch4 = result4.text[1:]


         hatch = hatch1,hatch2,hatch3,hatch4

         hatchback = f"{hatch} : Select the model of your choice"

         dispatcher.utter_message(text=hatchback)

         return[]


class ActionCarSedan(Action):

     def name(self) -> Text:
         return "action_car_sedan"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
         r = requests.get('https://www.marutisuzuki.com/')
         soup = BeautifulSoup(r.text,'html.parser')

         result4 = soup.find("li",id="4-thirdLevel-2")
         sed= result4.text[1:]

         sedan = f"{sed} : Want to go for dzire then type new dzire"

         dispatcher.utter_message(text=sedan)

         return[]

class ActionCarSuvmuv(Action):

     def name(self) -> Text:
         return "action_car_suvmuv"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
         r = requests.get('https://www.marutisuzuki.com/')
         soup = BeautifulSoup(r.text,'html.parser')

         result6 = soup.find("li",id="5-thirdLevel-3")
         muv1=result6.text[1:]
         result7 = soup.find("li",id="6-thirdLevel-3")
         muv2=result7.text[1:]
         result8 = soup.find("li",id="7-thirdLevel-3")
         muv3=result8.text[1:]
         muv = muv1,muv2,muv3

         muvsuv = f"{muv} : Select the model of your choice"
         dispatcher.utter_message(text=muvsuv)

         return[]

class ActionCarVan(Action):

     def name(self) -> Text:
         return "action_car_van"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
         r = requests.get('https://www.marutisuzuki.com/')
         soup = BeautifulSoup(r.text,'html.parser')

         result9 = soup.find("li",id="8-thirdLevel-4")
         vann= result9.text[1:]
         van = f"{vann} : Want to go for eeco then type eeco"

         dispatcher.utter_message(text=van)

         return[]





class ActionCarBrochures(Action):

     def name(self) -> Text:
         return "action_car_brochures"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
         entity = tracker.latest_message['entities'][0]['value']
         
       
         if entity == "ALTO 800":
            dispatcher.utter_message(text="https://marutistoragenew.blob.core.windows.net/msilintiwebpdf/Alto_Brand_Brochure.pdf")

         elif entity == "Alto":
            dispatcher.utter_message(text="https://marutistoragenew.blob.core.windows.net/msilintiwebpdf/Alto_Brand_Brochure.pdf")

         elif entity == "S-Pressco":
            dispatcher.utter_message(text="https://marutistoragenew.blob.core.windows.net/msilintiwebpdf/S-Presso_product_brochure.pdf")

         elif entity == "s-presso":
            dispatcher.utter_message(text="https://marutistoragenew.blob.core.windows.net/msilintiwebpdf/S-Presso_product_brochure.pdf")

         elif entity == "Celerio":
            dispatcher.utter_message(text="https://marutistoragenew.blob.core.windows.net/msilintiwebpdf/All_New_Celerio.pdf")

         elif entity == "celerio":
            dispatcher.utter_message(text="https://marutistoragenew.blob.core.windows.net/msilintiwebpdf/All_New_Celerio.pdf")

         elif entity == "NEW DZIRE":
            dispatcher.utter_message(text="https://marutistoragenew.blob.core.windows.net/msilintiwebpdf/Maruti_Dzire_Product_Brochure.PDF")

         elif entity == "New Dzire":
            dispatcher.utter_message(text="https://marutistoragenew.blob.core.windows.net/msilintiwebpdf/Maruti_Dzire_Product_Brochure.PDF")

         elif entity == "NEW ERTIGA":
            dispatcher.utter_message(text="https://marutistoragenew.blob.core.windows.net/msilintiwebpdf/Ertiga_Brand_Brochure.pdf")

         elif entity == "ertiga":
            dispatcher.utter_message(text="https://marutistoragenew.blob.core.windows.net/msilintiwebpdf/Ertiga_Brand_Brochure.pdf")

         elif entity == "New Swift":
            dispatcher.utter_message(text="https://marutistoragenew.blob.core.windows.net/msilintiwebpdf/New_Swift_product_broucher.pdf")

         elif entity == "swift":
            dispatcher.utter_message(text="https://marutistoragenew.blob.core.windows.net/msilintiwebpdf/New_Swift_product_broucher.pdf")

         elif entity == "Wagon R":
            dispatcher.utter_message(text="https://marutistoragenew.blob.core.windows.net/msilintiwebpdf/WagonR_Brand_Brochure.pdf")

         elif entity == "wagon r":
            dispatcher.utter_message(text="https://marutistoragenew.blob.core.windows.net/msilintiwebpdf/WagonR_Brand_Brochure.pdf")               

         elif entity == "Vitara Brezza":
            dispatcher.utter_message(text="https://marutistoragenew.blob.core.windows.net/msilintiwebpdf/Maruti-Suzuki-Brezza-Brochure.pdf")

         elif entity == "vitara brezza":
            dispatcher.utter_message(text="https://marutistoragenew.blob.core.windows.net/msilintiwebpdf/Maruti-Suzuki-Brezza-Brochure.pdf")

         elif entity == "Eeco":
            dispatcher.utter_message(text="https://marutistoragenew.blob.core.windows.net/msilintiwebpdf/Eeco_Brand_brochure.pdf")

         elif entity == "eeco":
            dispatcher.utter_message(text="https://marutistoragenew.blob.core.windows.net/msilintiwebpdf/Eeco_Brand_brochure.pdf")  
  

         else:
            dispatcher.utter_message(text="I did not understand")
            
         return []


class ActionLocationLink(Action):

    def name(self) -> Text:
        return "action_location_link"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Go to link to get your nearby showroom location and come back to fill personal details to book your appointment")
        dispatcher.utter_message(text="https://www.marutisuzuki.com/dealer-showrooms")
        return []


class ActionStoreData(Action):

    def name(self) -> Text:
        return "action_store_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name")
        state = tracker.get_slot("state")
        city = tracker.get_slot("city")
        dealer_name = tracker.get_slot("dealer_name")
        model_name = tracker.get_slot("model_name")
        date = tracker.get_slot("date")
        time = tracker.get_slot("time")
        email = tracker.get_slot("email")
        DataUpdate(tracker.get_slot("name"),tracker.get_slot("email"),tracker.get_slot("state"),tracker.get_slot("city"),tracker.get_slot("dealer_name"),tracker.get_slot("model_name"),tracker.get_slot("date"),tracker.get_slot("time"))
        return []

class ValidateDateForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_date_form"

    def validate_date(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `date` value."""
        
        def numOfDays(date1, date2):
            number=(date2-date1).days
            return number
     
        date1 = date.today()
        date2 = slot_value
        format_str = '%Y-%m-%d'
        datetime_obj = datetime.datetime.strptime(date2, format_str)
        number1=numOfDays(date1, datetime_obj.date())
        if number1 >=5:
            print(number1)
            return {"date": slot_value}
        else:
            dispatcher.utter_message(text=f"Date must be after 5 days from today's date")
            return {"date": None}


class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        SendEmail(
            tracker.get_slot("email"),
            name = tracker.get_slot("name"),
            date = tracker.get_slot("date"),
            time = tracker.get_slot("time")       
        )
        dispatcher.utter_message("Thanks for providing the details. We have sent you a mail at {}".format(tracker.get_slot("email")))
        return []

def SendEmail(toaddr,name,date,time):
    fromaddr = "siddhijain268@gmail.com"
    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr
    msg['Subject'] = 'Booking appointment Details'
    name1 = name
    date1 = date
    time1 = time
    message = "{} your booking in fixed at {} on {}".format(name1,date1,time1)
    body = message
    msg.attach(MIMEText(body, 'plain'))
    # open the file to be sent
    # filename = "/home/ashish/Downloads/webinar_rasa2_0.png"
    # attachment = open(filename, "rb")
    #
    # # instance of MIMEBase and named as p
    # p = MIMEBase('application', 'octet-stream')
    #
    # # To change the payload into encoded form
    # p.set_payload((attachment).read())
    #
    # # encode into base64
    # encoders.encode_base64(p)
    #
    # p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    #
    # # attach the instance 'p' to instance 'msg'
    # msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()


    # Authentication
    try:
        s.login(fromaddr, "Kapil@123")
        text = msg.as_string()
        # sending the mail
        s.sendmail(fromaddr, toaddr, text)
    except:
        print("An Error occured while sending email.")
    finally:
        # terminating the session
        s.quit()
