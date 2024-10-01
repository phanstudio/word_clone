import flet as ft
from .constants import *
from .note_render import *

class Renderer(ft.Column):
    def __init__(self, _parent):
        super().__init__(
            expand= True
        )
        self.scroll = ft.ScrollMode.ADAPTIVE
        self.ST = ""
        self.NT = Nt()
        self.PT = []
        self.update = False
        self.temp_prop = PropT()#it= True, wt= BOLD)
        self.main_parent = _parent

        self.note = Notes()
        self.controls = [
            self.note,
            ft.Divider(0, thickness=0, color= TRANSPARENT)
        ]
    
    def did_mount(self):
        # self.loader()
        # self.get_child('t')._render_properties()
        return super().did_mount()
    
    def render(self):
        length = len(self.PT)
        if len(self.ST) > 0:
            note = []
            for i in range(length):
                start = 0 if self.NT[i] < 0 else self.NT[i]# +1
                if i != length-1 and length > 1:
                    text = self.ST[start: self.NT[i+1]]#+1]
                else:
                    text = self.ST[start:]
                note.append(ft.TextSpan(f'{text}',style= ft.TextStyle(**self.PT[i].kw)))
                # note.append(ft.TextSpan(f'({text})',style= ft.TextStyle(**self.PT[i].kw))) # test
            self.note.set(note)
        else:
            self.note.set([])
    
    def correct_overlap(self):
        if self.NT[-1] == len(self.ST)-1:
            self.NT.pop()
            self.PT.pop()
        
        fuse = False
        # Using a set to keep track of unique elements
        unique_elements = set()
        # Using list comprehension to find duplicates
        duplicates = {item for item in self.NT if (self.NT.count(item) > 1 and item not in unique_elements)}

        new_nt = Nt(set(self.NT))
        new_nt.sort()
        duplicate_index = [new_nt.index(i) for i in duplicates]

        if len(duplicate_index) != 0:
            pos = min(duplicate_index)
            if self.PT[pos-1] == self.PT[pos+1]:
                fuse = True
            
        self.NT = new_nt
        for i in duplicate_index:
            self.PT.pop(i)
        
        if fuse:
            self.NT.pop((pos-1)+1)
            self.PT.pop((pos-1))
        
        if len(self.ST) == 0:
            self.PT = []
            self.NT = Nt()

    def loader(self):
        test = "()(love you very much you alot) (b)( alot)" 
        #"()(love you very much you) (b)( alot)" # "(b)(love you ) ()(very much ) (b)(thank you) ()( alot)"

        pt, nt, st = [], [], []
        for i in convert_to_md(test):
            st.append(i[1])
            pt.append(i[0])
            nt.append(len(i[1]))
        nt =  nt
        
        lt = [sum(nt[:i+1]) for i in range(len(nt))] # -1
        lt.pop()
        lt = Nt([-1] + lt)

        pl = []
        for i in pt:
            val = PropT()
            if i == "b":
                val.set('weight', ft.FontWeight.BOLD)
            pl.append(val)
        st = "".join(st)
        
        self.NT = lt
        self.PT = pl
        self.ST = st

        self.get_child('e').editer.value = st
        self.get_child('e').editer.update()
        self.render()

    def get_child(self, _key):
        _children = {
            't':self.main_parent.tool_bar,
            'e': self.main_parent.editor,
            }
        return _children[_key]
    
    def save_property(self, _pos):
        self.NT.append(_pos-1)
        self.PT.append(self.temp_prop.copy())

class simple_button(ft.UserControl):
    def __init__(self, custom_data , icon : ft.Icon = '', img = '', size = 15,
                func= lambda _: print(9)):
        super().__init__()
        custom_color = SURFACE
        custom_selected_color = ON_SURFACE
        custom_style = ft.ButtonStyle(
                            overlay_color= ft.colors.with_opacity(0.2, custom_color),
                            padding= 0,
                        )

        if icon == '':
            frame = ft.IconButton(
                        style= custom_style,
                        content= ft.Image(
                            img, 
                            width= size-3, height= size-3,
                            fit= ft.ImageFit.CONTAIN,
                            color= custom_color,
                        ),
                        on_click= func,
                        data = custom_data,
                    )
        else:
            frame = ft.IconButton(
                        icon, 
                        icon_color= custom_color,
                        style= custom_style,
                        icon_size= size, 
                        on_click= func,
                        # selected= True,
                        selected_icon= icon,
                        data = custom_data,
                        selected_icon_color= custom_selected_color,
                    )
        self.frame = frame
    
    def get(self):
        return self.frame

    def build(self):
        return self.frame

class format_panel(ft.Container):
    def __init__(self, engine:Renderer):
        super().__init__()
        self.content = ft.Row([
                simple_button(icon=ft.icons.FORMAT_SIZE, custom_data= 'T',
                                size= 20, func= lambda _: self.onclick('T')),
                simple_button(icon=ft.icons.FORMAT_BOLD, custom_data= 'B',
                                size= 20, func= lambda _: self.onclick('B')),
                simple_button(icon=ft.icons.FORMAT_ITALIC_ROUNDED, custom_data= 'I',
                                size= 20, func= lambda _: self.onclick('I')),
            ],
            spacing= 0,
            alignment= ft.MainAxisAlignment.SPACE_EVENLY,
        )
        self.engine = engine
        self.bgcolor = GOLD
        self.border_radius = ft.border_radius.horizontal(5, 5)
        
    def onclick(self, typ):
        if typ == "B":
            _value = BOLD if self.engine.temp_prop.get('weight') != BOLD else None
            self.engine.temp_prop.set('weight', _value)
        if typ == "I":
            _value = True if self.engine.temp_prop.get('italic') != True else False
            self.engine.temp_prop.set('italic', _value)

        self._render_properties()
        self.engine.get_child('e').focus()
        self.engine.update = True
    
    def _render_properties(self):
        B = False if self.engine.temp_prop.get('weight') != BOLD else True
        I = False if self.engine.temp_prop.get('italic') != True else True
        for i in self.content.controls:
            self.check_data(i, 'B', B)
            self.check_data(i, 'I', I)
    
    def check_data(self, i, k, v):
        if i.get().data == k:
            i.get().selected = v
            i.get().update()

class Notes(ft.Container):
    def __init__(self):
        super().__init__(
            content= ft.Text(
                spans=[]
            ),
        )
    
    def get(self):
        return self.content.spans
    
    def set(self, _value):
        self.content.spans = _value
        self.update()

class Editor(ft.Container):
    def __init__(self, engine:Renderer):
        super().__init__()
        self.editer = ft.TextField(on_change= self._onchange, multiline= True, max_lines= 2, selection_color= GOLD, focused_border_color= GOLD)
        self.content = self.editer
        self.engine = engine
    
    def focus(self):
        self.editer.focus()
        self.editer.update()

    def _onchange(self, e):
        # template 
        temp = self.editer.value

        # check and compare ✅
        changes = nhistory(self.engine.ST, temp)
        pos = min(i[1] for i in changes)

        # check the previous properties
        if not any(self.engine.NT < pos): # start
            self.engine.save_property(pos)
            self.engine.update = False
        else:
            current_pos = max(i for i in range(len(self.engine.NT)) if self.engine.NT[i] < pos)
            if self.engine.update:
                self.engine.update = False
                if (self.engine.PT[current_pos] != self.engine.temp_prop):
                    if any(i for i in changes if i[0] == 'delete'):
                        for i in changes:
                            self.engine.NT = self.engine.NT.process_list(*i)
                    else:
                        subbed = False
                        new_pos = pos
                        if any(i for i in changes if i[0] == 'replace'):
                            sub_lenght = sum([i[2] for i in changes if i[0] == 'replace'])
                            self.engine.NT.append(new_pos)
                            self.engine.NT.append(new_pos + sub_lenght) # +1
                            new_pos = new_pos+sub_lenght
                            subbed = True
                        
                        if pos < len(self.engine.ST):
                            if any(i for i in changes if i[0] == 'insert'):
                                lenght = sum([i[2] for i in changes if i[0] == 'insert'])
                                if not subbed:
                                    self.engine.NT.append(new_pos)
                                self.engine.NT = self.engine.NT.process_set(new_pos, lenght, True)
                                if not subbed:
                                    self.engine.NT.append(new_pos)
                        else:
                            self.engine.save_property(pos+1)
                        
                        self.engine.NT.sort()
                        if pos < len(self.engine.ST):
                            self.engine.PT = self.engine.PT[:current_pos+1] + [
                                self.engine.temp_prop.copy()] + self.engine.PT[current_pos:]

                else:
                    self.engine.NT = self.engine.NT.calculate_Nt(changes)
                    self.engine.update = False
            else:
                if (self.engine.PT[current_pos] != self.engine.temp_prop): # add indicator
                    self.engine.temp_prop = self.engine.PT[current_pos].copy()
                    self.engine.get_child('t')._render_properties()
                # edit
                if any(i for i in changes if i[0] == 'delete'):
                    for i in changes:
                        self.engine.NT = self.engine.NT.process_list(i[0], i[1]+1, i[2])
                else: # an error
                    for i in changes:
                        self.engine.NT = self.engine.NT.process_list(*i)

        # render ✅
        self.engine.ST = temp
        if self.engine.NT.overlap() or (self.engine.NT[-1] == len(self.engine.ST)-1 and 
                any(i for i in changes if i[0] == 'delete')):
            self.engine.correct_overlap()
        
        self.engine.render()
        self.update()
