from threading import Thread
def run():
  open("x.txt","w")
def keep_alive():  
    t = Thread(target=run)
    t.start()
