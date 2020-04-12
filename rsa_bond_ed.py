from rsa_bond import rsab
from rsab_fwd import rsab_fwd
from datetime import datetime

today = datetime(datetime.today().year, datetime.today().month, datetime.today().day, 12, 0, 0)  # clunky


def rsa_bond_ed(bond=None, trade_yield_or_price=0.00, number_of_units=0, transaction_date=today, unexcor_code='FYN544',
                bank_broker=None, trader=None, counterparty='Government of South Africa', forward_yield=0.10,
                repo_rate=0.00, book='A:LG:ALM TREASURY:REPBND:U', far_maturity_date=None):

    mkt_ext_spot_tkt = rsab(bank_broker=)
    mkt_int_spot_tkt = rsab()


