screen main_menu():
    tag menu
    imagemap:
        ground Solid('#fff')
        idle 'images/ui/cover-envelope-normal.png'
        hover 'images/ui/cover-envelope-broken.png'
        alpha True
        hotspot (0, 0, 1280, 720):
            action Start()
    
    hbox:
        yalign 0.95
        xalign 0.5
        spacing 50
        textbutton _("Загрузить") action ShowMenu("load")
        textbutton _("Настройки") action ShowMenu("preferences")
        #textbutton _("Помощь") action Help()
        textbutton _("Выход") action Quit(confirm=False)
