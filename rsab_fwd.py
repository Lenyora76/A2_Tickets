import pandas as pd
from datetime import datetime ,timedelta

today = datetime(datetime.today().year, datetime.today().month, datetime.today().day, 12, 0, 0)  # clunky


def rsab_fwd(bond=None, forward_yield=0.10, number_of_units=0, transaction_date=today, trader=None, repo_rate=0.00,
             counterparty=None, book='A:LG:ALM TREASURY:REPBND:U', far_maturity_date=None):

    # load default ticket template and bank counterparties
    rsab_fwd_tkt = pd.read_excel('Template_BondFwd.xlsx', index_col='Key')
    # banks = pd.read_excel('A2_Booking_Parameters.xlsx', sheet_name='Banks', index_col='Bank Code')

    yyyy = far_maturity_date.strftime("%Y")
    mm = far_maturity_date.strftime("%m")
    dd = far_maturity_date.strftime("%d")

    trade_ref = f'{yyyy}{mm}{dd}_{bond}_BNDFWD_{counterparty}'

    rsab_fwd_tkt.loc['tradeReference'] = trade_ref
    rsab_fwd_tkt.loc['transactionDate'] = transaction_date
    rsab_fwd_tkt.loc['book'] = book
    rsab_fwd_tkt.loc['counterparty'] = counterparty+'|Global Markets Liberty'
    rsab_fwd_tkt.loc['numberOfUnits'] = number_of_units
    rsab_fwd_tkt.loc['specialInfo1'] = repo_rate
    rsab_fwd_tkt.loc['specialInfo2'] = trader
    rsab_fwd_tkt.loc['bond'] = bond
    rsab_fwd_tkt.loc['unadjustedMaturityDate'] = far_maturity_date
    rsab_fwd_tkt.loc['forwardYieldOrPrice'] = forward_yield

    return rsab_fwd_tkt


# output Successfully uploaded into Alchemy
