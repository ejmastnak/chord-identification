# Chord identification

This project is a simple exercise in Fourier analysis with scientific Python packages, and uses Fourier techniques to identify the notes in guitar chords.

To run the code, clone the repository and run the Python script `src/chord-identification.py`.
An example shell session might read:

```bash
# Clone the repository
git clone https://github.com/ejmastnak/chord-identification.git

# Change into the source code directory
cd chord-identification/src

# Run the main script
python3 chord-identification.py
```

![2-spectrum-with-A-notes](https://user-images.githubusercontent.com/50270681/209318548-dc8da836-a29b-4c06-b1af-645b7207a09b.png)

## Goal

The `chords` directory contains 5 short recordings of 5 different strummed guitar chords: A, C, D, E, and G major.
The recordings are recorded in stereo WAV format and sampled at 44100 Hz.
The recordings are numbered 1, 2, 3, 4, and 5 and have been shuffled so that, unless you have some formal musical training, you probably cannot tell which file contains which chord from listening to the file alone.

Your goal is to use Fourier analysis, knowledge of the 12-tone equal temperament tuning system, and basic knowledge of the guitar fretboard to correctly match the file numbers 1, 2, 3, 4 and 5 to the guitar chords A, C, D, E, and G major. 

## Project structure

- `chords/` contains WAV recordings of the chords analyzed
- `src/` contains the source code
- `examples/` contains representative plots of recording `2.wav`'s spectrum with the theoretically-expected frequency-domain positions of the notes in the A and G major guitar chords overlayed---we can see that G major is the correct match for `2.wav`.
- `solution.txt` contains correct mappings between file names and chords.

## Dependencies

A reasonably up-to-date version of Python 3 with the following packages installed:

- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [SoundFile](https://pysoundfile.readthedocs.io/en/latest/)

A media player that can play WAV files is encouraged (to listen to the recordings for orientation) but not required for the code to run.
