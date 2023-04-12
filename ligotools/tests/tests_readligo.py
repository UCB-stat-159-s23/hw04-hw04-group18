from ligotools import readligo as rl
import pytest

#run the loaddata function for H1, L1 data
strain_h1, time_h1, chan_dict_h1 = rl.loaddata('data/H-H1_LOSC_4_V2-1126259446-32.hdf5', 'H1')
strain_l1, time_l1, chan_dict_l1 = rl.loaddata('data/H-L1_LOSC_4_V2-1126259446-32.hdf5', 'L1')


#test loaddata output correctness for H1
def test_loaddata_H1():
    assert strain_h1[1]== 2.08763900e-19
    assert time_h1[1] == 1126259446.0002441
    assert chan_dict_h1['CBC_CAT1'][1] == 1
    assert len(time_h1) == 131072
    assert len(chan_dict_h1) == 13

#test the datatype of the outputs of loaddata for H1
def test_H1_type():
    assert type(strain_h1) is np.array
    assert type(time_h1) is np.array
    assert type(chan_dict_h1) is dict

#test loaddata output correctness for L1
def test_loaddata_L1():
    assert strain_l1[1]== -1.03586274e-18
    assert time_l1[1] == 1.12625945e+09
    assert chan_dict_L1['NO_CW_HW_INJ'].sum() == 0
    assert len(time_l1) == 131072
    assert len(chan_dict_l1) == 13

#test the datatype of the outputs of loaddata for L1
def test_L1_type():
    assert type(strain_l1) is np.array
    assert type(time_l1) is np.array
    assert type(chan_dict_l1) is dict