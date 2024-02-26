from tkinter import *
from cell import Cell 
import settings
import utils


root = Tk()
# Override the setting of the window
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper Game")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='black', 
    width=utils.width_prct(100),
    height=utils.height_prct(25)
 )
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='black', 
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25))


center_frame = Frame(
    root,
    bg='black',
    width= utils.width_prct(75),
    height=utils.height_prct(75)
)
center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25),
    
) 


for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x,y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
            
            )
        

# Call the label from the Cell clas
Cell.create_cell_count_label(left_frame)        
Cell.cell_count_label_object.place(
    x=0, y=-57
    )
Cell.create_game_name(top_frame)
Cell.cell_game_new.place(
    x=(top_frame.winfo_width() // 2) ,y=0
    )
root.update()
Cell.cell_game_new.place(
    x=(top_frame.winfo_width() // 2 - Cell.cell_game_new.winfo_width() // 2 ) ,y=0
    )
print(Cell.cell_game_new.winfo_width())
Cell.randomize_mines()



#run the window
root.mainloop()
