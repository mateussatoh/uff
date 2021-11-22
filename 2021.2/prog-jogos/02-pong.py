from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

window = Window(640,480)
window.set_title("Pong!")

background = GameImage('./img/hobbit-town.jpg')

ball = Sprite('./img/ring.png', 1)
ball.x = background.width / 2 - ball.width / 2
ball.y = background.height / 2 - ball.height / 2

ballVelocityX = 0.3
ballVelocityY = 0.3

while True:
    if (ball.x >= (background.width - ball.width) or ball.x <= 0):
        ballVelocityX = ballVelocityX * -1
    if (ball.y >= (background.height - ball.height) or ball.y <= 0):
        ballVelocityY = ballVelocityY * -1

    ball.x = ball.x + ballVelocityX
    ball.y = ball.y + ballVelocityY

    background.draw()
    ball.draw()
    window.update()
