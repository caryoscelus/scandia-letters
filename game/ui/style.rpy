define narrator = Character(None, kind=nvl)

label nvl_clear:
    nvl clear
    return

init python:
    def set_padding(left, right):
        global narrator
        narrator = Character(kind=nvl, window_left_padding=left, window_right_padding=right)
    
    def nvl_page(left, right):
        set_padding(left, right)
        renpy.call('nvl_clear') #duh
    
    def nvl_page_left():
        renpy.scene()
        renpy.show('ui bg left')
        nvl_page(0, 380)
    
    def nvl_page_right():
        renpy.scene()
        renpy.show('ui bg right')
        nvl_page(380, 0)

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
