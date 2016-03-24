import io
import time
root = tk.Tk()
root.title("display a website image")
# a little more than width and height of image
w = 520
h = 320
x = 80
y = 100

root.geometry("%dx%d+%d+%d" % (w, h, x, y))

photos = [0] * 7
for i in range(5):
    photos[i] = tk.PhotoImage(file="Hypnotoad.gif", format = "gif -index " + str(i))
    print(i)
# create a white canvas
cv = tk.Canvas(bg='white')
cv.pack(side='top', fill='both', expand='yes')
# put the image on the canvas with
# create_image(xpos, ypos, image, anchor)
for i in range(5):
    cv.create_image(10, 10, image=photos[i], anchor='nw')
    #time.sleep(0.5)
root.mainloop()