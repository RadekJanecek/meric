let Bpressed = 0
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    Bpressed = randint(250, 3000)
    music.playTone(Note.D, Bpressed)
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    music.playTone(Note.D, Bpressed)
})
basic.showIcon(IconNames.Heart)
