from models.ModelFigureInfo import ModelFigureInfo
from models.ModelFigureType import ModelFigureType
from models.ModelManufacturer import ModelManufacturer
from models.ModelSeries import ModelSeries

from tkinter import ttk
from tkinter import Toplevel
from PIL import Image, ImageTk

class MyApp:
    def __init__(self, root) -> None:
        self._root = root
        self._main_frame = ttk.Frame(self._root)
        self._main_frame.pack(fill="both", expand=True)
        self._table_frame = None
        self.show_landingPage()

    def show_landingPage(self):
        
        for widget in self._main_frame.winfo_children():
            widget.destroy()
        
        self._landing_img = Image.open("assets/img/c5e85892dabb447a57f08baca16965c1.jpg")
        self._landing_img = self._landing_img.resize((500, 250), Image.ANTIALIAS)
        self._landing_img = ImageTk.PhotoImage(self._landing_img)
        landing_img_label = ttk.Label(self._main_frame, image=self._landing_img)
        landing_img_label.pack()

        landing_button = ttk.Button(self._main_frame, text="Get in!", command=self.show_tablePage)
        landing_button.pack()

    def show_tablePage(self):
        for widget in self._main_frame.winfo_children():
            widget.destroy()
        
        navbar = ttk.Frame(self._main_frame)
        navbar.pack(side="top", fill="x")
        
        figures_btn = ttk.Button(navbar, text="Figures", command= self.show_figures)
        figures_btn.pack(side="left")
        
        types_btn = ttk.Button(navbar, text="Types", command=self.show_figureType)
        types_btn.pack(side="left")
        
        manufacturers_btn = ttk.Button(navbar, text="Manufacturers", command=self.show_manufacturers)
        manufacturers_btn.pack(side="left")
        
        series_btn = ttk.Button(navbar, text="Series", command=self.show_series)
        series_btn.pack(side="left")
        
        self._table_frame = ttk.Frame(self._main_frame)
        self._table_frame.pack(fill="both", expand=True)
        
        self.show_figures()
    
    # nav button for figures
    def show_figures(self):
        for widget in self._table_frame.winfo_children():
            widget.destroy()
        
        # get figure Info data
        models = ModelFigureInfo()
        data = models.getAll()
        
        # table
        figureTable = ttk.Treeview(
            self._table_frame, 
            columns=("number","name","series"),
            show="headings"
        )
        figureTable.heading("number", text="No.")
        figureTable.heading("name", text="Name")
        figureTable.heading("series", text="Series")
        
        def on_select(event):
            selected_item = figureTable.selection()[0]
            figure_id = figureTable.item(selected_item)['tags'][0]
            self.show_figureDetails(figure_id)
        
        figureTable.bind("<<TreeviewSelect>>", on_select)
        
        no = 0
        for row in data:
            figure_id = row.getId()
            no +=1
            name = row.getName()
            series = row.getSeries()
            
            figureTable.insert("", "end", values=(no, name, series), tags=(figure_id))
        
        figureTable.pack()
        models.close()
    
    def show_figureDetails(self, id):
        
        models = ModelFigureInfo()
        data = models.getById(id)
        
        name = data.getName()
        img_path = data.getImg()
        type = data.getType()
        series = data.getSeries()
        man = data.getManufacturer()
        
        # creating the pop-up
        window = Toplevel()
        window.title(name)
        
        name_label = ttk.Label(window, text=name)
        name_label.pack()
        
        img = Image.open("assets/img/figures/"+img_path)
        img = img.resize((200,200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        img_label = ttk.Label(window, image=img)
        img_label.image = img
        img_label.pack()
        
        type_title = ttk.Label(window, text="Type:")
        type_title.pack()
        type_label = ttk.Label(window, text=type)
        type_label.pack()
        
        series_title = ttk.Label(window, text="Series:")
        series_title.pack()
        series_label = ttk.Label(window, text=series)
        series_label.pack()
        
        man_title = ttk.Label(window, text="Manufacturer")
        man_title.pack()
        man_label = ttk.Label(window, text=man)
        man_label.pack()
        models.close()
        
    # nav button for figure types table
    def show_figureType(self):
        for widget in self._table_frame.winfo_children():
            widget.destroy()
        
        # get type data
        model = ModelFigureType()
        data = model.getAll()
        
        # setup table
        
        typeTable = ttk.Treeview(
            self._table_frame,
            columns=("no", "name", "nFig"),
            show="headings"
        )
        typeTable.heading(column="no", text="No.")
        typeTable.heading(column="name", text="Name")
        typeTable.heading(column="nFig", text="Number of Figures")
        
        no = 0
        for row in data:
            no += 1
            name = row.getName()
            nFig = row.getNFigures()
            
            typeTable.insert("", "end", values=(no, name, nFig))
        
        typeTable.pack()
        model.close()
        
    # nav button for manufacturer table
    def show_manufacturers(self):
        for widget in self._table_frame.winfo_children():
            widget.destroy()
        
        # get manufacturer data
        model = ModelManufacturer()
        data = model.getAll()
        
        # set manufacturer table
        table = ttk.Treeview(
            self._table_frame,
            columns=("no", "name", "nFig"),
            show="headings"
        )
        table.heading(column="no", text="No.")
        table.heading(column="name", text="Name")
        table.heading(column="nFig", text="Number of Figures")
        
        no = 0
        for row in data:
            no += 1
            name = row.getName()
            nFig = row.getNFigures()
            
            table.insert("", "end", values=(no, name, nFig))

        table.pack()
        model.close()
        
    # nav button for series/ brands table
    def show_series(self):
        for widget in self._table_frame.winfo_children():
            widget.destroy()
        
        # get series data
        model = ModelSeries()
        data = model.getAll()
        
        # set series table
        table = ttk.Treeview(
            self._table_frame,
            columns=("no", "name", "nFig"),
            show="headings"
        )
        table.heading(column="no", text="No.")
        table.heading(column="name", text="Name")
        table.heading(column="nFig", text="Number of Figures")
        
        no = 0
        for row in data:
            no += 1
            name = row.getName()
            nFig = row.getNFigures()
            
            table.insert("", "end", values=(no, name, nFig))

        table.pack()
        model.close()

