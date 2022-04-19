import re
from datetime import datetime, timedelta
from .datesObjects import  monthsAlias, monthsNumber, weekDays, weekDaysEnglish
resultDatesArr = []
resultadoFinal = {
    "diaRenta": None,
    "diaEntrega": None,
    "fechaValida": True
}
finished = False
def searchDates(phrase):

    
    if not finished :
      dateFormatGeneric1(phrase)

    
    if not finished and len(resultDatesArr) < 2:
      dateFormatGeneric2(phrase)
    
    
    if not finished and not resultDatesArr:
      dateFormatGeneric3(phrase)

    if not finished and not resultDatesArr:
      dateFormatGeneric4(phrase)

    if not finished and not resultDatesArr:
       dateToday(phrase)
    if not finished and not resultDatesArr:
       dateWeekDay(phrase)
    if not finished:
      dateFormat1(phrase)
      
    if not finished:
      dateFormat2(phrase)


    resultDatesSet = set(resultDatesArr)
    resultDatesList = list(resultDatesSet)
   
    if not resultadoFinal["diaRenta"] and not resultadoFinal["diaEntrega"]:
        ordernar_fechas(resultDatesList)

    
    return resultadoFinal
    

def searchOnlyDate(phrase):
    
    
    if not resultDatesArr:
      dateFormat1(phrase)
    
    
    if not resultDatesArr:
      dateFormat2(phrase)
    
    
    if not resultDatesArr:
      dateFormatGeneric2(phrase)
    
    
    if not finished and not resultDatesArr:
      dateFormatGeneric3(phrase)

    if not finished and not resultDatesArr:
      dateFormatGeneric4(phrase)

    
    if not resultDatesArr:
        dateToday(phrase)
    
    if not resultDatesArr and not finished:
        dateWeekDay(phrase)

    resultDatesSet = set(resultDatesArr)
    resultDatesList = list(resultDatesSet)
    
    if not resultadoFinal["diaRenta"] and not resultadoFinal["diaEntrega"]:
        ordernar_fechas(resultDatesList)

    
    return resultadoFinal

def searchInPhrase(dateToSearch, string):
    index = string.find(dateToSearch)
    return index


def dateWeekDay(phrase):
    phraseToProcess = phrase.lower()
    regex = "(l[u|ú]nes|m[a|á]rtes|mi[e|é]rcoles|ju[e|é]ves|vi[e|é]rnes|s[a|á]bado|domingo)"
    resultweekDays = re.findall(regex, phraseToProcess)
    global finished
    if len(resultweekDays) >= 2:
        day1 = weekDays[resultweekDays[0]]
        day2 = weekDays[resultweekDays[1]]
        if resultweekDays[0] == resultweekDays[1]:
            slicedPhrase = phraseToProcess[phraseToProcess.find(resultweekDays[0]):]
            regex = "(siguiente|pr[o|ó]ximo|que sigue|sig)"
            result = re.findall(regex, slicedPhrase)
            if(result):
                weekday = weekDaysEnglish[day1]
                auxDate = datetime.now() + timedelta(days=1)
                while(True):
                    if auxDate.strftime("%A") == weekday:
                        date1ToHold = auxDate.strftime("%Y-%m-%d")
                        resultDatesArr.append(date1ToHold)
                        resultadoFinal["diaRenta"] = date1ToHold
                        auxDate = auxDate + timedelta(days=4)
                        while(True):
                            if auxDate.strftime("%A") == weekday:
                                date2ToHold = auxDate.strftime("%Y-%m-%d")
                                resultDatesArr.append(date2ToHold)
                                resultadoFinal["diaEntrega"] = date2ToHold
                                
                                finished = True
                                break
                            else:
                                auxDate = auxDate + timedelta(days=1)
                        break
                    else:
                        auxDate = auxDate + timedelta(days=1)
            else:
                slicedPhrase = phraseToProcess[phraseToProcess.find(resultweekDays[0]):]
                regex = "(mismo)"
                result = re.findall(regex, slicedPhrase)
                if(result):
                    weekday = weekDaysEnglish[day1]
                    auxDate = datetime.now() + timedelta(days=1)
                    while(True):
                        if auxDate.strftime("%A") == weekday:
                            date1ToHold = auxDate.strftime("%Y-%m-%d")
                            resultDatesArr.append(date1ToHold)
                            resultadoFinal["diaRenta"] = date1ToHold
                            resultadoFinal["diaEntrega"] = date1ToHold
                            
                            finished = True
                            break
                        else:
                            auxDate = auxDate + timedelta(days=1)
        else:
            weekday = weekDaysEnglish[day1]
            auxDate = datetime.now() + timedelta(days=1)
            while(True):
              if auxDate.strftime("%A") == weekday:
                date1ToHold = auxDate.strftime("%Y-%m-%d")
                resultDatesArr.append(date1ToHold)
                resultadoFinal["diaRenta"] = date1ToHold
                auxDate = auxDate + timedelta(days=1)
                weekday2 = weekDaysEnglish[day2]
                while(True):
                    if auxDate.strftime("%A") == weekday2:
                      date2ToHold = auxDate.strftime("%Y-%m-%d")
                      resultDatesArr.append(date2ToHold)
                      resultadoFinal["diaEntrega"] = date2ToHold
                      
                      finished = True
                      break
                    else:
                      auxDate = auxDate + timedelta(days=1)
                
                finished = True
                break
              else:
                auxDate = auxDate + timedelta(days=1)
    
    elif len(resultweekDays) == 1: 
      day1 = weekDays[resultweekDays[0]]
      finished = True
      weekday = weekDaysEnglish[day1]
      auxDate = datetime.now() + timedelta(days=1)
      while(True):
        if auxDate.strftime("%A") == weekday:
          date1ToHold = auxDate.strftime("%Y-%m-%d")
          
          resultDatesArr.append(date1ToHold)
         
          if "mismo" in phrase:
              resultadoFinal["diaRenta"] = date1ToHold
              resultadoFinal["diaEntrega"] = date1ToHold        
              
          break
        else:
          auxDate = auxDate + timedelta(days=1)    


def dateToday(phrase):   
    phraseToProcess = phrase.lower()
    regex = "(hoy|ahora|today|ahorita|manana|pasado manana|pasadomanana|pasadomañana|mañana|pasado mañana)"
    result = re.findall(regex, phraseToProcess)
    print(result)
    for date in result:
        if date in["hoy", "ahora", "today", "ahorita"]:
            dateToHold = datetime.now().strftime("%Y-%m-%d")
        elif date == "pasadomañana" or date == "pasado mañana" or date == "pasadomanana" or date == "pasado manana":
            dayAfterTomorrow = datetime.now() + timedelta(days=2)
            dateToHold = dayAfterTomorrow.strftime("%Y-%m-%d")
        elif date == "mañana" or date=="manana":
            tomorrow = datetime.now() + timedelta(days=1)
            dateToHold = tomorrow.strftime("%Y-%m-%d")
        
        resultDatesArr.append(dateToHold)
        global finished
        finished = True
"""
Function to validate these formats:
dd/mm/yyyy || dd/mm/yy || d/m/yy etc 
"""
def dateFormat1(string):
    regex = "\D(\d{1,2})([/-]+)(\d{1,2})([/-]+)(\d{2,4})\D"
    result = re.findall(regex, string+" ")
    for date in result:     
        dateToSearch = "".join(date)
        idx = searchInPhrase(dateToSearch, string)
        dayToHold = date[0] if len(date[0]) == 2 else '0'+date[0]
        monthToHold = date[2] if len(date[2]) == 2 else '0'+date[2]
        yearToHold = date[4] if len(date[4]) == 4 else '20'+date[4]
        dateToHold = f"{yearToHold}-{monthToHold}-{dayToHold}"
        resultDatesArr.append(dateToHold)   
        
"""
Function to validate these formats:
yyyy/mm/dd || yyyy/mm/y || yyyy/m/d etc 
"""
def dateFormat2(string):
    regex = "\D(\d{4})([/-])(\d{1,2})([/-])(\d{1,2})"
    result = re.findall(regex, string)
    for date in result:     
        dateToSearch = "".join(date)
        idx = searchInPhrase(dateToSearch, string)
        dayToHold = date[4] if len(date[4]) == 2 else '0'+date[0]
        monthToHold = date[2] if len(date[2]) == 2 else '0'+date[2]
        yearToHold = date[0]
        dateToHold = f"{yearToHold}-{monthToHold}-{dayToHold}"
        resultDatesArr.append(dateToHold)   


"""
Function to validate these formats:
dd to dd of month of year 
"""
def dateFormatGeneric1(string):
  
  for key, value in monthsAlias.items():
      for variant in value:
        regex = r"(\d{1,2})*([ ]*)(hasta|al)([a-zA-Z ]*)(\d{1,2})*([a-zA-Z ]*)(" + variant + r")([a-zA-Z. ]*)(\d{0,4})"
        result = re.findall(regex, string)
       
        if result:
            
            if len(result) >= 2:
              global finished
              finished = True
            for date in result:
                idx = string.find(date[0]+date[1]+date[2]+date[3]+date[4]+date[5]+date[6]+date[7]+date[8])
                if idx > 2:
                    if string[idx-2:idx].isnumeric():
                        continue
                day1ToHold = date[0] if len(date[0]) == 2 else '0'+date[0]
                day2ToHold = date[4] if len(date[4]) == 2 else '0'+date[4]
                
                monthToHold = monthsNumber[key]
                if date[8]:
                    if len(date[8]) == 4:
                        yearToHold = date[8]
                    elif len(date[8]) == 2:
                         yearToHold = "20" + date[8]
                    else:
                        yearToHold = str(datetime.now().year)
                else:
                    actualMonth = datetime.now().month
                    actualDay = datetime.now().day
                    
                    if int(monthToHold) < actualMonth:
                        yearToHold = str(datetime.now().year + 1)
                    else:
                         yearToHold = str(datetime.now().year)

                date1ToHold = f"{yearToHold}-{monthToHold}-{day1ToHold}"
                date2ToHold = f"{yearToHold}-{monthToHold}-{day2ToHold}"
                print(date1ToHold, date2ToHold)
                if validateCorrectDate(date1ToHold) and validateCorrectDate(date2ToHold):
                 
                  if date1ToHold not in resultDatesArr:
                    resultDatesArr.append(date1ToHold) 
                  if date2ToHold not in resultDatesArr:
                    resultDatesArr.append(date2ToHold)
               

"""
Function to validate these formats:
dd of month of year 
"""
def dateFormatGeneric2(string):
  global resultDatesArr
  resultDatesArr = []
  for key, value in monthsAlias.items():
      for variant in value:
        regex = r"(\d{1,2})([a-zA-Z ]*)(" + variant + r")([a-zA-Z. ]*)(\d{4})"
        result = re.findall(regex, string)
        if result:
            
            if len(result) >= 2:
                global finished
                finished = True
            for date in result:
                
                dayToHold = date[0] if len(date[0]) == 2 else '0'+date[0]
                monthToHold = monthsNumber[key]
                yearToHold = date[4]
                dateToHold = f"{yearToHold}-{monthToHold}-{dayToHold}"
                
                if validateCorrectDate(dateToHold):
                    if dateToHold not in resultDatesArr:
                      resultDatesArr.append(dateToHold)
                          
                    if len(resultDatesArr) >= 2:
                        finished = True
                else:
                    resultadoFinal["fechaValida"] = False


"""
Function to validate these formats:
dd of month 
"""
def dateFormatGeneric3(string):
  for key, value in monthsAlias.items():
      for variant in value:
        regex = r"(\d{1,2})([d|e| ]*)(" + variant + r")"
        result = re.findall(regex, string)
        
        if result:
            
            for date in result:
                dayToHold = date[0] if len(date[0]) == 2 else '0'+date[0]
                monthToHold = monthsNumber[key]
                actualMonth = datetime.now().month
                actualDay = datetime.now().day    
                if int(monthToHold) < actualMonth:
                    yearToHold = str(datetime.now().year + 1)
                elif int(dayToHold) < actualDay and int(monthToHold) < actualMonth:
                    yearToHold = str(datetime.now().year + 1)
                else:
                    yearToHold = str(datetime.now().year)

                dateToHold = f"{yearToHold}-{monthToHold}-{dayToHold}"
                
                if validateCorrectDate(dateToHold):
                    if dateToHold not in resultDatesArr:
                      resultDatesArr.append(dateToHold)


"""
Function to validate these formats:
month dd 
"""
def dateFormatGeneric4(string):
    
    for key, value in monthsAlias.items():
        for variant in value:
            regex = r"(" + variant + r")([d|e| ]*)(\d{1,2})"
            result = re.findall(regex, string)
           
            if result:
                
                for date in result:
                    dayToHold = date[2] if len(date[2]) == 2 else '0' + date[2]
                    monthToHold = monthsNumber[key]
                    actualMonth = datetime.now().month
                    actualDay = datetime.now().day
                    if int(monthToHold) < actualMonth:
                        yearToHold = str(datetime.now().year + 1)
                    elif int(dayToHold) < actualDay and int(monthToHold) < actualMonth:
                        yearToHold = str(datetime.now().year + 1)
                    else:
                        yearToHold = str(datetime.now().year)

                    dateToHold = f"{yearToHold}-{monthToHold}-{dayToHold}"

                    if validateCorrectDate(dateToHold):
                        if dateToHold not in resultDatesArr:
                            resultDatesArr.append(dateToHold)
                            

       

def ordernar_fechas(arrFechas):
    if len(arrFechas) == 1:
        resultadoFinal["diaRenta"] = arrFechas[0]
    elif len(arrFechas) == 2:
        try:
          day1 = datetime.strptime(arrFechas[0], "%Y-%m-%d")
          day2 = datetime.strptime(arrFechas[1], "%Y-%m-%d")
        except:
            resultadoFinal["diaRenta"] = None
            resultadoFinal["diaEntrega"] = None
            resultadoFinal["fechaValida"] = False
            return 
        if day2 > day1:
            day1ToHold = day1.strftime("%Y-%m-%d")
            day2ToHold = day2.strftime("%Y-%m-%d")
            resultadoFinal["diaRenta"] = day1ToHold
            resultadoFinal["diaEntrega"] = day2ToHold
        elif day1 > day2:
            day1ToHold = day2.strftime("%Y-%m-%d")
            day2ToHold = day1.strftime("%Y-%m-%d")
            resultadoFinal["diaRenta"] = day1ToHold
            resultadoFinal["diaEntrega"] = day2ToHold
        else:
            day1ToHold = day1.strftime("%Y-%m-%d")
            day2ToHold = day1.strftime("%Y-%m-%d")
            resultadoFinal["diaRenta"] = day1ToHold
            resultadoFinal["diaEntrega"] = day2ToHold
    elif len(arrFechas) >= 3:
        resultadoFinal["diaRenta"] = None
        resultadoFinal["diaEntrega"] = None
        resultadoFinal["fechaValida"] = False
        return 

def validateCorrectDate(date):
    try:
        correctDate = datetime.strptime(date, "%Y-%m-%d")
        year = correctDate.year
        month = correctDate.month
        day = correctDate.day
        actualYear = datetime.now().year
        actualMonth = datetime.now().month
        actualDay = datetime.now().day
        if year < actualYear or year > actualYear+1 :
            return False
       
        if month < actualMonth and year <= actualYear:
            return False
        
        if day < actualDay and month < actualMonth and year <= actualYear:
            return False
        
        return True
    except:
        return False


def cleanCacheDates():
    global resultDatesArr 
    global finished
    finished = False
    resultDatesArr = []
    global resultadoFinal
    resultadoFinal = {
        "diaRenta": None,
        "diaEntrega": None,
        "fechaValida": True
    }

if __name__ == '__main__':
    #phrase = "quiero rentar del 20 de agosto de 2022 al 30 de sept de 2022" ####
    #phrase = "quiero rentar del 3-11-2021 al 7/12/21"
    #phrase = "quiero rentar del 29-2-2021 al 7/12/21"  #Fecha invalida mes/dia
    #phrase = "quiero rentar del 1-02-2022 al 2022-02/18"
    #phrase = "quiero rentar del 30 de agosto al 30 de sept" #####
    #phrase = "quiero rentar del 01 de mayo al 30 de junio" #####
    #phrase = "quiero rentar del 20 al 30 de sept de 2022"
    #phrase = "07 de agosto al 05 de septiembre"
    #phrase = "quiero rentar de agosto 04 a septiembre 05"
    #phrase = "quiero rentar un auto para el jueves y entregarlo el siguiente viernes"
    #phrase = "quiero rentar un auto para el miercoles y entregarlo el siguiente miercoles"
    #phrase = "quiero rentar un auto para el miercoles y entregarlo el mismo dia"
    #phrase = "quiero rentar un auto para el miercoles y entregarlo el mismo miercoles"
    phrase = "El martes 15 de septiembre a las 11 de la manana"
    #phrase = "quiero rentar del 01 de agosto a las 10:30 al 30 de sept a las 11:30"
    #phrase = "quiero rentar del 28-0-2021 al 7/12/21"  #Fecha invalida mes/dia
    print(searchOnlyDate(phrase))
    #print(validateCorrectDate("2022-06-20"))
    #print(searchOnlyDate(phrase))
    
    
    