#!/bin/env python 

#generate_midi.py
import subprocess
import sys

args = sys.argv

def generateforChord(argue):
    chord_progression = "C G Am F C G Am F"
    if argue[1] > argue[2]:
        chord_progression = "C G Am F C G Am F"
    elif argue[1] < argue[2]:
        chord_progression = "Am F G C"

    return chord_progression

container_id = 'testm'
gen_command = 'improv_rnn_generate'
gen_config = '--config=basic_improv'
model_path = '--bundle_file=/magenta-models/chord_pitches_improv.mag'
output_directory = '--output_dir=/magenta-data/chord_piteches_improv/generated '
#prime_note = 60

backing = 'backing_chords="'+generateforChord(args)+'"'
#command = ['docker','run' ,'--rm','--mount','type=bind','src=$(pwd)','dst=/magenta-data','-it','-p','6006:6006','tensorflow/magenta']
command=['improv_rnn_generate']
ex_command = [gen_command,gen_config,model_path,output_directory, backing,'--render_chords','--primer_melody=[67]']
command.extend(ex_command)
print(command)
res = subprocess.call(command)

print(res)

#print(shell_command)
#res = subprocess.call(shell_command)
#print("Message",res)
