voiced = 0
voiceless = 0
too_high = 0
too_low = 0
values = 0
voiced_values = 0
voiceless_sound = 0
voiceless_egg = 0
test_data = 0
test_frames = 0
test_frames2 = 0
fill = 0

clearinfo

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
			test_data += 1 
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
	
			# timestep, pitchfloor, no. of candidates, very accurate, silence treshold, voicing threshold
			# ... octave cost, octave jump, voiced/unvoiced, pitch ceiling

			duration = Get total duration
			real_sound = Extract one channel: 1
			pitch_sound = noprogress To Pitch (ac): 0.0, 75.0, 15, "yes", 0.0, 0.45, 
			... 0.01, 0.35, 0.14, 600.0

			selectObject: sound
			egg = Extract one channel: 2
			pitch_egg = noprogress To Pitch (ac): 0.01, 75.0, 15, "yes", 0.0, 0.0, 
			... 0.01, 0.35, 0.0, 600.0

			number_of_frames = Get number of frames

			selectObject: channel3
			voice = Extract one channel: 3

			for frame to number_of_frames

				if test_data <= 84 || test_data > 756
					test_frames += 1

					selectObject: pitch_egg
					time = Get time from frame number: frame
					value_egg = Get value in frame: frame, "Hertz"

					selectObject: pitch_sound
					value_sound = Get value in frame: frame, "Hertz"

					selectObject: voice
					value_voice = Get value at time: 1, time, "Nearest"
							
					# voiced
					if value_voice <> 0 && value_egg <> undefined
						values += 1
						voiced_values += 1

						if value_sound == undefined
							voiceless += 1
							voiceless_sound += 1
						elsif abs((value_sound - value_egg) / value_egg) > 0.20
							fill += 1
							if value_sound > value_egg
								too_high += 1
							elsif value_sound < value_egg
								too_low += 1
							endif
						endif

					# voiceless
					else
						if value_sound <> undefined
							voiced += 1
						endif
					endif
				endif		
			endfor
			removeObject: sound, egg, channel3, real_sound, pitch_sound, pitch_egg, voice
		endfor
	endfor
endfor

clearinfo

gross_errors_freq = too_high + too_low
gross_errors_voicing = voiceless + voiced
gross_errors = gross_errors_freq + gross_errors_voicing

appendInfoLine: "The number of values is: ", values
appendInfoLine: "The number of voiced values is: ", voiced_values
appendInfoLine: "The number of test frames is: ", test_frames
appendInfoLine: "The number of gross errors is: ", gross_errors
appendInfoLine: "The number of gross errors freq is: ", gross_errors_freq
appendInfoLine: "The number of too high gross errors is: ", too_high
appendInfoLine: "The number of too low gross errors is: ", too_low
appendInfoLine: "The number of gross errors voicing is: ", gross_errors_voicing
appendInfoLine: "The number of wrong voiced gross-errors is: ", voiced
appendInfoLine: "The number of wrong voiceless gross-errors is: ", voiceless
appendInfoLine: "The percentage of gross errors freq is: ", fixed$(gross_errors_freq/test_frames*100,2), "%"
appendInfoLine: "The percentage of too high gross errors is: ", fixed$(too_high/gross_errors_freq*100,2), "%"
appendInfoLine: "The percentage of too low gross errors is: ", fixed$(too_low/gross_errors_freq*100,2), "%"
appendInfoLine: "The percentage of gross errors voicing is: ", fixed$(gross_errors_voicing/test_frames*100,2), "%"
appendInfoLine: "The percentage of wrong voiced gross-errors is: ", fixed$(voiced/gross_errors_voicing*100,2), "%"
appendInfoLine: "The percentage of wrong voiceless gross-errors is: ", fixed$(voiceless/gross_errors_voicing*100,2), "%"
appendInfoLine: "The percentage of (all) gross errors is: ", fixed$(gross_errors/test_frames*100,2), "%"
appendInfoLine: "The accuracy is: ", fixed$(100-(gross_errors/test_frames*100),2), "%"
