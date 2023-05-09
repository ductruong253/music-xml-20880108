from music21 import converter, stream, tempo, key, dynamics, chord

class MusicXMLProcessor:
    def __init__(self, filename):
        self.music = converter.parse(filename)

    def change_tempo(self, new_tempo):
        for elem in self.music.recurse().getElementsByClass(tempo.MetronomeMark):
            elem.number = new_tempo

    def transpose(self, interval):
        for elem in self.music.recurse().getElementsByClass(key.Key):
            elem.transpose(interval, inPlace=True)

    def change_dynamic(self, new_dynamic):
        for elem in self.music.recurse().getElementsByClass(dynamics.Dynamic):
            elem.value = new_dynamic

    def add_basic_chords_and_rhythms(self):
        for m in self.music.getElementsByClass(stream.Measure):
            notes = m.notes.stream()
            if len(notes) > 0:
                c = chord.Chord(notes)
                c.duration = notes[0].duration
                m.append(c)

    def save(self, filename):
        self.music.write('musicxml', fp=filename)

if __name__ == '__main__':
    # Example usage:
    processor = MusicXMLProcessor('jingle_bells.xml')
    processor.change_tempo(120)
    processor.transpose('P5')  # Transpose up a perfect fifth
    processor.change_dynamic('mf')
    processor.add_basic_chords_and_rhythms()
    processor.save('jingle_bells_output.xml')