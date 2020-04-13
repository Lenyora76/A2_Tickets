from rsab_fwd import rsab_fwd
import pandas as pd
from datetime import datetime


def rsabfwd_internal(bond=None, forward_yield=None, number_of_units=None, transaction_date=None, trader=None,
                     repo_rate=None, far_maturity_date=None, mirror_desk=None, create_ticket=True):

    yyyy = far_maturity_date.strftime("%Y")
    mm = far_maturity_date.strftime("%m")
    dd = far_maturity_date.strftime("%d")

    trade_ref = f'{yyyy}{mm}{dd}_{bond}_BNDFWD'

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

    if create_ticket:
        price_maker.to_excel(f'{trade_ref}_{mirror_desk}.xlsx', header=False)
        price_taker.to_excel(f'{trade_ref}_Treasury.xlsx', header=False)

    else:
        return price_maker, price_taker


# Not tested as I am unable to open Alchemy

test_trade = {'bond': 'R2048', 'forward_yield':  0.1002, 'number_of_units': 100,
              'transaction_date': datetime(2020, 4, 9, 12, 0, 0), 'trader': 'Nico Nchabeleng', 'repo_rate': 0.0560,
              'far_maturity_date': datetime(2020, 6, 17, 18, 0, 0), 'mirror_desk': 'GIT', 'create_ticket': True
              }
rsabfwd_internal(**test_trade)
