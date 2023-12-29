import pandas as pd
import os

formatted_date = "28-11-2023"
formatted_today = "29-12-2023"

symbols = [
    "3PLAND", "AARVEEDEN", "ABSLNN50ET", "ACEINTEG", "AGROPHOS", "AKASH", "AKG", "ALPSINDUS", "AMBICAAGAR"]
symbols123 = [
    "ASHOKAMET", "AXISILVER", "BALKRISHNA", "BANARBEADS", "BANKA", "BIOFILCHEM", "CREATIVEYE", "CYBERMEDIA",
    "DHRUV", "DIVOPPBEES", "EGOLD", "ESILVER", "EUROTEXIND", "FIBERWEB", "FMNL", "GATECHDVR", "GLFL", "GSEC10YEAR",
    "HDFCBSE500", "HDFCLOWVOL", "HDFCMID150", "HDFCMOMENT", "HDFCNEXT50", "HDFCNIF100", "HDFCQUAL", "HEADSUP", "HEALTHY",
    "JAIPURKURT", "KANANIIND", "KHAITANLTD", "KHANDSE", "KOTAKALPHA", "KOTAKCONS", "KOTAKLOVOL", "KOTAKMNC", "LAXMICOT",
    "LCCINFOTEC", "LIBAS", "MADHAV", "MALUPAPER", "MCL", "MITTAL", "MOGSEC", "MOHEALTH", "MOHITIND", "MOLOWVOL",
    "MORARJEE", "MOVALUE", "NARMADA", "NGIL", "ORIENTALTL", "ORIENTLTD",
    "ORTINLAB", "PEARLPOLY", "PIGL", "PNC", "RADAAN", "ROML", "SAGARDEEP", "SAMPANN", "SANGINITA", "SECURCRED", "SHANTI",
    "SHIVAMILLS", "SHYAMTEL", "SILGO", "TERASOFT", "TIJARIA", "TNTELE", "TREEHOUSE", "UTISXN50", "VCL", "VIJIFIN", "VINEETLAB",
    "VIVIDHA"
]
symbol = "KOTAKCONS"
directory_path = "/Users/omkar/Downloads"

def read_csv_file(formatted_date, formatted_today, symbol, directory_path):
    # Create the file name based on the provided parameters
    file_name = f"{formatted_date}-TO-{formatted_today}-{symbol}-ALL-N.csv"
    # Construct the full file path
    file_path = os.path.join(directory_path, file_name)

    # Check if the file exists
    if os.path.exists(file_path):
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(file_path)
        last_clumn_name = df.columns[-1]
        new_last_clumn_name = "del_per"
        df = df.rename(columns={last_clumn_name: new_last_clumn_name})
        return df
    else:
        print(f"File not found: {file_path}")
        return None

def calculate_del_per(data_frame):
    if(data_frame is not None):
        del_per = data_frame["del_per"]
        # calculate if del_per of last day is greater than all previous days and del_per of any day is not greater than 95
        if(del_per.iloc[-1] > del_per.iloc[:-1].max() and del_per.max() < 95):
            print("Buy this stock", symbol)
        else:
            print("Don't buy this stock", symbol)
# calculate if del_per is of last day is greater than all previous days and del_per of any day is not greater than 95
for symbol in symbols:
    data_frame = read_csv_file(formatted_date, formatted_today, symbol, directory_path)
    calculate_del_per(data_frame)


