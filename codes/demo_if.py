loop = 1
while loop == 1:
	score = input("Enter your score: ")
	if score == 'exit':
		loop = 0
		print('Okay, you want to exit.')
	else:
		score = float(score)
		if score > 100:
			print("Huh......")
		elif score < 0:
			print("F*CK YOU")
		else:
			print(f"Okay, your score is {score}.")
			if score >= 80:
				grade = 'A'
			elif score >= 70:
				grade = 'B'
			elif score >= 60:
				grade = 'C'
			elif score >= 50:
				grade = 'D'
			elif score >= 0:
				grade = 'F'
			print(f"Score = {score} => Grade = {grade}")
print("Good Bye (^_^)")