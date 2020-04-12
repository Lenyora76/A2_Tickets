from rsa_bond import rsab
from rsab_fwd import rsab_fwd
from datetime import datetime


def ed_bond_spot(bond=None, trade_yield_or_price=None, forward_yield=None, number_of_units=None, trader=None,
                 repo_rate=None, far_maturity_date=None, bank_broker=None):
    """
    Function must be run from a spreadsheet that can price a bond forward and provide date in the correct format.
    To be used ONLY to book market facing ED Spot Bond trades.

    :param bond: e.g 'R186' str()
    :param trade_yield_or_price: Spot YTM float()
    :param forward_yield: Fwd YTM
    :param number_of_units: int()
    :param trader: Name of Trader that executed the trade str()
    :param repo_rate: float()
    :param far_maturity_date: datetime(yyyy, m, d, 18, 0, 0)
    :param bank_broker: RSAB counterparty is Gov of SA for all bonds. Used to capture Bank counterparty or broker
    :return: Excel output of all tickets (xlsx) required to book a spot bond trade in EDs as a bond forward
    """

    # ALM MRM facing externaly, booked into custody account: Spot
    book = 'A:LG:ALM MRM ANN AND GCB:GOVBND:U'
    counterparty='Government of South Africa'
    mkt_ext_spot_tkt = rsab(bond=bond, trade_yield_or_price=trade_yield_or_price, number_of_units=number_of_units,
                            trader=trader, bank_broker=bank_broker, book=book, counterparty=counterparty)

    # ALM MRM facing Treasury Internal: Spot
    book = 'A:IN:ALM MRM ANN AND GCB:INTERNAL RISK:U'
    counterparty = 'Libfin Treasury'
    mkt_int_spot_tkt = rsab(bond=bond, trade_yield_or_price=trade_yield_or_price, number_of_units=-number_of_units,
                            trader=trader, bank_broker=bank_broker, book=book, counterparty=counterparty)

    # Treasury facing ALM MRM Internal: Spot
    book = 'A:IN:ALM TREASURY:INTERNAL RISK:U'
    counterparty = 'LibFin Ann and GCB'
    trs_int_spot_tkt = rsab(bond=bond, trade_yield_or_price=trade_yield_or_price, number_of_units=number_of_units,
                            trader=trader, bank_broker=bank_broker, book=book, counterparty=counterparty)

    # Treasury facing ED & NRR Internal: Fwd
    book = 'A:IN:ALM TREASURY:INTERNAL RISK NRR CURVE:U'
    counterparty = 'Liberty Libfin Emdedded Derivs R'
    trs_int_fwd_tkt = rsab_fwd(bond=bond, forward_yield=forward_yield, number_of_units=-number_of_units, trader=trader,
                               repo_rate=repo_rate, far_maturity_date=far_maturity_date, book=book,
                               counterparty=counterparty)

    # ED & NRR facing Treasury Internal: Fwd
    book = 'A:IN:ALM MRM EDS AND NRR:INTERNAL:NRR CURVE:V'
    counterparty = 'Libfin Treasury'
    ed_int_fwd_tkt = rsab_fwd(bond=bond, forward_yield=forward_yield, number_of_units=number_of_units, trader=trader,
                              repo_rate=repo_rate, far_maturity_date=far_maturity_date, book=book,
                              counterparty=counterparty)

    mkt_ext_spot_tkt.to_excel(f'test_{bond}_ext_spot.xlsx', header=False)
    mkt_int_spot_tkt.to_excel(f'test_{bond}_int_spot_mkt.xlsx', header=False)
    trs_int_spot_tkt.to_excel(f'test_{bond}_int_spot_trs.xlsx', header=False)
    trs_int_fwd_tkt.to_excel(f'test_{bond}_int_fwd_trs.xlsx', header=False)
    ed_int_fwd_tkt.to_excel(f'test_{bond}_int_fwd_ed.xlsx', header=False)

