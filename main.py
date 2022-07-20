def on_button_pressed_a():
    music.start_melody(music.built_in_melody(Melodies.POWER_UP), MelodyOptions.ONCE)
    basic.show_string("INICIO")
    basic.pause(500)
    music.start_melody(music.built_in_melody(Melodies.BA_DING), MelodyOptions.ONCE)
    basic.show_string("REMOJAR")
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                # # # # #
    """)
    basic.pause(500)
    music.play_tone(175, music.beat(BeatFraction.WHOLE))
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                # # # # #
                # # # # #
    """)
    basic.pause(500)
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    basic.show_leds("""
        . . . . .
                . . . . .
                # # # # #
                # # # # #
                # # # # #
    """)
    basic.pause(500)
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    basic.show_leds("""
        . . . . .
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    """)
    basic.pause(500)
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    basic.show_leds("""
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    """)
    basic.pause(500)
    basic.clear_screen()
    music.start_melody(music.built_in_melody(Melodies.BA_DING), MelodyOptions.ONCE)
    basic.show_string("LAVAR")
    for index in range(4):
        basic.show_arrow(ArrowNames.SOUTH)
        basic.show_icon(IconNames.TSHIRT)
    for index2 in range(10):
        basic.show_leds("""
            . # . . #
                        . . # . .
                        # . . # .
                        . . . . .
                        . # . . #
        """)
        basic.show_leds("""
            . . . # .
                        # . # . .
                        . # . . #
                        . . . . .
                        # . . # .
        """)
        basic.show_leds("""
            . . # . .
                        # . . . .
                        . # . . #
                        . . # . .
                        # . . # .
        """)
        basic.show_leds("""
            # . . # .
                        . . . . #
                        . . . # .
                        . . # . .
                        # . . . #
        """)
    basic.clear_screen()
    music.start_melody(music.built_in_melody(Melodies.BA_DING), MelodyOptions.ONCE)
    basic.show_string("ENJUAGAR")
    for index3 in range(8):
        basic.show_leds("""
            # . # . #
                        . # . # .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        # . # . #
                        . # . # .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . # . # .
                        . . . . .
                        # . # . #
                        . # . # .
                        . . . . .
        """)
        basic.show_leds("""
            # . # . #
                        . # . # .
                        . . . . .
                        # . # . #
                        . # . # .
        """)
    for index4 in range(4):
        basic.clear_screen()
        basic.show_leds("""
            . # . . #
                        . . . . .
                        # . . # .
                        . . . . .
                        . # . . #
        """)
        basic.show_leds("""
            . . . # .
                        # . # . .
                        . # . . #
                        . . . . .
                        # . . # .
        """)
        basic.show_leds("""
            . . # . .
                        # . . . .
                        . # . . #
                        . . # . .
                        # . . # .
        """)
        basic.show_leds("""
            # . . # .
                        . . . . #
                        . . . # .
                        . . # . .
                        # . . . #
        """)
    basic.clear_screen()
    music.start_melody(music.built_in_melody(Melodies.BA_DING), MelodyOptions.ONCE)
    basic.show_string("SECAR")
    for index5 in range(4):
        basic.show_leds("""
            . # # # .
                        # . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        # . . . .
                        # . . . .
                        # . . . .
                        . # . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . #
                        . # # # .
        """)
        basic.show_leds("""
            . . . # .
                        . . . . #
                        . . . . #
                        . . . . #
                        . . . . .
        """)
        basic.show_leds("""
            . . # # .
                        . # . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . # . . .
                        . # . . .
                        . . # . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . # .
                        . . . . .
                        . . # # .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        # # . # .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        # . . . .
                        # . . . .
                        # . . . .
                        . # . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . #
                        . # # # .
        """)
        basic.show_leds("""
            . . . # .
                        . . . . #
                        . . . . #
                        . . . . #
                        . . . . .
        """)
    basic.clear_screen()
    basic.pause(500)
    for index6 in range(4):
        basic.show_arrow(ArrowNames.NORTH)
        basic.show_icon(IconNames.TSHIRT)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    music.start_melody(music.built_in_melody(Melodies.POWER_DOWN),
        MelodyOptions.ONCE)
    basic.show_string("END!")
input.on_button_pressed(Button.B, on_button_pressed_b)

music.set_volume(50)