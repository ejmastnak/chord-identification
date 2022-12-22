import numpy as np
from numpy.fft import fft, fftshift, fftfreq
import matplotlib.pyplot as plt
import soundfile as sf
import music_theory

# Directory holding chord `wav` files
data_dir = "../chords/"

# Whether to save figures to disk
save_figs = False
fig_dir = "../examples/"


# Colors for plotting waveform and spectrum
color_waveform = "#16697a"
color_spectrum = "#ff165d"

def remove_spines(ax):
    """
    Utility function to remove spines from a matplotlib axis for better
    aesthetics.

    """
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()


def get_chord_spectrum(wav_file):
    """
    Computes and returns the DFT of the audio signal in the file `file`

    """
    # Read samples and sample rate in [Hz]
    x, fs = sf.read(data_dir + wav_file)
    fc = 0.5 * fs  # Nyquist frequency
    N = x.shape[0]  # number of samples
    t1 = 0     # recording start time in [s]
    t2 = t1 + N/fs  # recording end time in [s]
    t = np.linspace(t1, t2, N)  # generate time samples

    X = fft(x[:,0])
    f = fftfreq(N, 1/fs)  # with Numpy's built-in method

    return (f, X, fs)


def plot_chord_spectrum(f, X, fs, chord_name, filename, f_max=1000):
    """
    Plots spectrum of a chord and add notes in chord.
    Only shows audible frequencies.

    Parameters
    ----------
    f : ndarray
        1D array of frequencies in [Hz] on which the chord's spectrum is defined
    X : ndarray
        1D array holding the chord's spectrum
    chord_name : str
        Single-letter name of the chord (assumed to be a major chord).
        Examples: "A", "C", "D", "E", "G"
    filename : str
        Name of the recording file used for this graph
    fs : double
        Frequency in [Hz] at which the chord was sampled
    f_max : double
        Maximum frequency [Hz] in chord's spectrum to plot
    
    """
    # Trim spectrum to contain only appreciably audible frequencies
    n_max = int(len(f)*f_max/fs)
    X = X[:n_max]
    f = f[:n_max]

    fig, ax = plt.subplots(1, 1)

    # Plot spectrum
    remove_spines(ax)
    ax.set_title("Spectrum of {} with {} major's notes overlayed".format(filename, chord_name))
    ax.set_xlabel("Frequency $f$ [Hz]")
    ax.set_ylabel("Amplitude $|X|$")
    ax.plot(f, np.abs(X))

    add_notes_to_chord_axis(ax, chord_name, np.max(np.abs(X)))

    plt.tight_layout()

    if save_figs:
        plt.savefig(fig_dir + "{}-spectrum-with-{}-notes.pdf".format(filename.replace(".wav", ""), chord_name))
    plt.show()


def plot_waveform_and_spectrum(wav_file):
    """
    Plots waveform and spectrum of the audio signal in WAV file `wav_file`.

    """
    # Read samples and sample rate in [Hz]
    x, fs = sf.read(wav_file)
    fc = 0.5 * fs  # Nyquist frequency
    N = x.shape[0]  # number of samples
    t1 = 0     # recording start time in [s]
    t2 = t1 + N/fs  # recording end time in [s]
    t = np.linspace(t1, t2, N)  # generate time samples

    X = fft(x[:,0])
    f = fftfreq(N, 1/fs)  # with Numpy's built-in method

    fig, axes = plt.subplots(2, 1)

    # Plot waveform
    ax = axes[0]
    remove_spines(ax)
    ax.set_title("Waveform")
    ax.set_xlabel("Time $t$ [s]")
    ax.set_ylabel("Amplitude $|X|$")
    ax.plot(t, x)

    # Plot spectrum
    ax = axes[1]
    remove_spines(ax)
    ax.set_title("Spectrum")
    ax.set_xlabel("Frequency $f$ [Hz]")
    ax.set_ylabel("Amplitude $|X|$")
    ax.plot(f, np.abs(X))

    plt.tight_layout()

    if save_figs:
        plt.savefig("overview" + ".pdf")
    plt.show()


def add_notes_to_chord_axis(ax, chord_name, max_spectral_amplitude):
    """
    Adds theoretically-expected positions of notes in a chord to a plot of
    the chord's spectrum.

    """
    notes = music_theory.get_notes_in_chord(chord_name)
    note_frequencies = []
    for note in notes:
        note_frequencies.append(music_theory.get_frequency_of_note(note))

    line_height = 1.0*max_spectral_amplitude
    text_height = 1.01*max_spectral_amplitude
    line_color = '#888888'

    for i, f in enumerate(note_frequencies):
        # Plot vertical line at each note frequency
        ax.vlines(f, ymin=0, ymax=line_height, color=line_color, 
                linestyle='--', zorder=-1)
        # Add the note name at the top of the vertical line
        ax.annotate(notes[i], (f, text_height), ha="center", va="bottom")

if __name__ == "__main__":
    chord_name = "A"
    f_max = 550
    filename = "2.wav"
    plot_chord_spectrum(*get_chord_spectrum(data_dir + filename), chord_name, filename, f_max=f_max)
