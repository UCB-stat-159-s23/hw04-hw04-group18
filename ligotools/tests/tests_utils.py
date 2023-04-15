from ligotools import utils
import pytest
import numpy as np
from scipy.interpolate import interp1d
from scipy.signal import butter

strain_H1, time_H1, chan_dict_H1 = rl.loaddata('data/H-H1_LOSC_4_V2-1126259446-32.hdf5', 'H1')

fs = 4096
NFFT = 4 * fs
Pxx_H1, freqs = mlab.psd(strain_H1, Fs = fs, NFFT = NFFT)
psd_H1 = interp1d(freqs, Pxx_H1)
dt = time_h1[1] - time_h1[0]

strain_H1_whiten = whiten(strain_H1, psd_H1, dt)
fband = [43.0, 300.0]
bb, ab = butter(4, [fband[0] * 2./fs, fband[1] * 2./fs], btype = 'band')
normalization = np.sqrt((fband[1]-fband[0])/(fs/2))
strain_H1_whitenbp = filtfilt(bb, ab, strain_H1_whiten) / normalization
filename = 'GW150914'+"_H1_whitenbp.wav"
det = 'H1'
plottype = 'png'
pcolor = 'r'

def test_whiten():
    assert dt != 0
    assert type(strain_H1) is np.ndarray
    assert psd_H1(np.fft.rfftfreq(len(strain_H1), dt)) != 0
    assert 1./np.sqrt(1./(dt*2)) != 0
    assert type(utils.whiten(strain_H1, psd_H1, dt)) is np.ndarray
    
def test_write_wavfile():
    assert type(filename) is str
    assert type(strain_H1_whitenbp) is np.ndarray
    assert type(int(fs)) is int
    
def test_reqshift():
    assert type(utils.reqshift(strain_H1_whitenbp) is np.ndarray
    
def test_plot():
    assert plottype == 'png' or plottype == 'pdf'
    assert det == 'H1' or det == 'L1'
    assert len(pcolor) == 1 and type(pcolor) is str
