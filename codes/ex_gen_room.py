def genClassRoom(myroom, mydate, mytime):
	x = []
	for i in myroom:
		for j in mydate:
			for k in mytime:
				c = i + '_' + j + '_' + k
				x.append(c)
	return x

def showMyList(mylist, myText):
	pos = 0
	for i in mylist:
		pos = pos + 1
		print(f'{myText:9s} {pos:03.0f}:\t{i}')


def genVar(mysubject, myclassroom, varPrefix):
	x = []
	for i in mysubject:
		for j in myclassroom:
			v = varPrefix + '_' + i + '_' + j
			x.append(v)
	return x


def genSubject(mysid, mysec):
	x = []
	len_sid = len(mysid)
	len_sec = len(mysec)
	if len_sid == len_sec:
		for i in range(0, len_sid):
			y = mysid[i] + '_SEC_' + mysec[i]
			x.append(y)
	return x


# Main program
r = ['1905', '1906', '1907']
d = ['MON', 'TUE', 'WED', 'THU', 'FRI']
t = ['AM', 'PM', 'EV']
sid = ['911001', '911001', 
	'911002', '911002', 
	'911003', 
	'911004']
sec = ['1', '2',
	'1', '2',
	'1',
	'1']

showMyList(r, 'ROOM')
showMyList(sec, 'SEC')
subject = genSubject(sid, sec)
showMyList(subject, 'SUBJECT')
# print(f'Classroom = {genClassRoom(r, d, t)}')
# showClassRoom(genClassRoom(r, d, t))
classroom = genClassRoom(r, d, t)
showMyList(classroom, 'CLASSROOM')
var = genVar(subject, classroom, 'X')
showMyList(var, 'VAR')










