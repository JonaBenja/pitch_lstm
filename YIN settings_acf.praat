#GEDOWNSAMPLED

writeInfoLine: "WAV16:"

gross_errors_freq = 0
gross_errors_voice = 0
values = 0
voiceless = 0
num_values = 0
total_values = 0
voiced_values = 0

for igender from 1 to 2
	if igender = 1
		directory$ = "WAV16F/"
	else
		directory$ = "WAV16M/"
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
			sound = Read from file: directory$ + participant$ + n_sound$ + ".wav"

			time_step = 0.01
	
			duration = Get total duration
			real_sound = Extract one channel: 1
			pitch_praat = noprogress To Pitch (ac): 0.0, 40.0, 15, "no", 0.0, 0.0, 
			... 0.01, 0.35, 0.0, 800.0

			selectObject: sound
			truth = Extract one channel: 2
			pitch_truth = noprogress To Pitch (ac): 0.0, 40.0, 15, "no", 0.0, 0.0, 
			... 0.01, 0.35, 0.0, 800.0

			number_of_frames = Get number of frames

			selectObject: sound
			voice = Extract one channel: 3

			for frame to number_of_frames
				total_values += 1
				selectObject: pitch_truth
				time = Get time from frame number: frame

				selectObject: voice
				voiced_value = Get value at time: 1, time, "Nearest"

				selectObject: pitch_praat
				value_praat = Get value in frame: frame, "Hertz"

				selectObject: pitch_truth
				value_truth = Get value in frame: frame, "Hertz"

				if voiced_value <> 0
					voiced_values += 1
		
					if value_praat == undefined
						voiceless += 1
						gross_errors_voice += 1

					elif abs((value_praat - value_truth) / value_truth) > 0.20
						gross_errors_freq += 1	
					endif
				endif		

			endfor
		removeObject: sound, truth, real_sound, pitch_praat, pitch_truth, voice
		endfor
	endfor
endfor

gross_errors = gross_errors_voice + gross_errors_freq

appendInfoLine: "The number of total values is: ", total_values
appendInfoLine: "The number of gross errors is: ", gross_errors
appendInfoLine: "The number of voiced values is: ", voiced_values
appendInfoLine: "The number of voiceless values is: ", voiceless
appendInfoLine: "The percentage of gross errors_freq is: ", fixed$(gross_errors_freq/voiced_values*100,2), "%"
appendInfoLine: "The percentage of gross errors_voice is: ", fixed$(gross_errors_voice/voiced_values*100,2), "%"
appendInfoLine: "The percentage of gross errors is: ", fixed$(gross_errors/voiced_values*100,2), "%"
