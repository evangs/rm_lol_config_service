import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import os
import time

LOL_CONFIG = 'c:/Games/League of Legends/Config/game.cfg'


class AppServerSvc (win32serviceutil.ServiceFramework):
    _svc_name_ = "rm LOL config"
    _svc_display_name_ = "rm LOL config"

    def __init__(self,args):
        win32serviceutil.ServiceFramework.__init__(self,args)
        self.hWaitStop = win32event.CreateEvent(None,0,0,None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_,''))
        self.main()

    def main(self):
        while True:
            if os.path.isfile(LOL_CONFIG):
                os.remove(LOL_CONFIG)

            time.sleep(300)

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(AppServerSvc)