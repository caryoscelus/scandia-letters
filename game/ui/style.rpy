define narrator = Character(None, kind=nvl)

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
