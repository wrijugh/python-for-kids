from turtle import * 

speed(12)
color("red", "yellow")
begin_fill()

for i in range(18):
    right(20)

    for j in range(2):
        forward(200)
        right(90)
        forward(100)
        right(90)

end_fill()
done()