Bpressed = 0

def on_button_pressed_b():
    global Bpressed
    Bpressed = randint(250, 3000)
    music.play_tone(Note.D,Bpressed)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_a():
    music.play_tone(Note.D,Bpressed)
input.on_button_pressed(Button.A, on_button_pressed_a)

basic.show_icon(IconNames.HEART)



