from levels import levels
from playground import window,canvas,createLevel,players,walls,keys,doors,exits
currentLevel=0
createLevel(levels[currentLevel])
def playerMove(event):
    global currentLevel
    player=players[0]
    key=event.keysym
    x=0
    y=0
    if key=='Up':
        y=-5
    elif key=='Left':
        x=-5
    elif key=='Down':
        y=5
    elif key=='Right':
        x=5
    canvas.move(player,x,y)
    for wall in walls:
        x1,y1,x2,y2=canvas.coords(wall)
        if player in canvas.find_overlapping(x1,y1,x2,y2):
            canvas.move(player,-x,-y)
    for key in keys:
        x1,y1,x2,y2=canvas.coords(key)
        if player in canvas.find_overlapping(x1,y1,x2,y2):
            canvas.delete(key)
            keys.remove(key)
            if len(keys)==0:
                for door in doors:
                    canvas.itemconfig(door,fill="green",outline="green")
    for door in doors:
        x1,y1,x2,y2=canvas.coords(door)
        if player in canvas.find_overlapping(x1,y1,x2,y2):
            if canvas.itemcget(door,'fill')=='red':
                canvas.move(player,-x,-y)
    for exit in exits:
        x1,y1,x2,y2=canvas.coords(exit)
        if player in canvas.find_overlapping(x1,y1,x2,y2):
            canvas.delete('all')
            currentLevel+=1
            if currentLevel<len(levels):
                createLevel(levels[currentLevel])
            else:
                messagebox.showinfo('YOU WON THE GAME')
canvas.bind_all('<Key>',playerMove)
window.mainloop()
