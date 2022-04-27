# -*- coding: utf-8 -*-
from time import strftime
from datetime import datetime, timedelta
import datetime
import time

class thaidateandtime:
    __version__ = '0.9'
    __doc__ = 'class for display date and time in thai lang.'
    CurYearThai = ''
    CurYearThai2 = ''
    MonthNameShort = {'01':'ม.ค.',
                          '02':'ก.พ.',
                          '03':'มี.ค.',
                          '04':'เม.ย.',
                          '05':'พ.ค.',
                          '06':'มิ.ย.',
                          '07':'ก.ค.',
                          '08':'ส.ค.',
                          '09':'ก.ย.',
                          '10':'ต.ค.',
                          '11':'พ.ย.',
                          '12':'ธ.ค.'}
    MonthName = {'01':'มกราคม',
                          '02':'กุมภาพันธู์',
                          '03':'มีนาคม',
                          '04':'เมษายน',
                          '05':'พฤษภาคม',
                          '06':'มิถุนายน',
                          '07':'กรกฏาคม',
                          '08':'สิงหาคม',
                          '09':'กันยายน',
                          '10':'ตุลาคม',
                          '11':'พฤศจิกายน',
                          '12':'ธันวาคม'}
    def __init__(self):
        self.Now()
        self.getFullDate()
    #enddef

    def getVersion(self):
        return self.__version__
    #enddef

    def getMonthNameTH(self,MonthNo):
        return self.MonthName[MonthNo]
    #enddef
    def getMonthNameShortTH(self,MonthNo):
        return self.MonthNameShort[MonthNo]
    #enddef

    def Now(self):
        self.CurrentTime = datetime.datetime.now()
    #enddef

    def getNowDate(self,format="%Y-%m-%d"):
        self.Now()
        return self.CurrentTime.strftime(format)
    #enddef

    def getNowDateTimeMilisec(self,format="%Y-%m-%dT%H:%M:%S.%f",millisec_digit = 3):
        if(millisec_digit <= 0):
            millisec_digit = 3
        #endif
        self.Now()
        self.CurrentTime.strftime(format)
        format_datetime = self.CurrentTime.strftime(format)[:-millisec_digit]
        format_datetime_full = f"{format_datetime}+07:00"
        return format_datetime_full
    #enddef

    def getNowTime(self,format = "%H:%M:%S"):
        self.Now()
        return self.CurrentTime.strftime(format)
    #enddef

    def getNowDateTime(self,format="%Y-%m-%d %H:%M:%S"):
        self.Now()
        return self.CurrentTime.strftime(format)
    #enddef

    def setNow(self,curtime):
        self.CurrentTime = curtime
    #enddef

    def getCurDate(self,format = '%d'):
        libformat = set(['%d','%A','%a'])
        if(not (format in libformat)):
            format = '%d'
        #end if
        self.CurDate = self.CurrentTime.strftime(format)
        return self.CurDate
    #enddef

    def getCurMonth(self,format="%m"):
        libformat = set(['%b','%B','%m'])
        if(not (format in libformat)):
            format = '%m'
        #end if
        self.CurMonth = self.CurrentTime.strftime(format)
        return self.CurMonth
    #enddef

    def getMinusDate(self,nominusday,format="%Y-%m-%d %H:%M:%S",DateToMinus = "",DateToMinusFormat = "%Y-%m-%d"):
        if(len(str(DateToMinus)) != 0 and len(str(DateToMinusFormat)) != 0):
            DateMakeMinus = datetime.datetime.strptime(DateToMinus, DateToMinusFormat)
            minusdate = DateMakeMinus + timedelta(days = - nominusday)
        else:
            self.Now()
            minusdate = self.CurrentTime + timedelta(days = - nominusday)
        #endif
        return minusdate.strftime(format)
    #enddef

    def getPlusDate(self,noplusday,format="%Y-%m-%d %H:%M:%S"):
        self.Now()
        minusdate = self.CurrentTime + timedelta(days = noplusday)
        return minusdate.strftime(format)
    #enddef

    def getCur4Year(self,format ='%Y'):
        libformat = set(['%Y','%y'])
        if(not (format in libformat)):
            format = '%Y'
        #end if
        self.CurYear = self.CurrentTime.strftime(format)
        return self.CurYear
    #enddef

    def getCur4YearThai(self):
        self.CurYearThai = str(int(self.CurrentTime.strftime("%Y"))+543)
        return self.CurYearThai
    #enddef

    def getCur2YearThai(self):
        tmpYearThai2 = str(int(self.CurrentTime.strftime("%Y"))+43)
        self.CurYearThai2 = tmpYearThai2[2:4]
        return  self.CurYearThai2
    #enddef

    def getFullDate(self):
        self.getCurDate()
        self.getCurMonth()
        self.getCur4Year()
    #enddef

    def getFullDateTH(self,date,format = '%d-%m-%Y'):
        c = time.strptime(date,format)
        date = time.strftime("%d",c)
        month = time.strftime("%m",c)
        year = str(int(time.strftime("%Y",c))+543)
        MonthName = self.getMonthNameTH(month)
        self.FullDateTh = str(date)+" "+str(MonthName)+" "+str(year)
        return self.FullDateTh
    #enddef
    
    def getShortDateTH(self,date,format = '%d-%m-%Y'):
        c = time.strptime(date,format)
        date = time.strftime("%d",c)
        month = time.strftime("%m",c)
        year = str(int(time.strftime("%Y",c))+543)[2:4]
        MonthName = self.getMonthNameShortTH(month)
        self.FullDateTh = str(date)+" "+str(MonthName)+" "+str(year)
        return self.FullDateTh
    #enddef
    def string2date(self,date_time_str,format_time = '%Y-%m-%d %H:%M:%S'):
        return datetime.datetime.strptime(date_time_str, format_time)
    #enddef
    def sleep(self,TimeSeconds = 5):
        time.sleep(TimeSeconds)
    #endif
    def getNowDate2(self,format="%Y%m%d"):
        self.Now()
        return self.CurrentTime.strftime(format)
    #enddef
    def getPlusMinutes(self,noMinutes,format="%Y-%m-%d %H:%M:%S"):
        self.Now()
        minusdate = self.CurrentTime + timedelta(minutes = noMinutes)
        return minusdate.strftime(format)
    #enddef

#endclass
