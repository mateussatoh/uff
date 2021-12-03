from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *


window = Window(640,480)
window.set_title("Pong!")

background = GameImage('./img/hobbit-town.jpg')

keyboard = Window.get_keyboard()

topPad = Sprite('./img/wodden-pad.png', 1)
topPad.x = background.width / 2 - topPad.width / 2
topPad.y = 0

bottomPad = Sprite('./img/wodden-pad.png', 1)
bottomPad.x = background.width / 2 - bottomPad.width / 2
bottomPad.y = background.height - bottomPad.height

ball = Sprite('./img/ring.png', 1)
ball.x = background.width / 2 - ball.width / 2
ball.y = background.height / 2 - ball.height / 2

ballVelocityX = 200
ballVelocityY = 300
paddingVelocity = 180

scoreBottom = 0
scoreTop = 0
bounce = 0 

while True:
    if keyboard.key_pressed("RIGHT") and bottomPad.x < window.width - bottomPad.width:
        bottomPad.x = bottomPad.x + paddingVelocity * window.delta_time()
    if keyboard.key_pressed("LEFT") and bottomPad.x > 0:
        bottomPad.x = bottomPad.x - paddingVelocity * window.delta_time()

    if (topPad.x + topPad.width / 2) < (ball.x + ball.width / 2):
        topPad.x = topPad.x + paddingVelocity * window.delta_time()
    if (topPad.x + topPad.width / 2) > (ball.x + ball.width / 2):
        topPad.x = topPad.x - paddingVelocity * window.delta_time()

    if (ball.x >= (background.width - ball.width)):
        ballVelocityX = - abs(ballVelocityX) 
    if (ball.x <= 0):
        ballVelocityX = abs(ballVelocityX) 

    ball.x = ball.x + ballVelocityX * window.delta_time()

    if (ball.y >= (background.height - ball.height)):
        bounce = 0
        scoreBottom += 1
        ballVelocityY = - abs(ballVelocityY)
        ball.y = window.height / 2
        ball.x = window.width / 2

    if (ball.y <= 0):
        bounce = 0
        scoreTop += 1
        ballVelocityY = abs(ballVelocityY)
        ball.y = window.height / 2
        ball.x = window.width / 2

    ball.y = ball.y + ballVelocityY * window.delta_time()

    if ball.collided(bottomPad):
        ballVelocityY = - abs(ballVelocityX) 
        bounce += 1
    if ball.collided(topPad):
        ballVelocityY = abs(ballVelocityX) 
        bounce += 1

    if (bounce == 4):
        bottomPad = Sprite('./img/wodden-pad-small.png', 1)
        bottomPad.x = background.width / 2 - bottomPad.width / 2
        bottomPad.y = background.height - bottomPad.height

    background.draw()
    window.draw_text(f"{scoreBottom}", 20, 30, 30, (0, 0, 0))
    window.draw_text(f"{scoreTop}", 20, window.height - 60, 30)
    ball.draw()
    bottomPad.draw()
    topPad.draw()
    window.update()
