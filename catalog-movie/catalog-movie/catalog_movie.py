#!/usr/bin/env python3

import tkinter as tk
from client.gui_app import Frame,menu_bar


def main ():
    root = tk.Tk()
    root.title('Catalog Movies')
    root.resizable(0,0)  
    
    menu_bar(root)
    
    
    app = Frame(root=root)
    app.mainloop()


if __name__ == '__main__':
    
    main()

