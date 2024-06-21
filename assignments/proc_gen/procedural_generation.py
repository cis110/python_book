# Part 1: Audio
import random
from midiutil.MidiFile import MIDIFile


def generate_tilemap(width: int, height: int, tiles: list[tuple[float, str]]) -> list[list[str]]:
    """ Given a width and height, generate a tilemap with the given tiles.
        The output tilemap should be a list of lists of strings, where each string
        is a name representing a tile type.

        Arguments:
        width -- the width of the tilemap
        height -- the height of the tilemap
        tiles -- a list of (weight, type) tuples, where weight is a float representing
                 the probability of the tile type being chosen, and type is a string
                 representing the tile type
    """
    tilemap: list[list[str]] = []
    population: list[str] = [tile[1] for tile in tiles]
    weights: list[float] = [tile[0] for tile in tiles]
    # tilemap = [random.choices(population, weights=weights, k=width) for i in range(height)]
    for i in range(height):
        row: list[str] = []
        for j in range(width):
            row.append(random.choices([tile[1] for tile in tiles],
                                      [tile[0] for tile in tiles])[0])
        tilemap.append(row)
    return tilemap


def generate_melody(total_length: int, key: int, is_major: bool) -> list[tuple[int, int]]:
    """ Given a total_length in beats, generate a melody in a fixed key. 
        The output melody should be a list of (pitch, duration) tuples.
        The pitch is an integer representing the MIDI note number calculated
        from the key and the tonality. -1 is used to represent a "rest" (no note played.)
        The duration is an integer representing the number of beats over which that pitch
        should be played. No duration should be longer than 4 beats.

        Arguments:
        total_length -- the number of beats that the melody should span
        key -- the key of the melody as a root note
        is_major -- whether the melody should be in a major key
    """

    elapsed_duration: int = 0
    melody: list[tuple[int, int]] = []
    MAJOR_SCALE = [0, 2, 4, 5, 7, 9, 11]
    MINOR_SCALE = [0, 2, 3, 5, 7, 8, 10]

    while elapsed_duration < total_length:
        pitch: int = -1
        if (random.random() > 0.3):
            if is_major:
                pitch = key + random.choice(MAJOR_SCALE)
            else:
                pitch = key + random.choice(MINOR_SCALE)
        duration: int = random.randint(
            1, min(4, total_length - elapsed_duration))
        melody.append((pitch, duration))
        elapsed_duration += duration
    return melody

    # Create the MIDIFile Object with 1 track


def generate_song_file():
    MyMIDI = MIDIFile(1)
    # Tracks are numbered from zero. Times are measured in beats.
    track = 0
    time = 0

    # Add track name and tempo.
    MyMIDI.addTrackName(track, time, "melody")
    MyMIDI.addTempo(track, time, 140)

    # Add a note. addNote expects the following information:
    melody = generate_melody(32, 72, False)
    print(melody)
    track = 0
    channel = 0
    time = 0
    volume = 100
    for pitch, duration in melody:
        if (pitch != -1):
            MyMIDI.addNote(track, channel, pitch, time, duration, volume)
        time += duration

    for i in range(4):
        for (idx, pitch) in enumerate([48, 52, 55, 60]):
            MyMIDI.addNote(track, 0, pitch, 8 * i, 8, volume)
    # And write it to disk.
    binfile = open("output.mid", 'wb')
    MyMIDI.writeFile(binfile)
    binfile.close()


if __name__ == "__main__":
    # generate_song_file()
    print(generate_tilemap(
        5, 5, [(0.2, "grass"), (0.3, "water"), (0.5, "mountain")]))
