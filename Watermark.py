from tkinter import *
from tkinter import filedialog
from wand.image import Image


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        a = Button(text="Browse Input Image", bd='5', command=self.browse)
        a.place(relx=0.5, rely=0.3, anchor=CENTER)

        b = Button(text="Browse Input Folder (Yet to come)", bd='5')
        b.place(relx=0.5, rely=0.5, anchor=CENTER)

        c = Button(text="EXIT", bd='5', command=self.client_exit)
        c.place(relx=0.5, rely=0.7, anchor=CENTER)

    def client_exit(self):
        exit()

    def browse(self):
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("jpg files", "*.jpg"), ("jpeg files", "*.jpeg"), ("png files", "*.png")))
        with Image(filename=root.filename) as background:
            print('Background width = ', background.width)
            i = background.width
            print('Background height = ', background.height)
            q = background.height
            with Image(filename='watermark.jpg') as watermark:
                print('Watermark width = ', watermark.width)
                y = watermark.width
                print('Watermark height = ', watermark.height)
                z = watermark.height
                background.watermark(image=watermark, transparency=0.5, left=i - y - 100, top=q - z - 100)
            background.save(filename='result.jpg')


root = Tk()
root.title("Watermark Application")
root.geometry("400x300")
app = Application(root)
root.mainloop()
