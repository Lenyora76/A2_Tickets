import pandas as pd
from datetime import datetime

today = datetime(datetime.today().year, datetime.today().month, datetime.today().day, 12, 0, 0)  # clunky


def rsab(bond=None, trade_yield_or_price=0.00, number_of_units=0, transaction_date=today, unexcor_code='FYN544',
         bank_broker=None, trader=None, counterparty='Government of South Africa'):

    # load default ticket template, unexcor portfolio mapping and bank counterparties
    rsab_tkt = pd.read_excel('Template_BondSpot.xlsx', index_col='Key')
    u_codes = pd.read_excel('A2_Booking_Parameters.xlsx', sheet_name='Unexcor_Codes', index_col='Unexcor Code')

    # populate template with trade details
    rsab_tkt.loc['tradeReference', 'Value'] = bond
    rsab_tkt.loc['transactionDate', 'Value'] = transaction_date
    rsab_tkt.loc['book', 'Value'] = u_codes.loc[unexcor_code, 'Portfolio']
    rsab_tkt.loc['counterparty'] = f'{counterparty}|Global Markets Liberty'
    rsab_tkt.loc['numberOfUnits', 'Value'] = number_of_units
    rsab_tkt.loc['specialInfo1', 'Value'] = bank_broker
    rsab_tkt.loc['specialInfo2', 'Value'] = trader
    rsab_tkt.loc['bond', 'Value'] = bond
    rsab_tkt.loc['tradeYieldOrPrice', 'Value'] = trade_yield_or_price
    rsab_tkt.loc['nonStandardSettlement', 'Value'] = False  # Check that it doesn't get evaluated on export
    return rsab_tkt

# output Successfully uploaded into Alchemy