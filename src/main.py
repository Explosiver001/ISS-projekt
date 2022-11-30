import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
MIDIFROM = 24
MIDITO = 108
SKIP_SEC = 0.25
HOWMUCH_SEC = 0.5
WHOLETONE_SEC = 2
howmanytones = MIDITO - MIDIFROM + 1
tones = np.arange(MIDIFROM, MIDITO+1)
s, Fs = sf.read("../audio/klavir.wav")

plt.title('klavir_orig')
plt.plot(s)
plt.show()
N = int(Fs * HOWMUCH_SEC)
Nwholetone = int(Fs * WHOLETONE_SEC)

MIDI_A = 40
MIDI_A_F = 82.41
MIDI_B = 78
MIDI_B_F = 739.99
MIDI_C = 80
MIDI_C_F = 830.61

#MIDI A
start = Nwholetone*(MIDI_A-MIDIFROM)
plt.title('a_orig')
TONE_A = s[start:start+Nwholetone]
sf.write('../audio/a_orig.wav', TONE_A, Fs)
plt.plot(TONE_A[0:int(3*Fs/MIDI_A_F)])
plt.show()


TONE_A_DFT = np.fft.fft(TONE_A)
TONE_A_DFT = np.abs(TONE_A_DFT)
TONE_A_DFT = TONE_A_DFT[:TONE_A_DFT.size//2]
F = np.arange(TONE_A_DFT.size) * Fs / TONE_A.size
plt.title('a_DFT')
plt.plot(F[0:5000], TONE_A_DFT[0:5000])
plt.show()

#MIDI B
start = Nwholetone*(MIDI_B-MIDIFROM)
plt.title('b_orig')
TONE_B = s[start:start+Nwholetone]
sf.write('../audio/b_orig.wav', TONE_B, Fs)
plt.plot(TONE_B[0:int(3*Fs/MIDI_B_F)])
plt.show()


TONE_B_DFT = np.fft.fft(TONE_B)
TONE_B_DFT = np.abs(TONE_B_DFT)
TONE_B_DFT = TONE_B_DFT[:TONE_B_DFT.size//2]
F = np.arange(TONE_B_DFT.size) * Fs / TONE_B.size
plt.title('b_DFT')
plt.plot(F[0:5000], TONE_B_DFT[0:5000])
plt.show()

#MIDI C
start = Nwholetone*(MIDI_C-MIDIFROM)
plt.title('c_orig')
TONE_C = s[start:start+Nwholetone]
sf.write('../audio/c_orig.wav', TONE_C, Fs)
plt.plot(TONE_C[0:int(3*Fs/MIDI_C_F)])
plt.show()


TONE_C_DFT = np.fft.fft(TONE_C)
TONE_C_DFT = np.abs(TONE_C_DFT)
TONE_C_DFT = TONE_C_DFT[:TONE_C_DFT.size//2]
F = np.arange(TONE_C_DFT.size) * Fs / TONE_C.size
plt.title('c_DFT')
plt.plot(F[0:5000], TONE_C_DFT[0:5000])
plt.show()

