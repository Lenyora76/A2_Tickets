from rsa_bond import rsab
from rsab_fwd import rsab_fwd
from datetime import datetime


def rsa_bond_ed(bond=None, forward_yield=0.10, number_of_units=0, trader=None, repo_rate=0.00, far_maturity_date=None,
                trade_yield_or_price=0.00, bank_broker=None):

    # ALM MRM facing externaly, booked into custody account: Spot
    book = 'A:LG:ALM MRM ANN AND GCB:GOVBND:U'
    counterparty='Government of South Africa'
    mkt_ext_spot_tkt = rsab(bond, trade_yield_or_price, number_of_units, trader, bank_broker, book, counterparty)

    # ALM MRM facing Treasury Internal: Spot
    book = 'A:IN:ALM MRM ANN AND GCB:INTERNAL RISK:U'
    counterparty = 'Libfin Treasury'
    mkt_int_spot_tkt = rsab(bond, trade_yield_or_price, -number_of_units, trader, bank_broker, book, counterparty)

    # Treasury facing ALM MRM Internal: Spot
    book = 'A:IN:ALM TREASURY:INTERNAL RISK:U'
    counterparty = 'LibFin Ann and GCB'
    trs_int_spot_tkt = rsab(bond, trade_yield_or_price, number_of_units, trader, bank_broker, book, counterparty)

    # Treasury facing ED & NRR Internal: Fwd
    book = 'A:IN:ALM TREASURY:INTERNAL RISK NRR CURVE:U'
    counterparty = 'Liberty Libfin Emdedded Derivs R'
    trs_int_fwd_tkt = rsab_fwd(bond, forward_yield, -number_of_units, trader, repo_rate, far_maturity_date, book,
                               counterparty)

    # ED & NRR facing Treasury Internal: Fwd
    book = 'A:IN:ALM MRM EDS AND NRR:INTERNAL:NRR CURVE:V'
    counterparty = 'Libfin Treasury'
    ed_int_fwd_tkt = rsab_fwd(bond, forward_yield, -number_of_units, trader, repo_rate, far_maturity_date, book,
                              counterparty)

    # mkt_ext_spot_tkt.to_excel(f'test_{bond}_ext_spot.xlsx')
    # mkt_int_spot_tkt.to_excel(f'test_{bond}_int_spot_mkt.xlsx')
    # trs_int_spot_tkt.to_excel(f'test_{bond}_int_spot_trs.xlsx')
    # trs_int_fwd_tkt.to_excel(f'test_{bond}_int_fwd_trs.xlsx')
    # ed_int_fwd_tkt.to_excel(f'test_{bond}_int_fwd_ed.xlsx')

    return mkt_ext_spot_tkt


m_date = datetime(2020, 6, 17, 18, 0, 0)
tkt = rsa_bond_ed(bond='R186', trade_yield_or_price=0.1, forward_yield=0.102, number_of_units=100, trader='Jacob',
                  repo_rate=0.0560, far_maturity_date=m_date, bank_broker='SBBJ')

print(tkt)



