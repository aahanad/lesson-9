import pgzrun
WIDTH=900
HEIGHT=550
title_box=Rect(0,0,900,80)
question_box=Rect(15,110,650,140)
answer_box1=Rect(15,270,315,115)
answer_box2=Rect(345,270,315,115)
answer_box3=Rect(15,405,315,115)
answer_box4=Rect(345,405,315,115)
skip=Rect(705,110,155,115)
reset=Rect(705,250,155,115)
timer=Rect(705,390,155,115)
score=0
time_left=5
question_file_name="questions.txt"
title=""
game_over=False
questions=[]
question_count=0
question_index=0
question=[]
def draw ():
    screen.fill ("blue")
    screen.draw.filled_rect(title_box,"violet")
    screen.draw.filled_rect(question_box,"violet")
    screen.draw.filled_rect(answer_box1,"violet")
    screen.draw.filled_rect(answer_box2,"violet")
    screen.draw.filled_rect(answer_box3,"violet")
    screen.draw.filled_rect(answer_box4,"violet")
    screen.draw.filled_rect(skip,"violet")
    screen.draw.filled_rect(reset,"violet")
    screen.draw.filled_rect(timer,"violet")
    title="WELCOME TO QUIZ MASTER..."+f"Q: {question_index} of {question_count}"
    screen.draw.textbox(title,title_box,color="black")
    screen.draw.textbox("skip",skip,color="black")
    screen.draw.textbox("reset",reset,color="black")
    screen.draw.textbox(str(time_left),timer,color="black")
def update():
    title_box.x-=2
    if title_box.right<0:
        title_box.left=900
def gameover():
    global time_left,game_over,question
    message=f"Game over!\n You got {score} questions correct!"
    time_left=0
    game_over=True
    question=[message,"-","-","-","-",5]
def updatetime():
    global time_left
    if time_left:
        time_left=time_left-1
    else:
        gameover()
clock.schedule_interval(updatetime,1)
pgzrun.go()
