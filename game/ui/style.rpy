define narrator = Character(None, kind=nvl, what_color='#111', what_size=20)

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
            text title
        text text
