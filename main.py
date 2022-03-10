
from time import strftime
import pandas as pd
import datetime 
from pandas.tseries.offsets import BDay
import tkinter as tk
from tkinter import filedialog as fd


# create the root window
root = tk.Tk()
root.title('Reporter')
root.resizable(False, False)
root.geometry('300x150')
#Assign empty global variables for directories
vttk_directory = None
likp_directory = None

#Functionm to generate report
def generate_report():
    vttk = vttk_directory
    likp = likp_directory

    #Adding DataBase path
    DFDB_path = "DSRDB 2022.xlsx"
    #Creating dataframes for bought reports and Database
    df_vttk = pd.read_excel(vttk)
    df_likp = pd.read_excel(likp)
    DFDB = pd.read_excel(DFDB_path)
    #Filtering Dataframes for the data we need 
    df_vttk_col = df_vttk[['Shipment #', 'From', 'To', 'Departure DT', 'Forwarder','Forwarder Name','CAR Regular','QTY Regular']]
    df_likp_col = df_likp[['Shipment #', 'Receiving Ship-to Name']]

    #Remove duplicates
    df_vttk_col = df_vttk_col.drop_duplicates(subset = 'Shipment #')
    df_likp_col = df_likp_col.drop_duplicates(subset = 'Shipment #')

    #Merging reports on Shipment inner so we remove the data we dont need
    report = pd.merge(df_vttk_col, df_likp_col, on='Shipment #', how = 'inner')


    #Creating forwarder filter
    forwarder_filter = (report['Forwarder Name'] == 'AUTOTRASPORTI RUTILLI ADOLFO S.R.L.') | (report['Forwarder Name'] == 'BF Global Logistics B.V') | (report['Forwarder Name'] == 'Merpo Logistics')

    #Creating Shops filter
    shop_filter = (report['Receiving Ship-to Name'] == 'JC # 8206 - PARNDORF') | (report['Receiving Ship-to Name'] == 'JC # 8214 - SICILY OUTLET') | (report['Receiving Ship-to Name'] == 'JC # 8221 - KILDARE OUTLET') | (report['Receiving Ship-to Name'] == 'JC # 8217 - SANREMO OUTLET') | (report['Receiving Ship-to Name'] == 'JC # 8216 - CASTEL ROMANO') | (report['Receiving Ship-to Name'] == 'JC # 8208 - SERRAVALLE') |(report['Receiving Ship-to Name'] == 'JC # 8200 - Fidenza Village') |(report['Receiving Ship-to Name'] == 'JC # 8164 - METZINGEN') |(report['Receiving Ship-to Name'] == 'JC # 8123 - THE MALL FLORENCE') |(report['Receiving Ship-to Name'] == 'JC # 8218 - NOVENTA') | (report['Receiving Ship-to Name'] == 'JC # 8115 - BICESTER') | (report['Receiving Ship-to Name'] == 'JC # 8125 - LA VALLEE') | (report['Receiving Ship-to Name'] == 'JC # 8162 - INGOLSTADT VILLAGE') | (report['Receiving Ship-to Name'] == 'JC # 8187 - FOXTOWN OUTLET') | (report['Receiving Ship-to Name'] == 'JC # 8127 - LA ROCA') | (report['Receiving Ship-to Name'] == 'JC # 8179 - LAS ROZAS') | (report['Receiving Ship-to Name'] == 'JC # 8209 - ROERMOND') | (report['Receiving Ship-to Name'] == 'JC # 8200 - FIDENZA VILLAGE') | (report['Receiving Ship-to Name'] == 'JC # 8103 - MILAN')

    #Applyint filters
    report = report.loc[forwarder_filter]
    report = report.loc[shop_filter]

    #Changing format for date columns
    report['Departure DT'] = pd.to_datetime(report['Departure DT'], format="%d.%m.%y")
    # DFDB['Departure DT']  = pd.to_datetime(DFDB['Departure DT'], format="%d/%m/%y")
    # DFDB['Estimated Delivery Date']  = pd.to_datetime(DFDB['Departure DT'], format="%d/%m/%y")
    report = report.reset_index(drop=True)

    #Adding estimate delivery date column
    report['Estimated Delivery Date'] = None
    report['Estimated Delivery Date'] = pd.to_datetime(report['Estimated Delivery Date'])

    #Looping column 'Receiving Ship-to Name' and applying conditions to 'Estimated Delivery Date' by adding Business day
    for k, v in enumerate(report['Receiving Ship-to Name']):

        if (v == 'JC # 8209 - ROERMOND'):
            report.at[k, 'Estimated Delivery Date'] = report['Departure DT'][k] + BDay(1)

        elif (v == 'JC # 8103 - MILAN') | (v == 'JC # 8123 - THE MALL FLORENCE') | (v == 'JC # 8125 - LA VALLEE') | (v == 'JC # 8162 - INGOLSTADT VILLAGE') | (v == 'JC # 8164 - METZINGEN') | (v == 'JC # 8200 - Fidenza Village') |(v == 'JC # 8208 - SERRAVALLE') | (v == 'JC # 8218 - NOVENTA'):
            report.at[k,'Estimated Delivery Date'] = report['Departure DT'][k] + BDay(2)

        elif (v == 'JC # 8115 - BICESTER') | (v == 'JC # 8127 - LA ROCA') | (v == 'JC # 8179 - LAS ROZAS') | (v == 'JC # 8187 - FOXTOWN OUTLET') | (v == 'JC # 8206 - PARNDORF') | (v == 'JC # 8216 - CASTEL ROMANO') | (v == 'JC # 8217 -  SAN REMO'):
            report.at[k,'Estimated Delivery Date'] = report['Departure DT'][k] + BDay(3)

        elif (v == 'JC # 8217 - SANREMO OUTLET'):
            report.at[k, 'Estimated Delivery Date'] = report['Departure DT'][k] + BDay(5)

        elif (v == 'JC # 8214 - SICILY OUTLET') | (v == 'JC # 8221 - KILDARE OUTLET'):
            report.at[k, 'Estimated Delivery Date'] = report['Departure DT'][k] + BDay(6)

    #Rename Column to Store 
    report.rename(columns={'Receiving Ship-to Name': 'Store'},inplace = True)
    
    #Change index position
    report = report.reindex(columns=['Shipment #', 'From', 'To', 'Departure DT', 'Forwarder','Forwarder Name', 'Estimated Delivery Date','Store', 'CAR Regular', 'QTY Regular'])
    
    #report = report.set_index('Shipment #')
    #Change date format for DFDB and report 
    DFDB['Estimated Delivery Date'] = DFDB['Estimated Delivery Date'].dt.strftime('%d/%m/%y')
    DFDB['Departure DT'] = DFDB['Departure DT'].dt.strftime('%d/%m/%y')
    DFDB.to_excel('DFDB.xlsx')
    report['Departure DT'] = report['Departure DT'].dt.strftime('%d/%m/%y')
    report['Estimated Delivery Date'] = report['Estimated Delivery Date'].dt.strftime('%d/%m/%y')
    report.to_excel('r.xlsx')
    #Assign current date to variable
    now = datetime.datetime.now().strftime('%d.%m.%y')

    #Creating new column 
    #report['OnTime'] = ""

    #Creating mask for concat 
  
    df = pd.concat([DFDB, report], axis=0)
    df.drop_duplicates(subset= 'Shipment #')
    #Save database
    df.set_index('Shipment #')
    # df = df.drop(['Unnamed: 0'], axis=1)
    df.to_excel("DSRDB 2022.xlsx")
   

    df['Estimated Delivery Date'] = pd.to_datetime(df['Estimated Delivery Date'], dayfirst=True)
    df['Departure DT'] = pd.to_datetime(df['Departure DT'], dayfirst=True)

    #Masking date to add to database 
    filter_date = df['Estimated Delivery Date'] >= datetime.datetime.today()
    df['Departure DT'] = df['Departure DT'].dt.strftime('%d/%m/%Y')
    df['Estimated Delivery Date'] = df['Estimated Delivery Date'].dt.strftime('%d/%m/%Y')
    ready_report = df.loc[filter_date]
    ready_report = ready_report.set_index('Shipment #')

    #ready_report = ready_report.drop(['Unnamed: 0', 'OnTime'],axis=1)
    ready_report.to_excel('DSR '+ str(now) +'.xlsx')

def select_file_vttk():
    global vttk_directory

    filetypes = (
        ('text files', '*.xlsx'),
        ('All files', '*.*')
    )

    vttk_directory = fd.askopenfilename(
        title='Open a VTTK file',
        initialdir='/',
        filetypes=filetypes)


def select_file_likp():
    global likp_directory

    filetypes = (
        ('text files', '*.xlsx'),
        ('All files', '*.*')
    )

    likp_directory = fd.askopenfilename(
        title='Open a LIKP file',
        initialdir='/',
        filetypes=filetypes)

# open button
vttk_button = tk.Button(
    root,
    text='Open a VTTK File',
    command=select_file_vttk
)

likp_button = tk.Button(
    root,
    text='Open a LIKP File',
    command=select_file_likp
)

report_button = tk.Button(
    root,
    text='Generate Report',
    command=generate_report
)

vttk_button.pack(expand=True)
likp_button.pack(expand=True)
report_button.pack(expand=True)

# run the application
root.mainloop()

