# Time step: 0.0
# Pitch floor: 75 Hz
# Max. number of candidates: 15
# Very accurate: "yes"
# Silence threshold: 0.03
# Voicing threshold: 0.45
# Octave cost: 0.01
# Octave-jump cost: 0.35
# Voiced/unvoiced cost: 0.14
# Pitch ceiling: 600 Hz.

train_labels = Create Table with column names: "train_labels", 0, "place frequency"
min_dif = 0
dif = 0
min_row = 0
i = 0
filter = 40
smoothing = 20

for igender from 1 to 2
	if igender = 1
		directory16$ = "WAV16F/"
		directory$ = "WAVF/"
	else
		directory16$ = "WAV16M/"
		directory$ = "WAVM/"
	endif

	for ipart from 1 to 14
		if igender = 1
			gender$ = "F"
		else
			gender$ = "M"
		endif

		if ipart < 10
			n_part$ = "0"+string$(ipart)
		elsif ipart >= 10
			n_part$ = string$(ipart)
		endif

		participant$ = gender$ + n_part$
		writeInfoLine: participant$
		
		number = 48
		for isound from 1 to 30
			if isound mod 2 == 0
				bin = 2
			else
				bin = 1
				number += 1
			endif
			n_sound$ = "/" + participant$ + "-JA01F0" + string$(number) + "-" + string$(bin)
			channel3 = Read from file: directory16$ + participant$ + n_sound$ + ".wav"
			sound = Read from file: directory$ + participant$ + n_sound$ + ".wav"
			
			time_step = 0.01

			duration = Get total duration
			real_sound = Extract one channel: 1

			pitch_sound = noprogress To Pitch (ac): 0.0, 75.0, 15, "yes", 0.03, 0.45, 
			... 0.01, 0.35, 0.14, 600.0

			selectObject: sound
			egg = Extract one channel: 2
			filtered_sound = Filter (stop Hann band): 0, filter, smoothing
			pitch_egg = noprogress To Pitch (ac): 0.0, 75.0, 15, "yes", 0.03, 0.0, 
			... 0.01, 0.35, 0.0, 600.0

			frames = Get number of frames

			selectObject: channel3
			voice = Extract one channel: 3

			for frame from 1 to frames
				i += 1
				selectObject: pitch_egg
				time = Get time from frame number: frame
				value_egg = Get value in frame: frame, "Hertz"
	
				selectObject: pitch_sound
				value_sound = Get value in frame: frame, "Hertz"

				candidates_frame[frame] = Tabulate candidates in frame: frame
				Sort rows: "frequency"

				selectObject: voice
				value_voice = Get value at time: 1, time, "Nearest"

				min_dif = value_egg
				dif = value_egg
				selectObject: candidates_frame[frame]
		
				rows = Get number of rows

				for row from 1 to rows
					value[row] = Get value: row, "frequency"
					dif = abs(value_egg - value[row])

					if dif < min_dif
						min_dif = dif
						min_row = row
					endif
				endfor

				if i <> 1 && frame == 1
					selectObject: train_labels
					Append row
					eos = Get number of rows
					Set string value: eos, "place", "eos"
					Set string value: eos, "frequency", "eos"
					i += 1
				endif
	
				selectObject: train_labels
				Append row
				if value_egg <> undefined && value_voice <> 0
					Set numeric value: i, "place", min_row
					Set numeric value: i, "frequency", value_egg
				else
					Set numeric value: i, "place", 1
					Set numeric value: i, "frequency", 0
				endif 

				selectObject: candidates_frame[frame]
				Append row
				eof = Get number of rows
				Set string value: eof, "frequency", "eof"
				Set string value: eof, "strength", "eof"		
			endfor

			for frame from 1 to frames
				plusObject: candidates_frame[frame]
			endfor
			candidates_sound[isound] = Append

			Append row
			eos = Get number of rows
			Set string value: eos, "frequency", "eos"
			Set string value: eos, "strength", "eos"

			selectObject: candidates_frame[1]
			for frame from 1 to frames
				plusObject: candidates_frame[frame]
			endfor
			Remove

			removeObject: sound, filtered_sound, egg, channel3, real_sound, pitch_sound, pitch_egg, voice

			selectObject: candidates_sound[isound]
		endfor
	
		for isound from 1 to 30
			 plusObject: candidates_sound[isound]
		endfor

		candidates_part[ipart] = Append
	
		selectObject: candidates_sound[1]
		for isound from 1 to 30
			plusObject: candidates_sound[isound]
		endfor
		Remove

		selectObject: candidates_part[ipart]

	endfor

	for ipart from 1 to 14
		plusObject: candidates_part[ipart]
	endfor
	candidates_gender[igender] = Append

	selectObject: candidates_part[1]
	for ipart from 1 to 14
		plusObject: candidates_part[ipart]
	endfor
	Remove
	
	selectObject: candidates_gender[igender]
endfor

for igender from 1 to 2
	plusObject: candidates_gender[igender]
endfor
train_data = Append

selectObject: candidates_gender[1]
for igender from 1 to 2
	plusObject: candidates_gender[igender]
endfor
Remove

selectObject: train_data

Save as tab-separated file: "TrainData/train_data_all"

selectObject: train_labels

Append row
eos = Get number of rows
Set string value: eos, "place", "eos"
Set string value: eos, "frequency", "eos"

rows_labels = Get number of rows
Save as tab-separated file: "TrainData/train_labels_all"
writeInfoLine: "Number of frames: ", i, " Number of rows labels: ", rows_labels
appendInfoLine: "Number of frames: ", i-840, " Number of rows labels: ", rows_labels-840