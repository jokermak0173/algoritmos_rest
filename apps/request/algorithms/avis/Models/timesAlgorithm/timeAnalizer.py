import re
from .utilTime import *
timesFound = {
    "horaRenta": None,
    "horaEntrega": None,
}
timesArr = []
fatalError = False
def searchTimes(phrase):
  phrase = phrase.replace(".", ":")
  timeFormat1(phrase)
  if len(timesArr) < 2:
    timeFormat2(phrase)
  
  if timesArr:
    if len(timesArr) >= 2:
        
        if timesArr[0][1] > timesArr[1][1]:
            timesFound["horaRenta"] = timesArr[1][0]
            timesFound["horaEntrega"] = timesArr[0][0]
        
        elif timesArr[0][1] < timesArr[1][1]:
            timesFound["horaRenta"] = timesArr[0][0]
            timesFound["horaEntrega"] = timesArr[1][0]
        
        else:
            timesFound["horaRenta"] = timesArr[0][0]
            timesFound["horaEntrega"] = timesArr[1][0]
    
    elif len(timesArr) == 1:
        timesFound["horaRenta"] = timesArr[0][0]
    
    if timesFound["horaRenta"]:
      if len(timesFound["horaRenta"]) != 8:
        timesFound["horaRenta"] = None
    
    if timesFound["horaEntrega"]:
      if len(timesFound["horaEntrega"]) != 8:
        timesFound["horaEntrega"] = None
  
  return timesFound

timeFound = {
    "timeFound": None
}
def searchTime(phrase):
  timeFormat1(phrase)
  if len(timesArr) == 0:
    timeFormat2(phrase)
  if timesArr:
    timeFound = {
        "timeFound": timesArr[0][0]
    }
  
  print(timeFound)


def timeFormat1(phrase):
  phraseToProcess = phrase.lower()
  regex = r"(\d{1,2})([a-z ]*)(:\d{1,2}|media|cuarto|punto)([a-z ]*)(a\.{0,1}m|p\.{0,1}m|mañana|manana|tarde|noche|horas|hr|hrs|hora|h|hs)"  
  result = re.findall(regex, phraseToProcess)
 
  for time in result:
    idxTime = phrase.find(time[0]+time[1]+time[2]+time[3]+time[4])
    time = list(time)
    tempTime = ""
    for idx in range(3):
        if idx == 0:
                
            if len(time[idx]) == 1:
                time[idx] = "0" + time[idx]
              
            if int(time[idx]) > 12 and int(time[idx]) <= 24:
              tempTime += time[idx] 
              
            
            elif int(time[idx]) <= 11 and int(time[idx]) >= 1:
              if time[4]:
                  if time[4][0].lower() == "p" or time[4] in ('tarde', 'noche'):
                    tempTime += timeDict[int(time[idx])]
                  else:
                    tempTime += time[idx]
              else:     
                tempTime += time[idx]
            
            elif int(time[idx]) == 12:
                if time[4]:
                  if time[4][0].lower() == "p" or time[4] in ('tarde'):
                    tempTime += "12"
                  elif time[4][0].lower() == "a" or time[4] in ('noche'):
                    tempTime += "00"
            else:
                fatalError = True
                break
            
            
        elif idx == 2:
            time[idx] =  time[idx].replace(":", '')
            tempTime += ":"
            try:
            
                if int(time[idx]) >= 0 and int(time[idx]) <= 7:
                    tempTime += "00"
                
                elif int(time[idx]) >= 8 and int(time[idx]) <= 22:
                    tempTime += "15"
                
                elif int(time[idx]) >= 23 and int(time[idx]) <= 37:
                    tempTime += "30"
                
                elif int(time[idx]) >= 38 and int(time[idx]) <= 59:
                    tempTime += "45"
            
            except: 
                if time[idx] == "media":
                    tempTime += "30"

                elif time[idx] == "cuarto":
                    tempTime += "15"
                
                else:
                    tempTime += "00"

            tempTime += ":00"
            timeElement = (tempTime, idxTime)
            timesArr.append(timeElement)
            if len(timesArr) >= 2:
                return



def timeFormat2(phrase):
  phraseToProcess = phrase.lower()
  regex = r"(\d{1,2})([a-z ]*)(:\d{1,2})*([a-z ]*)(a\.{0,1}m|p\.{0,1}m|mañana|manana|tarde|noche|h|hr|hs|hrs|hora|horas)"  
  result = re.findall(regex, phraseToProcess)
  print(result)
  for time in result:
    idxTime = phrase.find(time[0]+time[1]+time[2]+time[3]+time[4])
    time = list(time)
    tempTime = ""
    for idx in range(3):
        if idx == 0:
                
            if len(time[idx]) == 1:
                time[idx] = "0" + time[idx]
              
            if int(time[idx]) > 12 and int(time[idx]) <= 24:
              tempTime += time[idx] 
              
            
            elif int(time[idx]) <= 11 and int(time[idx]) >= 1:
              if time[4]:
                  if time[4][0].lower() == "p" or time[4] in ('tarde', 'noche'):
                    tempTime += timeDict[int(time[idx])]
                  else:
                    tempTime += time[idx]
              else:     
                tempTime += time[idx]
            
            elif int(time[idx]) == 12:
                if time[4]:
                  if time[4][0].lower() == "p" or time[4] in ('tarde'):
                    tempTime += "12"
                  elif time[4][0].lower() == "a" or time[4] in ('noche'):
                    tempTime += "00"
            else:
                fatalError = True
                break
            
            
        elif idx == 2:
            if time[idx]:
                time[idx] =  time[idx].replace(":", '')
                tempTime += ":"
                print("**********", time)
                if int(time[idx]) >= 0 and int(time[idx]) <= 7:
                    tempTime += "00"
                    
                elif int(time[idx]) >= 8 and int(time[idx]) <= 22:
                    tempTime += "15"
                    
                elif int(time[idx]) >= 23 and int(time[idx]) <= 37:
                    tempTime += "30"
                    
                elif int(time[idx]) >= 38 and int(time[idx]) <= 59:
                    tempTime += "45"
            else:
                tempTime += ":00"
  
    tempTime += ":00"
    timeElement = (tempTime, idxTime)
    timesArr.append(timeElement)
    if len(timesArr) >= 2:
      return

"""
def timeFormat3(phrase):
  phraseToProcess = phrase.lower()
  regex = r"(\d{1,2})(:\d{1,2})*"
  result = re.findall(regex, phraseToProcess)
  
  for time in result:
    idxTime = phrase.find(time[0]+time[1])
    time = list(time)
    tempTime = ""
    if time[0]:
      if len(time[0]) == 1:
          time[0] = "0" + time[0]
              
      if int(time[0]) >= 0 and int(time[0]) <= 24:
        tempTime += time[0] 
            
      else:
        continue
    else:
      continue
    
    if time[1]:
      time[1] =  time[1].replace(":", '')
      tempTime += ":"
  
      if int(time[1]) >= 0 and int(time[1]) <= 7:
        tempTime += "00"
                    
      elif int(time[1]) >= 8 and int(time[1]) <= 22:
        tempTime += "15"
                    
      elif int(time[1]) >= 23 and int(time[1]) <= 37:
        tempTime += "30"
                    
      elif int(time[1]) >= 38 and int(time[1]) <= 59:
        tempTime += "45"
    
    else:
      tempTime += ":00"
    
    tempTime += ":00"
    timeElement = (tempTime, idxTime)
    timesArr.append(timeElement)
    if len(timesArr) >= 2:
      return  
"""

def cleanCacheTimes():
  global timesFound
  global timesArr
  global fatalError
  timesFound = {
    "horaRenta": None,
    "horaEntrega": None,
  }
  timesArr = []
  fatalError = False

if __name__ == "__main__":
    #phrase
    #phrase = "a las 08:30 pM  y lo quiero entregar a las 9:45 de la noche"
    #phrase = "a las 08:45  de la tarde  y lo quiero entregar a las 9 y cuarto de la noche"
    phrase = "a las 8 de la noche y lo entrego a las 4 de la tarde" 
    #fechasEncontradas = searchDates(phrase)
    searchTimes(phrase)
    print(timesFound)
    #timeFormat2(phrase)
    #print(timesArr)
    #print(horasEncontradas)
