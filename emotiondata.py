# taking generic json emotion data, how to pull out numbers and get engagement value(s)

def emotiondigest(list): # outputs: engagement at each second, array/list
	negative = 0
	positive = 0
	neutral = 0
	engauge = []
	for i in list:
		try: 
			dict = i[0] # each element in list, if nonempty, is one dict
			emotiondict = dict['faceAttributes']['emotion']
			negative += emotiondict['anger'] + emotiondict['fear'] + emotiondict['sadness'] + emotiondict['disgust']
			positive += emotiondict['happiness'] + emotiondict['surprise']
			neutral += emotiondict['contempt'] + emotiondict['neutral']
		except LookupError as e:
			engauge.append(0)
			continue 

		engagement = positive + .5*negative - neutral 
		engauge.append(engagement)
	return engauge 

# tester
list = [[], [], [], [{'faceId': '2322025a-eaae-481f-a624-a626e7b389c7', 'faceRectangle': {'top': 135, 'left': 228, 'width': 276, 'height': 276}, 'faceAttributes': {'emotion': {'anger': 0.0, 'contempt': 0.0, 'disgust': 0.0, 'fear': 0.0, 'happiness': 0.0, 'neutral': 0.8, 'sadness': 0.199, 'surprise': 0.0}}}], [{'faceId': '0a907d73-53f9-4bef-a849-923c87de1374', 'faceRectangle': {'top': 139, 'left': 230, 'width': 270, 'height': 270}, 'faceAttributes': {'emotion': {'anger': 0.0, 'contempt': 0.0, 'disgust': 0.0, 'fear': 0.0, 'happiness': 0.0, 'neutral': 0.912, 'sadness': 0.088, 'surprise': 0.0}}}]]
print(emotiondigest(list))

