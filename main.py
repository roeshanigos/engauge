import json
import urllib

import VideoAnalyzer as va
import DataAnalyzer as da

# STEP 1: Set video information as necessary.
data = va.getVideoData()

# STEP 2: Get the information and timestamps for the keywords
keywords = da.getKeywords(data)


print(keywords)




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
