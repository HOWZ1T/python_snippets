# NOTE: this function is a snippet from a larger class object that is a subclass of threading.Thread

def interrupt(self, exctype):
    id = self.id
    is_verbose = self.verbose  # capture this value for logging control
    if not self.isAlive():
        raise threading.ThreadError("the ExThread: " + self.id + " is not active!")

    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(self.ident, ctypes.py_object(exctype))

    if res == 0:
        raise Exception("could not interrupt ExThread: " + self.id + " as it was not found!")
    elif res != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(self.ident, 0)
        raise SystemError("PyThreadState_SetAsyncExc failed")

    if is_verbose:
        print("ExThread: {} interrupted! at {}".format(self.id, time.strftime("%H:%M:%S", time.gmtime())))
