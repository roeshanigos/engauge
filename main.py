import json
import urllib

import VideoAnalyzer as va
import DataAnalyzer as da

# STEP 1: Set video information as necessary.
data = va.getVideoData()

# STEP 2: Get the information and timestamps for the keywords
keywords = da.getKeywords(data)


print(keywords)


# Upload all of the keyword timestamps and information to the website

for i in keywords:
    print(i)
    print(keywords[i])
    keyword = '' + str(i) + ''
    values = '' + str(keywords[i]) + ''
    values = values[1:]
    values = values[:-1]

    url = "http://engauge.lex.ma/data.php?keyword=" + keyword.replace(' ', '%20') + "&data=" + values.replace(' ', '%20')
    print(url)
    contents = urllib.request.urlopen(url).read()



# Upload the engagement data

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


url = "http://engauge.lex.ma/clear.php"
print(url)
contents = urllib.request.urlopen(url).read()

engagement_data = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 6, 1, 4, 0, 2]

for i in range(0, len(engagement_data), 20):
    engagement_string = ",".join(map(str, engagement_data[i:i + 20]))

    url = "http://engauge.lex.ma/upload.php?engagement=" + engagement_string + ''
    print(url)
    contents = urllib.request.urlopen(url).read()
