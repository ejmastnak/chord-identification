"""
About: a set of utility functions, unrelated to the DSP aspect of this
project, for converting between human-readable and machine friendly
representations of musical notes in the 12-tone equal temperament tuning
system.
"""

def get_notes_in_chord(chord_name):
    """
    Returns the names of notes in standard strummed guitar chords.
    
    Parameters
    ----------
    chord_name : str
        Examples: "A", "C", "D", "E", "G"

    Returns
    -------
    notes : tuple
        A tuple of strings representing the names of the notes in `chord_name` 
        Returns the notes in the A chord if `chord_name` 
        does not match "A", "C", "D", "E", "G".

    """
    return {"E": ("E2", "B2", "E3", "G#3", "B3", "E4"),
            "D": ("D3", "A3", "D4", "F#4"),
            "C": ("C3", "E3", "G3", "C4", "E4"),
            "A": ("A2", "E3", "A3", "C#4", "E4", "A4"),
            "G": ("G2", "D3", "G3", "B3", "D4", "G4")}.get(chord_name,
                    ("A2", "E3", "A3", "C#4", "E4", "A4"))


def get_note_number(note):
    """
    Auxiliary method used in note name to note ordinal conversion.
    Maps "C" to 0, "C#" to 1, ..., "B" to 11.
    """
    return {'C': 0, "C#": 1, "D": 2, "D#": 3, "E": 4, "F":  5,
            "F#": 6, "G": 7, "G#": 8, "A": 9, "A#": 10, "B": 11}.get(note, 0)


def get_note_ordinal(base_note, octave, A4_ordinal=49):
    """
    Returns the 12-TET ordinal of a note represented 
    by a base note (e.g. "A") and octave (e.g. 4).
    Uses A4 = 49 as a reference ordinal (as the 49th piano key)

    """
    return A4_ordinal - (9 - get_note_number(base_note)) - 12 * (4 - octave)


def decompose_note(note_name):
    """
    Decomposes a note name into the base note and octave number.
    Example input: "A4" or "F#5"
    Corresponding output: ("A", 4) or ("F#", 5).

    """
    if len(note_name) == 2:  # e.g. "A4"
        return note_name[0:1], int(note_name[1:2])
    elif len(note_name) == 3:  # e.g. "A#4"
        return note_name[0:2], int(note_name[2:3])
    else:  # should never happen, but return A4 as a fallback case
        return ("A", 4)


def get_frequency_of_note(note_name, A4=440, A4_ordinal=49):
    """
    Computes the frequency of a note in the 12-TET tuning system.

    Parameters
    ----------
    note_name : str
        Representation of a note as a base note and an octave number.
        Example: "A4", "F#5"

    Returns
    -------
    f : double
        Frequency associated with `note_name` in the 12-TET tuning system.

    """
    base_note, octave = decompose_note(note_name)
    ordinal = get_note_ordinal(base_note, octave, A4_ordinal=A4_ordinal)
    return A4*((2**(1/12))**(ordinal - A4_ordinal))
