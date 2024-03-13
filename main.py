import pgzrun
WIDTH=900
HEIGHT=650
title_box=Rect(0,0,900,80)
question_box=Rect(15,110,650,140)
answer_box1=Rect(15,270,315,115)
answer_box2=Rect(345,270,315,115)
def draw ():
    screen.fill ("blue")
    screen.draw.filled_rect(title_box,"violet")
    screen.draw.filled_rect(question_box,"violet")
    screen.draw.filled_rect(answer_box1,"violet")
    screen.draw.filled_rect(answer_box2,"violet")
pgzrun.go()
#finish answer boxes or make level 2 for cat and fish game