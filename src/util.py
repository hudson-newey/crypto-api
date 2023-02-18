from datetime import datetime

def getDate() -> str:
  return str(datetime.now())

def getTimeMinute() -> str:
  dateObj = datetime.now()
  return str(dateObj.minute)

def getTimeHour() -> str:
  dateObj = datetime.now()
  return str(dateObj.hour)
