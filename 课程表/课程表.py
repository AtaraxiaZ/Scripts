import requests
from bs4 import BeautifulSoup
from time import sleep


url = 'http://xk.urp.seu.edu.cn/jw_service/service/stuCurriculum.action?queryStudentId={}&queryAcademicYear=18-19-3'
perfix = '040175'

for i in range(1, 41):
    try:
        if i < 10:
            response = requests.get(url.format(perfix + '0' + str(i)))
        else:
            response = requests.get(url.format(perfix + str(i)))
        response.encoding = 'UTF-8'
        bp = BeautifulSoup(response.text, 'lxml')
        #print(bp)
        data = bp.find_all('td', {'width':'20%', 'align':'left'})
        print(data[4].text)
        #sleep(0.5)
    except:
        pass
    
