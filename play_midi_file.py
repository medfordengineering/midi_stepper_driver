import mido
from mido import MidiFile

#load a midi file
#mid = MidiFile('mary4.mid')
#mid = MidiFile('star1.mid')
mid = MidiFile('Axel_F2.mid')

#print available ports
print(mido.get_output_names())

#print the contents of the midi file.
#for i, track in enumerate(mid.tracks):
#	print('Track {}: {}'.format(i, track.name))
#	for msg in track:
#		print(msg)

#open a port either external with ttymidi or internal with timidity
outport = mido.open_output('ttymidi:MIDI in 131:1')
#outport = mido.open_output('TiMidity port 0')

#play the file on the assigned port
#for msg in MidiFile('mary.mid').play():
for msg in mid.play():
	outport.send(msg)

#close the port
outport.close()

