import threading

import customtkinter

from utils.graph import draw_graph
from utils.list import city, type_cv
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from utils.models import status_parser
from utils.parser import get_parser


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.canvas_widget = None
        self.fig = None
        self.canvas = None
        self.title("Real Estate Analyst")
        self.geometry("1200x800")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.main_frame = customtkinter.CTkFrame(self)
        self.main_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")

        self.button = customtkinter.CTkButton(self, text="Update", command=self.get_data)
        self.button.grid(row=10, column=0, padx=10, pady=10, sticky="w")

        self.city = customtkinter.CTkLabel(self.main_frame, text="City")
        self.city.grid(row=1, column=0)
        self.city_menu = customtkinter.CTkOptionMenu(self.main_frame, values=list(city.keys()))
        self.city_menu.grid(row=2, column=0)

        self.type = customtkinter.CTkLabel(self.main_frame, text="Type")
        self.type.grid(row=3, column=0)
        self.type_menu = customtkinter.CTkOptionMenu(self.main_frame, values=type_cv)
        self.type_menu.grid(row=4, column=0)

    def get_data(self):
        threading.Thread(target=self.get_data_thread()).start()

    def get_data_thread(self):
        self.button.configure(state="disabled")

        selected_city = city.get(self.city_menu.get())
        selected_type = type_cv.index(self.type_menu.get())

        def run_task():
            get_parser(status_parser(selected_city, str(selected_type)))
            self.update_table()
            self.button.configure(state="normal")

        threading.Thread(target=run_task).start()

    def update_table(self):
        self.fig = draw_graph()
        # self.canvas_widget.destroy()
        if self.canvas is not None:
            self.canvas.get_tk_widget().destroy()
        if self.fig is not None:
            self.canvas = FigureCanvasTkAgg(self.fig, master=self)
            self.canvas_widget = self.canvas.get_tk_widget()
            self.canvas_widget.grid(row=0, column=1, sticky="n")
