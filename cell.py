from tkinter import Button, Label
import random
from webbrowser import get
import settings
import ctypes
import sys

class Cell:
    all = []
    cell_remaining = settings.CELL_COUNT - settings.MINES_COUNT
    cell_count_label_object = None
    cell_game_new = None
    def __init__(self,x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None

        self.x = x
        self.y = y

        Cell.all.append(self)
        

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            
        )
        btn.bind('<Button-1>', self.left_click_actions )
        btn.bind('<Button-3>', self.right_click_actions )
        self.cell_btn_object = btn
        
    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            text=f"Cells Left:{Cell.cell_remaining}",
            width=12,
            height=4,
            font=("",30)
            )
        Cell.cell_count_label_object = lbl
        
    @staticmethod
    def create_game_name(location):
        lbl2 = Label(
            location,
            bg='black',
            fg='white',
            text=f"MINESWEEPER",
            width=15,
            height=4,
            font=("",30)
            )
        Cell.cell_game_new = lbl2
        
    def left_click_actions(self, event):
        if self.is_mine_candidate:
            return
        if self.is_mine:
            self.show_mine()
        else:
            
            self.show_with_neigbors()
            # Cell sayisi 0'a düþtüðünde oyuncu kazanýr.
            if Cell.cell_remaining == 0:
                ctypes.windll.user32.MessageBoxW(0,'SEN BU ISI BILIYOSUN ADAMIM!', 'Kazandiniz!',0)
                sys.exit()

                  


        # Eðer cell açýlmýþsa o cell için yapýlan eylemleri iptal et
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>') 

    def show_with_neigbors(self):
        if self.surrounded_cells_mines_lenght == 0:
                for cell_obj in self.surrounded_cells:
                    if cell_obj.is_opened:
                        continue
                    cell_obj.show_cell()
                    cell_obj.show_with_neigbors()
                    
        self.show_cell()   
            
    def get_cell_by_axis(self, x,y):
        # Return a cell object based on the value of x,y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
                cells = [
            self.get_cell_by_axis(self.x -1, self.y -1),
            self.get_cell_by_axis(self.x -1, self.y),
            self.get_cell_by_axis(self.x -1, self.y +1),
            self.get_cell_by_axis(self.x, self.y -1),
            self.get_cell_by_axis(self.x +1, self.y -1),
            self.get_cell_by_axis(self.x +1, self.y),
            self.get_cell_by_axis(self.x +1, self.y +1),
            self.get_cell_by_axis(self.x ,self.y +1),
            
            ]
                cells = [cell for cell in cells if cell is not None]
                return cells
    @property
    def surrounded_cells_mines_lenght(self):
       counter = 0
       for cell in self.surrounded_cells:
           if cell.is_mine:
              counter += 1
             
       return counter

    def show_cell(self):
        if self.is_mine_candidate or self.is_opened:
            return
        
        Cell.cell_remaining -= 1
        self.cell_btn_object.configure(text=self.surrounded_cells_mines_lenght)
        # Replace the text of cell count label with the newer count
        if Cell.cell_count_label_object:
            Cell.cell_count_label_object.configure(
                text= f"Cells Left: {Cell.cell_remaining}"
                )
            # mayýn olarak iþaretlenmiþ bir yeri açarken rengini eski haline döndürme
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
                )

            # Mark the cell as opened (Use is as the last line of this method)
            self.is_opened = True
        
    def show_mine(self):
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0,'BUMMMMMMM!!!', 'Game Over',0)

        sys.exit()
        # birinci 0 baþlýk ikinci 0 baþlýk
        # 0=tamam,1=tamam,iptal, 3=evet,hayýr,iptal 4=evet,hayýr etc.

    def right_click_actions(self, event):
       if self.is_opened:
           return
       if not self.is_mine_candidate:
           self.cell_btn_object.configure(
               bg='orange'
               )
           self.is_mine_candidate = True
       else:
           self.cell_btn_object.configure(
               bg='SystemButtonFace'
               )
           self.is_mine_candidate = False
           

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
            )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
    
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"

    



