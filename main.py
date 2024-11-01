# This function defines when the player sprite overlaps with a projectile sprite which is the food icons coming from the sides
def on_on_overlap(sprite, otherSprite):
    # Decreases the player's life by 1
    info.change_life_by(-1)
    # Shakes the screen of the game to indicate the impact of the player with an enemy food icon
    scene.camera_shake(4, 500)
    # Destroys the projectile sprite with a fire effect
    otherSprite.destroy(effects.fire)
    # Plays a sound effect to accompany the collision 
    music.pew_pew.play()
    
# Registers the on overlap function to trigger when the player bumps into or overlaps with the projectile    
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)

# This function defines when the player sprite overlaps with the strawberry food sprite 
def on_on_overlap2(sprite2, otherSprite2):
    # Increases the player's score by 1 point 
    info.change_score_by(1)
    # Destroys the strawberry food spire
    otherSprite2.destroy()
    # Creates a heart bubble effect on the player sprite for 100ms when they hit the strawberry food sprite
    sprite2.start_effect(effects.hearts, 100)
    # Plays a sound effect to signal that the strawberry food was collected
    music.ba_ding.play()

# Registers the overlap function to trigger when the player sprite overlaps and hit the strawberry food icon
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap2)

# Intialises the variables
projectile: Sprite = None
choice = 0

# Starts a heart effect on the screen for 1000ms at the start of the game
effects.hearts.start_screen_effect(1000)

# Sets the background colour to pink to add a fun, vibrant effect in the game 
scene.set_background_color(3)

# Creates the player sprite with a specific image of the player and assigns it to the player
# Added in some colour differences to the already set player to make it more personalised with the game
mySprite = sprites.create(img("""
        . . . . . . f f f f . . . . . . 
            . . . . f f f a a f f f . . . . 
            . . . f f f a a a a f f f . . . 
            . . f f f e e e e e e f f f . . 
            . . f f e c c c c c c e e f . . 
            . . f e c f f f f f f c e f . . 
            . . f f f f e e e e f f f f . . 
            . f f e f b f 4 4 f b f e f f . 
            . f e e 4 1 f d d f 1 4 e e f . 
            . . f e e d d d d d d e e f . . 
            . . . f e e 4 4 4 4 e e f . . . 
            . . e 4 f a a a a a a f 4 e . . 
            . . 4 d f a a a a a a f d 4 . . 
            . . 4 4 f 4 4 b b 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)

# Allows the player to be controlled with the arrow buttons and the controller on the screen
# Added in that the player has a speed of 100 
controller.move_sprite(mySprite, 100, 100)

# Ensures that the player sprite stays within the screen boundaries 
mySprite.set_stay_in_screen(True)

# Sets the player's starting life count to 3
info.set_life(3)

# Sets the game over screen effect at the end of the game to be a melting effect 

# Plays background music in a loop until finished
# Personalised the music to suit the game style 
game.set_game_over_effect(True, effects.melt)
music.play(music.string_playable("G B A F C5 B A C5 ", 200),
    music.PlaybackMode.UNTIL_DONE)

# This function ensures that the projectiles appear from the sides of the screen at regular intervals
def on_update_interval():
    global choice, projectile

    # Randomly selects a projectile type (1,2 or 3)
    choice = randint(1, 3)
    if choice == 1:
        # Creates a projectile sprite from the left side of the screen that moves across to the right at a speed of -60
        projectile = sprites.create_projectile_from_side(img("""
                . . . . . . . . . . b b b . . . 
                            . . . . . . . . b e e 3 3 b . . 
                            . . . . . . b b e 3 2 e 3 a . . 
                            . . . . b b 3 3 e 2 2 e 3 3 a . 
                            . . b b 3 3 3 3 3 e e 3 3 3 a . 
                            b b 3 3 3 3 3 3 3 3 3 3 3 3 3 a 
                            b 3 3 3 d d d d 3 3 3 3 3 d d 3 
                            b b b b b b b 3 d d d d d d 3 a 
                            b d 5 5 5 5 d b b b a a a a a a 
                            b 3 d d 5 5 5 5 5 5 5 d d d d a 
                            b 3 3 3 3 3 3 d 5 5 5 d d d d a 
                            b 3 d 5 5 5 3 3 3 3 3 3 b b b a 
                            b b b 3 d 5 5 5 5 5 5 5 d d b a 
                            . . . b b b 3 d 5 5 5 5 d d 3 a 
                            . . . . . . b b b b 3 d d d b a 
                            . . . . . . . . . . b b b a a .
            """),
            -60,
            0)
    elif choice == 2:
        # This creates a different projectile sprite that comes from the right side moving to the left at a speed of 60
        projectile = sprites.create_projectile_from_side(img("""
                . . . . . . b b b b a a . . . . 
                            . . . . b b d d d 3 3 3 a a . . 
                            . . . b d d d 3 3 3 3 3 3 a a . 
                            . . b d d 3 3 3 3 3 3 3 3 3 a . 
                            . b 3 d 3 3 3 3 3 b 3 3 3 3 a b 
                            . b 3 3 3 3 3 a a 3 3 3 3 3 a b 
                            b 3 3 3 3 3 a a 3 3 3 3 d a 4 b 
                            b 3 3 3 3 b a 3 3 3 3 3 d a 4 b 
                            b 3 3 3 3 3 3 3 3 3 3 d a 4 4 e 
                            a 3 3 3 3 3 3 3 3 3 d a 4 4 4 e 
                            a 3 3 3 3 3 3 3 d d a 4 4 4 e . 
                            a a 3 3 3 d d d a a 4 4 4 e e . 
                            . e a a a a a a 4 4 4 4 e e . . 
                            . . e e b b 4 4 4 4 b e e . . . 
                            . . . e e e e e e e e . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            60,
            0)
    else:
        # Creates a food sprite from the side and sets it kind to 'food' which is the strawberry icon
        projectile = sprites.create_projectile_from_side(img("""
                . . . . . . . . . . . 6 6 6 6 6 
                            . . . . . . . . . 6 6 7 7 7 7 8 
                            . . . . . . 8 8 8 7 7 8 8 6 8 8 
                            . . e e e e c 6 6 8 8 . 8 7 8 . 
                            . e 2 5 4 2 e c 8 . . . 6 7 8 . 
                            e 2 4 2 2 2 2 2 c . . . 6 7 8 . 
                            e 2 2 2 2 2 2 2 c . . . 8 6 8 . 
                            e 2 e e 2 2 2 2 e e e e c 6 8 . 
                            c 2 e e 2 2 2 2 e 2 5 4 2 c 8 . 
                            . c 2 e e e 2 e 2 4 2 2 2 2 c . 
                            . . c 2 2 2 e e 2 2 2 2 2 2 2 e 
                            . . . e c c e c 2 2 2 2 2 2 2 e 
                            . . . . . . . c 2 e e 2 2 e 2 c 
                            . . . . . . . c e e e e e e 2 c 
                            . . . . . . . . c e 2 2 2 2 c . 
                            . . . . . . . . . c c c c c . .
            """),
            55,
            0)
        # Changes the kind of the sprite to food
        projectile.set_kind(SpriteKind.food)
    projectile.y = randint(10, 110)

# Calls the function at a regular interval of 500ms to create new projectiles or food
game.on_update_interval(500, on_update_interval)
