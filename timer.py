import timer (odject):


class timer(odject):
    def _init_(self,verbose=false):
        self.verbose = verbose

def _enter _(self):
    self.start_time = time.time()
    return self




def _exit _(self, exc_type, exc_vel, exc_tb):
self.end_time = time.time()
self.secs  = self.end_time - self.start_time
