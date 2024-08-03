NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
SCALES = {
    'major': [2, 2, 1, 2, 2, 2, 1],
    'harmonic minor': [2, 1, 2, 2, 1, 3, 1],
    'natural minor': [2, 1, 2, 2, 1, 2, 2],
}


def get_scale(root: str, scale_type: str) -> list[str]:
    # Normalise the note and scale name:
    root = root.capitalize()
    scale_type = scale_type.lower()

    # Eliminate flats in favour of sharps:
    if 'b' in root:
        index = NOTES.index(root[0]) - 1
        root = NOTES[index]

    # Eliminate enharmonic equivalents:
    match root:
        case 'B#': root = 'C'
        case 'E#': root = 'F'

    # Set up index and initial list:
    current_index = NOTES.index(root)
    scale = [root]

    # Iterate through intervals according to scale type:
    for interval in SCALES[scale_type]:
        current_index = (current_index + interval) % 12
        scale.append(NOTES[current_index])

    return scale

