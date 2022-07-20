input.onButtonPressed(Button.A, function () {
    music.startMelody(music.builtInMelody(Melodies.PowerUp), MelodyOptions.Once)
    basic.showString("INICIO")
    basic.pause(500)
    music.startMelody(music.builtInMelody(Melodies.BaDing), MelodyOptions.Once)
    basic.showString("REMOJAR")
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        # # # # #
        `)
    basic.pause(500)
    music.playTone(175, music.beat(BeatFraction.Whole))
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        # # # # #
        # # # # #
        `)
    basic.pause(500)
    music.playTone(262, music.beat(BeatFraction.Whole))
    basic.showLeds(`
        . . . . .
        . . . . .
        # # # # #
        # # # # #
        # # # # #
        `)
    basic.pause(500)
    music.playTone(262, music.beat(BeatFraction.Whole))
    basic.showLeds(`
        . . . . .
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
    basic.pause(500)
    music.playTone(262, music.beat(BeatFraction.Whole))
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
    basic.pause(500)
    basic.clearScreen()
    music.startMelody(music.builtInMelody(Melodies.BaDing), MelodyOptions.Once)
    basic.showString("LAVAR")
    for (let index = 0; index < 4; index++) {
        basic.showArrow(ArrowNames.South)
        basic.showIcon(IconNames.TShirt)
    }
    for (let index = 0; index < 10; index++) {
        basic.showLeds(`
            . # . . #
            . . # . .
            # . . # .
            . . . . .
            . # . . #
            `)
        basic.showLeds(`
            . . . # .
            # . # . .
            . # . . #
            . . . . .
            # . . # .
            `)
        basic.showLeds(`
            . . # . .
            # . . . .
            . # . . #
            . . # . .
            # . . # .
            `)
        basic.showLeds(`
            # . . # .
            . . . . #
            . . . # .
            . . # . .
            # . . . #
            `)
    }
    basic.clearScreen()
    music.startMelody(music.builtInMelody(Melodies.BaDing), MelodyOptions.Once)
    basic.showString("ENJUAGAR")
    for (let index = 0; index < 8; index++) {
        basic.showLeds(`
            # . # . #
            . # . # .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            # . # . #
            . # . # .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . # . # .
            . . . . .
            # . # . #
            . # . # .
            . . . . .
            `)
        basic.showLeds(`
            # . # . #
            . # . # .
            . . . . .
            # . # . #
            . # . # .
            `)
    }
    for (let index = 0; index < 4; index++) {
        basic.clearScreen()
        basic.showLeds(`
            . # . . #
            . . . . .
            # . . # .
            . . . . .
            . # . . #
            `)
        basic.showLeds(`
            . . . # .
            # . # . .
            . # . . #
            . . . . .
            # . . # .
            `)
        basic.showLeds(`
            . . # . .
            # . . . .
            . # . . #
            . . # . .
            # . . # .
            `)
        basic.showLeds(`
            # . . # .
            . . . . #
            . . . # .
            . . # . .
            # . . . #
            `)
    }
    basic.clearScreen()
    music.startMelody(music.builtInMelody(Melodies.BaDing), MelodyOptions.Once)
    basic.showString("SECAR")
    for (let index = 0; index < 4; index++) {
        basic.showLeds(`
            . # # # .
            # . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            # . . . .
            # . . . .
            # . . . .
            . # . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . #
            . # # # .
            `)
        basic.showLeds(`
            . . . # .
            . . . . #
            . . . . #
            . . . . #
            . . . . .
            `)
        basic.showLeds(`
            . . # # .
            . # . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . # . . .
            . # . . .
            . . # . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . # .
            . . . . .
            . . # # .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            # # . # .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            # . . . .
            # . . . .
            # . . . .
            . # . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . #
            . # # # .
            `)
        basic.showLeds(`
            . . . # .
            . . . . #
            . . . . #
            . . . . #
            . . . . .
            `)
    }
    basic.clearScreen()
    basic.pause(500)
    for (let index = 0; index < 4; index++) {
        basic.showArrow(ArrowNames.North)
        basic.showIcon(IconNames.TShirt)
    }
})
input.onButtonPressed(Button.B, function () {
    music.startMelody(music.builtInMelody(Melodies.PowerDown), MelodyOptions.Once)
    basic.showString("END!")
})
music.setVolume(50)
