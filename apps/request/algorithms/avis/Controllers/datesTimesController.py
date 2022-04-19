from sys import path
from platform import system

"""
os = system()

if os == "Linux":
    path.append('/home/jordi/AvisAPI/Models/datesAlgorithm')
    path.append('/home/jordi/AvisAPI/Models/timesAlgorithm')
elif os == "Windows":
    path.append('d:\\Developer\\BotDeveloper\\Avis\\Models\\datesAlgorithm')
    path.append('d:\\Developer\\BotDeveloper\\Avis\\Models\\timesAlgorithm')
"""

from apps.request.algorithms.avis.Models.datesAlgorithm.datesAnalizer import searchDates, searchOnlyDate, cleanCacheDates,validateCorrectDate
from apps.request.algorithms.avis.Models.datesAlgorithm.datesObjects import *
from apps.request.algorithms.avis.Models.timesAlgorithm.timeAnalizer import searchTimes, cleanCacheTimes
from apps.request.algorithms.avis.Models.timesAlgorithm.utilTime import *



def searchDatesTimes(phrase):
    datesFound = searchDates(phrase)
    timesFound = searchTimes(phrase)
    #print(datesFound)
    if not datesFound["diaEntrega"] and datesFound["diaRenta"]:
        pass


    if datesFound["diaRenta"]:
        if not validateCorrectDate(datesFound["diaRenta"]):
            datesFound["diaRenta"] = None
            datesFound["fechaValida"] = False

    if datesFound["diaEntrega"]:
        if not validateCorrectDate(datesFound["diaEntrega"]):
            datesFound["diaEntrega"] = None
            datesFound["fechaValida"] = False
    
    if not datesFound["fechaValida"]:
        datesFound["diaRenta"] = None
        datesFound["diaEntrega"] = None

    else:
        datesFound.update(timesFound) 
        if datesFound["diaRenta"] and datesFound["diaEntrega"]:   
            
            if timesFound["horaRenta"] and timesFound["horaEntrega"]: 
                datesFound["fechaRenta"] = datesFound["diaRenta"] + "T" + datesFound["horaRenta"]
                datesFound["fechaEntrega"] = datesFound["diaEntrega"] + "T" + datesFound["horaEntrega"]
            
            elif timesFound["horaRenta"] and not timesFound["horaEntrega"]:
                datesFound["fechaRenta"] = datesFound["diaRenta"] + "T" + datesFound["horaRenta"]
                datesFound["fechaEntrega"] = datesFound["diaEntrega"] + "T" +  "00:00:00"
                datesFound["horaEntrega"] = None
            
            else:
                datesFound["fechaRenta"] = datesFound["diaRenta"] + "T" + "00:00:00"
                datesFound["fechaEntrega"] = datesFound["diaEntrega"] + "T" + "00:00:00"
                datesFound["horaEntrega"] = None
                datesFound["horaRenta"] = None
        
        elif datesFound["diaRenta"] and not datesFound["diaEntrega"]:
            datesFound["fechaEntrega"] = None
            if timesFound["horaRenta"]:
                datesFound["fechaRenta"] = datesFound["diaRenta"] + "T" + datesFound["horaRenta"]
            else:
                datesFound["fechaRenta"] = datesFound["diaRenta"] + "T" + "00:00:00"
                datesFound["fechaEntrega"] = None
       

    cleanCacheDates()
    cleanCacheTimes()
    return datesFound


def searchDateTime(phrase):
    datesFound = searchDates(phrase)
    timesFound = searchTimes(phrase)

    dateTime = {}
    
    if datesFound["diaRenta"]:
        if not validateCorrectDate(datesFound["diaRenta"]):
            datesFound["diaRenta"] = None
            datesFound["fechaValida"] = False

    if not datesFound["fechaValida"]:
        dateTime["fecha"] = None
        dateTime["hora"] = None
        dateTime["fechaValida"] = False
    else:
        if datesFound["diaRenta"]:
            if timesFound["horaRenta"]:
                dateTime["fecha"] = datesFound["diaRenta"] + "T" + timesFound["horaRenta"]
                dateTime["hora"] = timesFound["horaRenta"]
                dateTime["fechaValida"] = True
            else:
                dateTime["fecha"] = datesFound["diaRenta"] + "T" + "00:00:00"
                dateTime["hora"] = None
                dateTime["fechaValida"] = True
        else:
            dateTime["fecha"] = None
            dateTime["hora"] = None
            dateTime["fechaValida"] = False
    
    cleanCacheDates()
    cleanCacheTimes()
    return dateTime

def searchDate(phrase):
    datesFound = searchOnlyDate(phrase)
    date = {}
    print(datesFound)
    if datesFound["diaRenta"]:
        if not validateCorrectDate(datesFound["diaRenta"]):
            datesFound["diaRenta"] = None
            datesFound["fechaValida"] = False

    if not datesFound["fechaValida"]:
        date["fecha"] = None
        date["fechaValida"] = False
    else:
        if datesFound["diaRenta"]:
            date["fecha"] = datesFound["diaRenta"]
            date["fechaValida"] = True
        else:
            date["fecha"] = None
            date["fechaValida"] = False
    
    cleanCacheDates()
    return date

def searchTime(phrase):
    timesFound = searchTimes(phrase)
    time = {}
    if timesFound["horaRenta"]:
        time["hora"] = timesFound["horaRenta"]
    else:
        time["hora"] = None
    
    cleanCacheTimes()
    return time

    
if __name__ == '__main__':
    #phraseTime = "a las 08:30 pM  y lo quiero entregar a las 9:45 de la noche"
    #phrase1 = "quiero rentar del 29-2-2021 al 7/12/21"  #Fecha invalida mes/dia
    #phrase1 = "quiero rentar del 1-02-2022 al 2022-02/18"
    #phrase1 = "quiero rentar del 01 al 30 de mayo"
    #phrase = "quiero rentar un auto para el jueves y entregarlo el siguiente viernes"
    #phrase = "quiero rentar un auto para el miercoles y entregarlo el siguiente miercoles"
    #phrase = "quiero rentar un auto para el miercoles y entregarlo el mismo dia"
    #phrase = "quiero rentar un auto para el miercoles y entregarlo el mismo miercoles"
    #phrase = "quiero rentar un auto para hoy"
    #phrase = "quiero rentar del 28-0-2021 al 7/12/21"  #Fecha invalida mes/dia
    #phrase1 = "quiero rentar del 7/12/21 a las 08:30 pM al 8/12/21 a las 10:45 am"
    #phrase1 = "quiero rentar del 01 de mayo de 2022 a las 08:30 pM al 30 de mayo de 2022 a las 10:45 am"
    #phrase2 = "quiero rentar del 1 al 30 de mayo del 2022"
    #searchDatesTimes(phrase1)
    #print(searchDatesTimes("quiero rentar del 7/12/21 a las 08:30 pM al 8/12/21 a las 10:45 am"))
    print(searchDateTime("el 15 de octubre"))
    #print(searchDatesTimes("quiero rentar el 20/10/2021"))
    #print(searchTime("a las 4:30"))
    #print(searchDatesTimes("quiero rentar del 30 de agosto a las 10:30 pm al 30 de sept"))
    pass