basic.forever(function on_forever() {
    basic.showString("ME")
    basic.showLeds(`
            . # . # .
                    # # # # #
                    # # # # #
                    . # # # .
                    . . # . .
        `)
    basic.showString("U")
    music.playMelody("A B C D E F G - ", 120)
})
