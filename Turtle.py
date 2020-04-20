import  turtle

tao = turtle.Pen()
tao.shape('turtle')
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.up()
tao.home()
tao.backward(200)
tao.down()

for i in range(4):
    tao.forward(100)
    tao.left(90)

tao.up()
tao.home()
tao.left(90)
tao.down()
tao.forward(100)

for i in range(4):
    tao.forward(100)
    tao.left(90)

tao.reset()

input("EnyPress to exit")

