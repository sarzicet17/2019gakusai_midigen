#!/bin/env python 

#generate_midi.py
import subprocess
import sys

args = sys.argv


if len(args) < 4:
    print("arguments not enough")
    quit()

filename = args[4]

def generateforChord(argue):
    chord_progression = "C G Am F C G Am F"
    if argue[1] > argue[2] > argue[3]:
        chord_progression = "C G Am F C G Am F"
    elif argue[1] < argue[2] < argue[3]:
        chord_progression = "C G F Fm C"

    return chord_progression

gen_command = 'improv_rnn_generate'
gen_config = '--config=basic_improv'
model_path = '--bundle_file=/magenta-models/chord_pitches_improv.mag'
output_directory = '--output_dir=/magenta-data/'
output_files_num = '--num_outputs=1'
#prime_note = 60

backing = 'backing_chords="'+generateforChord(args)+'"'
command=['improv_rnn_generate']
ex_command = [gen_command,gen_config,model_path,output_directory, backing,output_files_num,'--render_chords','--primer_melody=[67]']
command.extend(ex_command)
print(command)
res = subprocess.call(command)
print(res)
# change filename
#mv_com = ['mv','/magenta-data/2019*.mid','music.mid']
#mv_com_args = ['/magenta-data/2019*.mid','music.mid']
#res2 = subprocess.call(mv_com,shell=True)
#mv_com.extend(mv_com_args)
subprocess.Popen('mv /magenta-data/2019*.mid /magenta-data/'+filename,shell=True).communicate()
#print(shell_command)
#res = subprocess.call(shell_command)
#print("Message",res)
