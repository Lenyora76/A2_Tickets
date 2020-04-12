from rsa_bond import rsab
from rsab_fwd import rsab_fwd
from datetime import datetime

today = datetime(datetime.today().year, datetime.today().month, datetime.today().day, 12, 0, 0)  # clunky


def rsa_bond_ed(**kwargs):

    yyyy = far_maturity_date.strftime("%Y")
    mm = far_maturity_date.strftime("%m")
    dd = far_maturity_date.strftime("%d")

    mkt_ext_spot_tkt = rsab(**kwargs)
    mkt_int_spot_tkt = rsab(**kwargs)
    trs_int_spot_tkt = rsab(**kwargs)
    trs_int_fwd_tkt = rsab_fwd()
    ed_int_fwd_tkt = rsab_fwd()

    mkt_ext_spot_tkt.to_excel(f'{bond}_ext_spot.xlsx')
    mkt_int_spot_tkt.to_excel(f'{bond}_int_spot_mkt.xlsx')
    trs_int_spot_tkt.to_excel(f'{bond}_int_spot_trs.xlsx')
    trs_int_fwd_tkt.to_excel(f'{bond}_int_fwd_trs.xlsx')
    ed_int_fwd_tkt.to_excel(f'{bond}_int_fwd_ed.xlsx')

# Test


