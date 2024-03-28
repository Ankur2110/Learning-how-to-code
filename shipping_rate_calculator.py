
import pandas as pd

# Load the Excel file
df = pd.read_excel("Delhivery_pincodes.xlsx")

# Create a dictionary mapping pincode to state
pincode_state_mapping = {pincode: state for pincode, state in zip(df['Pincode'], df['State'])}

# Create a dictionary mapping pincode to state
ODA_state_mapping = {pincode: ODA_status for pincode, ODA_status in zip(df['Pincode'], df['ODA'])}

# Function to get state based on pincode
def get_state_from_pincode(pincode):
    return pincode_state_mapping.get(pincode)

# Function to get ODA status based on pincode
def get_ODAstatus_from_pincode(pincode):
    ODA_status = ODA_state_mapping.get(pincode)
    if ODA_status == 1:
         return True
    else:
        return False
    
def IsNDinbound(state):
     if state =="Delhi":
          return True
     else:
          return False
    


# Get pickup pincode from user
pickup_pincode = int(input("Enter pickup pincode: "))
pickup_state = get_state_from_pincode(pickup_pincode)




# Get delivery pincode from user
delivery_pincode = int(input("Enter delivery pincode: "))
delivery_state = get_state_from_pincode(delivery_pincode)

print(IsNDinbound(delivery_state))

# Get user input
pickup_location = pickup_state
delivery_location = delivery_state
num_boxes = int(input("Enter number of boxes: "))
weight_per_box = float(input("Enter weight of each box (in kg): "))
length_per_box = float(input("Enter length of each box (in cm): "))
width_per_box = float(input("Enter width of each box (in cm): "))
height_per_box = float(input("Enter height of each box (in cm): "))
invoice_value = float(input("What is the invoice value (in INR): "))


Global_GST = 18
    
def get_base_rate(pickup_location, delivery_location, zone_locations,zone_base_rates):
    pickup_zone = get_zone(pickup_location, zone_locations)
    delivery_zone = get_zone(delivery_location, zone_locations)

    assert pickup_zone is not None, "Invalid pickup location"
    assert delivery_zone is not None, "Invalid delivery location"

    assert pickup_zone in zone_base_rates, "Base rate not available for pickup zone"
    assert delivery_zone in zone_base_rates[pickup_zone], "Base rate not available for delivery zone"

    base_rate = zone_base_rates[pickup_zone][delivery_zone]
    print("base_rate",base_rate)
    return base_rate


def shipment_rate_calculator(baserate, FSC, AWB, FOV, Handling_Charges, charged_weight, weight_per_box, unit_box_max_weight_limit, min_chargeable_amount, invoice_value, ODA_status, min_ODA_charges, ODA_rate, New_Delhi_inbound_status, Dimensional_Handling_Charges,  min_dimensional_handling_charges ):
    base_charges = charged_weight*baserate
    FSC_charges = max(base_charges*(FSC)/100, 0.002*invoice_value)
    print ("FSC Charges", FSC_charges)
    overweight_charges = 0
    ODA_charges = 0
    Environmental_charges = 0
    Dimensional_charges = 0
    if ODA_status:
        ODA_charges = max(charged_weight*ODA_rate,min_ODA_charges)
    print("ODACharges", ODA_charges)
    if Dimensional_Handling_Charges:
        Dimensional_charges = max(charged_weight*Dimensional_Handling_Charges, min_dimensional_handling_charges)
    print("DimensionalCharges", Dimensional_charges)
    if New_Delhi_inbound_status:
        Environmental_charges = 0.5*charged_weight
    print("Environmental Charges", Environmental_charges)
    if weight_per_box >unit_box_max_weight_limit:
       overweight_charges = Handling_Charges*(weight_per_box)
    print("Overweight_Charges", overweight_charges)
    total_charges = (base_charges+ FSC_charges+ AWB + FOV + overweight_charges + ODA_charges + Environmental_charges+ Dimensional_charges)*(100+Global_GST)/100
    return max(total_charges, min_chargeable_amount)

def get_zone(location, zone_locations):
    for zone, locations in zone_locations.items():
        if location in locations:
            return zone
    return None  # Return None if location is not found in any zone

def calculate_volume(length_per_box, width_per_box, height_per_box):
                     volume = length_per_box*width_per_box*height_per_box
                     return volume
                     
def calculate_charged_weight(weight_per_box, num_boxes, volume, CFT, min_chargeable_weight):
      volumetric_weight = volume/CFT
      larger_value = max(volumetric_weight, weight_per_box, min_chargeable_weight)
      return num_boxes*larger_value


      

#Delhivery specific details

D_FSC, D_AWB, D_FOV, D_Handling_charges = 15, 250, 150, 3
D_unit_box_max_weight_limit = 400
D_min_chargeable_amount = 350
D_min_chargeable_weight =20
D_CFT = 2831.68

D_Dimensional_Handling_Charges = 0
D_min_Dimnensional_handling_charges = 0

Delhivery_ODA_Status = get_ODAstatus_from_pincode(delivery_pincode)
Delhivery_min_ODA_Charges = 750
Delhivery_ODA_rate = 4
Delhivery_New_Delhi_inbound_status = IsNDinbound(delivery_state)



Delhivery_zone_locations = {
    "N1": ["Delhi", "UP", "Haryana", "Rajasthan"],
    "N2": ["Chandigarh", "Punjab", "HP", "Uttarakhand", "J&K", "Ladakh"],
    "E": ["WB", "Odisha", "Bihar", "Jharkhand"],
    "NE": ["Assam", "Meghalaya", "Tripura", "Arunachal Pradesh", "Mizoram", "Manipur", "Nagaland", "Sikkim"],
    "W1": ["Gujarat", "Daman & Diu", "Dadra & Nagar Haveli"],
    "W2": ["Maharashtra", "Goa"],
    "S1": ["AP", "Telangana", "Karnataka", "Tamilnadu", "Puducherry"],
    "S2": ["Kerala"],
    "C": ["Madhya Pradesh", "Chhattisgarh"]
}

Delhivery_zone_base_rates = {
    "N1": {"N1": 5.2, "N2": 5.2, "E": 8.5, "NE": 10.6, "W1": 6.1, "W2": 7.3, "S1": 8.5, "S2": 11.5, "C": 6.1},
    "N2": {"N1": 5.2, "N2": 5.2, "E": 8.5, "NE": 10.6, "W1": 7.3, "W2": 7.3, "S1": 8.5, "S2": 11.5, "C": 7.3},
    "E": {"N1": 7.3, "N2": 8.5, "E": 5.2, "NE": 6.1, "W1": 7.3, "W2": 8.5, "S1": 7.3, "S2": 10.3, "C": 6.1},
    "NE": {"N1": 7.3, "N2": 8.5, "E": 6.1, "NE": 5.2, "W1": 8.5, "W2": 8.5, "S1": 8.5, "S2": 11.5, "C": 7.3},
    "W1": {"N1": 6.1, "N2": 7.3, "E": 8.5, "NE": 10.6, "W1": 5.2, "W2": 5.2, "S1": 7.3, "S2": 10.3, "C": 6.1},
    "W2": {"N1": 7.3, "N2": 7.3, "E": 8.5, "NE": 10.6, "W1": 5.2, "W2": 5.2, "S1": 6.1, "S2": 9.1, "C": 6.1},
    "S1": {"N1": 7.3, "N2": 8.5, "E": 8.5, "NE": 10.6, "W1": 7.3, "W2": 6.1, "S1": 5.2, "S2": 7.2, "C": 6.1},
    "S2": {"N1": 8.5, "N2": 8.5, "E": 8.5, "NE": 10.6, "W1": 7.3, "W2": 7.3, "S1": 5.2, "S2": 5.2, "C": 6.1},
    "C": {"N1": 6.1, "N2": 7.3, "E": 8.5, "NE": 10.6, "W1": 5.2, "W2": 6.1, "S1": 6.1, "S2": 9.1, "C": 5.2}
}


#Rocketbox specific details

R_FSC, R_AWB, R_FOV = 18, 75, 75
R_unit_box_max_weight_limit = 100
R_min_chargeable_amount = 300
R_min_chargeable_weight =20
R_CFT = 4045.25


volume = calculate_volume(length_per_box, width_per_box, height_per_box)
charged_weight = calculate_charged_weight(weight_per_box, num_boxes, volume, R_CFT, R_min_chargeable_weight)
if 0 <= charged_weight < 100:
    R_Handling_charges = 0
elif 100 <= charged_weight < 250:
    R_Handling_charges = 3
elif 250 <= charged_weight < 500:
    R_Handling_charges = 4
elif charged_weight >= 500:
    R_Handling_charges = 5

R_Dimensional_Handling_Charges = 8 if length_per_box > 152.4 or width_per_box > 152.4 or height_per_box > 152.4 else None
R_min_Dimensional_Handling_charges = 1500
rocketbox_ODA_Status = get_ODAstatus_from_pincode(delivery_pincode)
rocketbox_min_ODA_Charges = 1200
rocketbox_ODA_rate = 4
rocketbox_New_Delhi_inbound_status = IsNDinbound(delivery_state)



rocketbox_zone_locations = {
    "North 1": ["Delhi", "Ghaziabad", "Noida", "Gurugram", "Faridabad"],
    "North 2": ["Haryana except Gurugram & Faridabad", "Himachal Pradesh", "Punjab", "Rajasthan", "Uttar Pradesh except Ghaziabad & Noida","Uttarakhand"],
    "North 3": ["Jammu"],
    "West 1": ["Dadra and Nagar Haveli", "Daman and Diu", "Gujarat"],
    "West 2": ["Maharashtra", "Goa"],
    "Central-1": ["Chattisgarh", "Madhya Pradesh"],
    "South 1": ["Andhra Pradesh", "Karnataka", "Telangaga"],
    "South 2": ["Pondicherry", "Tamil Nadu"],
    "South 3": ["Kerala"],
    "East 1": ["Bihar", "Jharkhand", "Odisha", "West Bengal"],
    "East 2": ["Guwahati", "Siliguri"],
    "Special Zone": ["Andaman and Nicobar", "Rest of Jammu and Kashmir", "Rest of North East"]
}


rocketbox_zone_base_rates = {
    "North 1": {"North 1": 5.9, "North 2": 6.4, "North 3": 8.9, "West 1": 8.4, "West 2": 8.7, "Central": 9.8, "East 1": 11.5, "East 2": 15.7, "South 1": 10.0, "South 2": 10.2, "South 3": 11.5, "Special Zone": 39.6},
    "North 2": {"North 1": 6.8, "North 2": 6.3, "North 3": 9.8, "West 1": 8.8, "West 2": 8.5, "Central": 8.9, "East 1": 11.8, "East 2": 18.7, "South 1": 10.4, "South 2": 11.1, "South 3": 12.4, "Special Zone": 39.6},
    "North 3": {"North 1": 8.2, "North 2": 8.8, "North 3": 7.4, "West 1": 10.4, "West 2": 10.8, "Central": 10.2, "East 1": 13.9, "East 2": 15.3, "South 1": 11.8, "South 2": 13.3, "South 3": 13.6, "Special Zone": 39.6},
    "West 1": {"North 1": 8.6, "North 2": 8.8, "North 3": 11.1, "West 1": 5.7, "West 2": 6.3, "Central": 7.3, "East 1": 11.6, "East 2": 15.6, "South 1": 8.4, "South 2": 9.1, "South 3": 10.3, "Special Zone": 39.6},
    "West 2": {"North 1": 8.6, "North 2": 8.0, "North 3": 11.2, "West 1": 6.1, "West 2": 5.8, "Central": 7.2, "East 1": 12.0, "East 2": 15.1, "South 1": 8.9, "South 2": 9.2, "South 3": 11.2, "Special Zone": 39.6},
    "Central": {"North 1": 9.3, "North 2": 9.3, "North 3": 12.5, "West 1": 7.1, "West 2": 7.4, "Central": 7.6, "East 1": 11.9, "East 2": 16.7, "South 1": 8.8, "South 2": 9.3, "South 3": 10.5, "Special Zone": 39.6},
    "East 1": {"North 1": 10.3, "North 2": 10.6, "North 3": 13.9, "West 1": 10.3, "West 2": 10.6, "Central": 10.2, "East 1": 6.9, "East 2": 13.1, "South 1": 10.1, "South 2": 11.1, "South 3": 11.6, "Special Zone": 39.6},
    "East 2": {"North 1": 14.0, "North 2": 17.1, "North 3": 14.2, "West 1": 15.7, "West 2": 12.1, "Central": 15.1, "East 1": 12.3, "East 2": 10.4, "South 1": 15.8, "South 2": 16.5, "South 3": 17.1, "Special Zone": 22.6},
    "South 1": {"North 1": 10.2, "North 2": 10.2, "North 3": 11.7, "West 1": 8.2, "West 2": 8.1, "Central": 8.9, "East 1": 11.4, "East 2": 18.0, "South 1": 5.9, "South 2": 6.0, "South 3": 7.5, "Special Zone": 39.6},
    "South 2": {"North 1": 10.2, "North 2": 10.8, "North 3": 13.0, "West 1": 8.9, "West 2": 8.7, "Central": 9.2, "East 1": 12.3, "East 2": 17.9, "South 1": 6.1, "South 2": 6.0, "South 3": 7.6, "Special Zone": 39.6},
    "South 3": {"North 1": 11.3, "North 2": 11.7, "North 3": 13.6, "West 1": 9.3, "West 2": 9.2, "Central": 9.6, "East 1": 13.1, "East 2": 18.4, "South 1": 7.3, "South 2": 7.2, "South 3": 6.8, "Special Zone": 39.6},
    "SP1": {"North 1": 39.6, "North 2": 39.6, "North 3": 39.6, "West 1": 39.6, "West 2": 39.6, "Central": 39.6, "East 1": 39.6, "East 2": 39.6, "South 1": 39.6, "South 2": 39.6, "South 3": 39.6, "Special Zone": 18.1}

    }


class Shipper:
    def __init__(self, FSC, AWB, FOV, Handling_Charges, unit_box_max_weight_limit, min_chargeable_amount, min_chargeable_weight, CFT, zone_base_rates, zone_locations, ODA_status, min_ODA_charges, ODA_rate, New_Delhi_inbound_status, dimensional_handling_charges, min_dimensional_handling_charges):
        self.FSC = FSC
        self.AWB = AWB
        self.FOV = FOV
        self.Handling_Charges = Handling_Charges
        self.unit_box_max_weight_limit = unit_box_max_weight_limit
        self.min_chargeable_amount = min_chargeable_amount
        self.min_chargeable_weight = min_chargeable_weight
        self.CFT = CFT
        self.zone_base_rates = zone_base_rates
        self.zone_locations = zone_locations
        self.ODA_status = ODA_status
        self.min_ODA_charges = min_ODA_charges
        self.ODA_rate = ODA_rate
        self.New_Delhi_inbound_status = New_Delhi_inbound_status
        self.dimensional_handling_charges = dimensional_handling_charges
        self.min_dimensional_handling_charges = min_dimensional_handling_charges


    def calculate_rate(self, pickup_location, delivery_location, num_boxes, weight_per_box, length_per_box, width_per_box, height_per_box):
        base_rate = get_base_rate(pickup_location, delivery_location, self.zone_locations, self.zone_base_rates)
        volume = calculate_volume(length_per_box, width_per_box, height_per_box)
        charged_weight = calculate_charged_weight(weight_per_box, num_boxes, volume, self.CFT, self.min_chargeable_weight)
        return shipment_rate_calculator(base_rate, self.FSC, self.AWB, self.FOV, self.Handling_Charges, charged_weight, weight_per_box, self.unit_box_max_weight_limit, self.min_chargeable_amount,invoice_value,self.ODA_status,self.min_ODA_charges, self.ODA_rate,self.New_Delhi_inbound_status, self.dimensional_handling_charges,self.min_dimensional_handling_charges)
    
    

rocketbox = Shipper(R_FSC, R_AWB, R_FOV, R_Handling_charges, R_unit_box_max_weight_limit, R_min_chargeable_amount, R_min_chargeable_weight, R_CFT,rocketbox_zone_base_rates ,rocketbox_zone_locations, rocketbox_ODA_Status,rocketbox_min_ODA_Charges, rocketbox_ODA_rate, rocketbox_New_Delhi_inbound_status,R_Dimensional_Handling_Charges, R_min_Dimensional_Handling_charges)
rocketbox_rate = rocketbox.calculate_rate(pickup_location, delivery_location, num_boxes, weight_per_box, length_per_box, width_per_box, height_per_box)


delhivery = Shipper(D_FSC, D_AWB, D_FOV, D_Handling_charges, D_unit_box_max_weight_limit, D_min_chargeable_amount, D_min_chargeable_weight, D_CFT,Delhivery_zone_base_rates ,Delhivery_zone_locations,Delhivery_ODA_Status, Delhivery_min_ODA_Charges, Delhivery_ODA_rate, Delhivery_New_Delhi_inbound_status, D_Dimensional_Handling_Charges, D_min_Dimnensional_handling_charges)
delhivery_rate = delhivery.calculate_rate(pickup_location, delivery_location, num_boxes, weight_per_box, length_per_box, width_per_box, height_per_box)


print (delhivery_rate, rocketbox_rate)