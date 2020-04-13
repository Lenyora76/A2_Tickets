from rsab_fwd import rsab_fwd
import pandas as pd


def rsab_fwd_int(bond=None, forward_yield=None, number_of_units=None, transaction_date=None, trader=None,
                 repo_rate=None, far_maturity_date=None, mirror_desk=None):

    d = {'Counterparty Desk': ['GIT', 'ED'],
         'Counterparty Name': ['Libfin GIT', 'Liberty Libfin Emdedded Derivs R'],
         'Counterparty Book': ['A:IN:ALM MRM GIT:INTERNAL RISK:R', 'A:IN:ALM MRM EDS AND NRR:INTERNAL:NRR CURVE:V']
         }

    df = pd.DataFrame.from_dict(d)
    df = df.set_index('Counterparty Desk')

    counterparty = df.loc[mirror_desk, 'Counterparty Name']
    price_maker = rsab_fwd(bond=bond, forward_yield=forward_yield, number_of_units=number_of_units,
                           transaction_date=transaction_date, trader=trader, repo_rate=repo_rate,
                           counterparty=counterparty, book='A:IN:ALM TREASURY:INTERNAL RISK:U',
                           far_maturity_date=far_maturity_date)

    book = df.loc[mirror_desk, 'Counterparty Book']
    price_taker = rsab_fwd(bond=bond, forward_yield=forward_yield, number_of_units=-number_of_units,
                           transaction_date=transaction_date, trader=trader, repo_rate=repo_rate,
                           counterparty='Libfin Treasury', book=book, far_maturity_date=far_maturity_date)

    return price_maker, price_taker

# Not tested
