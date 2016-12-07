define narrator = Character(None, kind=nvl)

label nvl_clear:
    nvl clear
    return

init python:
    current_letter = None
    
    def start_letter(n):
        global current_letter
        current_letter = n
        renpy.show('white', what=Solid('#fff'))

init python:
    class NvlLayout(object):
        def __init__(self, paddings, imgpos):
            self.paddings = paddings
            self.imgpos = imgpos
    
    nvl_layout_order = ['left', 'right']
    nvl_layouts = dict(
        left=NvlLayout([0, 420], [0.94, 0.5]),
        right=NvlLayout([420, 0], [0.06, 0.5]),
    )
    nvl_layout = None
    
    def set_padding(paddings):
        global narrator
        c_args = dict(kind=nvl)
        for i, d in enumerate(nvl_layout_order):
            c_args['window_{}_padding'.format(d)] = paddings[i]
        narrator = Character(**c_args)
    
    def nvl_page(layout):
        global nvl_layout
        nvl_layout = layout
        set_padding(nvl_layouts[nvl_layout].paddings)
        
        renpy.show('ui bg '+nvl_layout)
        
        renpy.call('nvl_clear') #duh

init python:
    def illustration(name, zoom):
        image = 'letter{} {}'.format(current_letter, name)
        trans = [
            t_zoom(zoom),
            t_xy_align(*nvl_layouts[nvl_layout].imgpos),
        ]
        renpy.show(image, at_list=trans)

transform t_zoom(zoom):
    zoom zoom

transform t_xy_align(x, y):
    xalign x yalign y

screen display_note(title, text):
    modal True
    tag note
    frame:
        xalign 0.5 yalign 0.5
        has vbox
        hbox:
            spacing 10
            textbutton "x" action Return()
            text title color '#fff'
        text text color '#fff'

# hyperlinks
init python:
    style.hyperlink_text = Style(style.say_dialogue)
    style.hyperlink_text.hover_underline = True
