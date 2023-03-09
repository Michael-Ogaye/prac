from threading import Thread,current_thread
import time

def ast():
    curr=current_thread()
    time.sleep(2)
    print(f'i am done running my thread {curr} ...')

t1=Thread(target=ast)
t2=Thread(target=ast)
t1.start()
t2.start()
class t3(Thread):

    def run(self) -> None:
        t1.join(3)
        return super().run()
    

t3.start()