define narrator = Character(None, kind=nvl)

label nvl_clear:
    nvl clear
    return

init python:
    nvl_layout_order = ['left', 'right']
    nvl_layouts = dict(
        left=[0, 380],
        right=[380, 0],
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
        set_padding(nvl_layouts[nvl_layout])
        
        renpy.scene()
        renpy.show('ui bg '+nvl_layout)
        
        renpy.call('nvl_clear') #duh

transform illustration:
    xalign 0.94
    yalign 0.5

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
