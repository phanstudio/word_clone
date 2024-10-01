import flet as ft
from .constants import *
from .utility import *

class EditNoteView(ft.Column):
    def __init__(self):
        super().__init__(
            tight= True,
            expand= True,
        )
        self.head = 'Untitled Note'
        # add save load here

        render_engine = Renderer(self)
        self.tool_bar = format_panel(render_engine)
        self.editor = Editor(render_engine)
                    
        self.controls= [ 
            self.header(),
            ft.Divider(1),
            ft.Container(
                render_engine,
                padding= 5,
                expand= True,
            ),
            self.tool_bar,
            self.editor,
        ]
    
    def header(self):
        self.tit = ft.Ref[ft.TextField]()
        head = ft.Row([
            ft.IconButton(icon= ft.icons.CHEVRON_LEFT, icon_color= GOLD,
                on_click= self.onback),
            ft.TextField(value=self.head.title(), 
                      ref = self.tit,
                      dense= True,
                      width = 200,
                      multiline= True,
                      border= ft.InputBorder.NONE,
                      text_align= 'center',
                      text_style= ft.TextStyle(
                            weight=  BOLD,
                        ),
                    ),
            ft.IconButton(icon= ft.icons.HELP, icon_color= GOLD,
                on_click= lambda _: print('#')),
            ], alignment= ft.MainAxisAlignment.SPACE_BETWEEN)
        return head
    
    def onback(self, e: ft.ControlEvent):
        ...
