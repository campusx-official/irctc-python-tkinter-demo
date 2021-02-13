from tkinter import *
import requests

class IRCTC:

    def __init__(self):
        self.load_gui()

    def load_gui(self):
        self.root = Tk()
        self.root.title("IRCTC App")
        self.root.minsize(300, 500)
        self.root.maxsize(300, 500)

        self.label = Label(self.root,text="Enter Train No")
        self.label.pack(pady=(10,10))

        self.train_no = Entry(self.root)
        self.train_no.pack(ipadx=80,ipady=5)

        self.btn = Button(self.root,text="Fetch Stations",command=lambda:self.fetch_data())
        self.btn.pack(pady=(10,10))

        self.result = Label(self.root,text="",bg="#16a085",fg="#fff")
        self.result.pack()

        self.root.configure(background="#16a085")
        self.root.mainloop()

    def fetch_data(self):
        # fetch the train_no
        train_no = self.train_no.get()

        url = "https://indianrailapi.com/api/v2/TrainSchedule/apikey/30c382602bfa67c8a7c580e6cfe2becb/TrainNumber/{}".format(train_no)

        data = requests.get(url)
        data = data.json()

        self.display_data(data)

    def display_data(self,data):

        result = ""
        for i in data['Route']:
            result = result + i['StationName'] + " " + "\n"

        #print(result)
        self.result['text'] = result

obj = IRCTC()
