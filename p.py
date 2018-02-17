#!/usr/bin/python
# Copyright (c) 2017 CVSC
# Distributed under the MIT/X11 software license, see the accompanying
# file license.blockt or http://www.opensource.org/licenses/mit-license.php.

from Tkinter import *
import thread
import time
import tkMessageBox
from main import *

class silme:

    def __init__(self, root):
        self.root = root
        self.frame = Frame(self.root)
        self.frame.pack()
        self.c = StringVar()
        self.t = StringVar()
        self.addr_ = StringVar()
        self.balance_ = StringVar()
        thread.start_new_thread(self._update, ())
        self.addr()
        self.mining()
        self.balance()
        self.send()
        

    def _update(self):

        addr = GenerateNewKey()
        while True:
            
            
            self.addr_.set(addr)
            self.balance_.set(CWalletDB().GetBalance())
            time.sleep(10)
    
    def addr(self):

        addr_f = LabelFrame(self.frame, text="Address", padx=5, pady=5)
        addr_f.grid(sticky=E+W)
        Entry(self.frame, state="readonly", textvariable=self.addr_, width=50).grid(in_=addr_f)



    def balance(self):

        addr_balance = LabelFrame(self.frame, text="balance", padx=5, pady=5)
        addr_balance.grid(sticky=E+W)
        Entry(self.frame, state="readonly", textvariable=self.balance_, width=50).grid(in_=addr_balance)


    def mining(self):
        mining_f = LabelFrame(self.frame, text="Mining", padx=3, pady=5)
        mining_f.grid(sticky=E+W)
        send_b = Button(self.frame, command=self.__mining, text="Start").grid(in_=mining_f, row=0, column=4, sticky=W+E)

    def send(self):
        send_f = LabelFrame(self.frame, text="Send Coin", padx=5, pady=15)
        send_f.grid(sticky=E+W)
        to_l = Label(self.frame, text="To: ").grid(in_=send_f)
        self.to = Entry(self.frame)
        self.to.grid(in_=send_f, row=0, column=1, sticky=W)
        amount_l = Label(self.frame, text="Amount: ").grid(in_=send_f, row=0, column=3, sticky=W)
        self.amount = Entry(self.frame, width=4)
        self.amount.grid(in_=send_f, row=0, column=4, sticky=W)
        Label(self.frame, text="   ").grid(in_=send_f, row=0, column=5)
        Label(self.frame, text="   ").grid(in_=send_f, row=0, column=2)
        send_b = Button(self.frame, command=self._send, text="Send").grid(in_=send_f, row=0, column=8, sticky=W+E)
            
    def _send(self):
        amount = self.amount.get()
        recipt = self.to.get()
        if not CWalletDB().GenerateTransaction(int(amount), str(recipt)):
            tkMessageBox.showinfo("Error", CWalletDB().GenerateTransaction(int(amount), str(recipt)))
        else:
            tkMessageBox.showinfo("Sending...", "Your coins are being sent, this could take a while.")

    def __mining(self):
        os.system('./miner &')




if __name__ == "__main__":

    if not os.path.exists(GetAppDir()):
        os.system('python main.py')
    
    root = Tk()
    root.geometry("450x250+350+100")
    silme(root=root)
    root.title("Silme Client")
    root.mainloop()