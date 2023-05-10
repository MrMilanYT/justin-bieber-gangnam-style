def on_forever():
    basic.show_string("ME")
    basic.show_leds("""
            . # . # .
                    # # # # #
                    # # # # #
                    . # # # .
                    . . # . .
        """)
    basic.show_string("U")
    music.play_melody("A B C D E F G - ", 120)
basic.forever(on_forever)

