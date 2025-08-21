# make a colorfull screen in tkinter
import tkinter as tk
import random

def random_color():
	return f'#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}'

class MovingMenu(tk.Frame):
	def __init__(self, master, button_texts):
		super().__init__(master)
		self.master = master
		self.buttons = []
		self.positions = []
		self.directions = []
		self.width = 500
		self.height = 80
		self.pack(fill=tk.X)
		self.canvas = tk.Canvas(self, width=self.width, height=self.height, bg='black', highlightthickness=0)
		self.canvas.pack(fill=tk.X)
		for i, text in enumerate(button_texts):
			btn = tk.Button(self.canvas, text=text, bg=random_color(), fg='white', font=('Arial', 14, 'bold'))
			btn_id = self.canvas.create_window(10 + i*110, 40, window=btn, anchor='nw')
			self.buttons.append((btn, btn_id))
			self.positions.append(10 + i*110)
			self.directions.append(1)
		self.animate()

	def animate(self):
		for i, (btn, btn_id) in enumerate(self.buttons):
			# Move horizontally
			self.positions[i] += self.directions[i] * 3
			if self.positions[i] > self.width - 100:
				self.directions[i] = -1
			elif self.positions[i] < 0:
				self.directions[i] = 1
			self.canvas.coords(btn_id, self.positions[i], 40)
			# Change color
			btn.config(bg=random_color())
		self.after(60, self.animate)

if __name__ == "__main__":
	root = tk.Tk()
	root.title("Colorful Moving Menu")
	root.geometry("500x120")
	menu = MovingMenu(root, ["Home", "Settings", "About", "Exit"])
	root.mainloop()