import pandas
import sys

import thinkstats2
import downey.nsfg as nsfg


def main(argv, dir):
    dct_file='{}/2002FemPreg.dct'.format(dir)
    dat_file='{}/2002FemPreg.dat.gz'.format(dir)
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    nsfg.CleanFemPreg(df)
    return df


if __name__ == "__main__":
    main(*sys.argv)

