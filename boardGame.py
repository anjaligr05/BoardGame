import sys

board_beg=[]
board_value=[]
player=''
opponent=''
player_score=0

opponent_score=0

task=0
cutoff_depth=0
end=False
global next_state_output
#next_state_output=open("next_state.txt","w")
global traverse_output
#next_state_output=open("next_state.txt","w")
#traverse_output=open("traverse_log.txt","w")
directions=[(0,1),(1,0),(-1,0),(0,-1)]

rows = [1, 2, 3, 4, 5]
columns = ['A','B','C','D','E']
def readfile(filename):
    global board_beg
    f = open( filename)
    global task
    task = int (f.readline().rstrip('\n')) 
    
    
    if(task!=4):
        global next_state_output
        next_state_output=open("next_state.txt","w")
        global player
        global opponent
        player =  (f.readline().rstrip('\r\n'))
        if player == 'O':
            opponent= 'X'
        else:
            opponent = 'O'
        #print "Player is", player
        global cutoff_depth
        cutoff_depth = int(f.readline().rstrip('\r\n'))
        
        global traverse_output
        if(task!=1):
            traverse_output=open("traverse_log.txt",'w')
            traverse_output.write("Node,Depth,Value")
        if task==3:
            traverse_output.write(",Alpha,Beta")
        
    
    if(task==4):
       global first_player
       global fp_algo
       global second_player
       global sp_algo
       player=(f.readline().rstrip('\r\n'))
       fp_algo=(f.readline().rstrip('\n'))
       fp_depth=(f.readline().rstrip('\n'))
       opponent=(f.readline().rstrip('\r\n'))
       sp_algo=(f.readline().rstrip('\n'))
       sp_depth=(f.readline().rstrip('\n'))
       
       global trace_state
       trace_state=open("trace_state.txt","w")
       
    global board_value, board_value1
    board_value1=[]
    board_value=[]
    n1=0    
    global player_score
    global opponent_score
    while n1<= 4:
         board_value1.append(list(f.readline().split()))
         n1 += 1
    n=0    
    board_value= [map(int, x) for x in board_value1]
    #print "Board values " , board_value
    while n <= 4:
         board_beg.append(list(f.readline().rstrip().replace('\r','')))
         n += 1
    #print "Board intial state ", board_beg
    if task!=4:
        for a in range(5):
            for b in range(5):
                if board_beg[a][b].strip()==player.strip():
                    player_score+=board_value[a][b]
                if board_beg[a][b].strip()==opponent.strip():
                    opponent_score+=board_value[a][b]
    if task==4:
        for a in range(5):
            for b in range(5):
                if board_beg[a][b].strip()==player:
                    player_score+=board_value[a][b]
                if board_beg[a][b].strip()==opponent:
                    opponent_score+=board_value[a][b]
    #print "player_score", player_score
    if(task!=4):
        return (task,cutoff_depth)
    if(task==4):
        return (task,player,fp_algo,fp_depth,opponent,sp_algo,sp_depth,trace_state)
    
#print "outside" ,player_score
    
def greedy_search(localplayer):
    #print"In greedy"
    max_value=-10000000000
    flag=0;
    res=()
    Result=()
    row1=-1
    col1=-1
    #print board_beg
    row=0
    while row<=4:
        col=0
        while col<=4:
            if board_beg[row][col]=='*':
               Result= evaluation(localplayer,row,col)
               #print "* eva", Result
               temp=Result[0]-max_value
               if temp>0:
                  max_value=Result[0];
                  row1=row;
                  col1=col;
                  flag=1;
                  res=Result;
            else:
                pass
            col=col+1
            #print "bfs",Result
        row=row+1
    if row1==-1 and col1==-1:
        #print "Reached end"
        global end
        end=True;
    #global player_score
    #global opponent_score
    #print "p1",player_score
    #print "p2",opponent_score
    else:
        #print "greedy eval",Result
        make_move(localplayer,row1,col1,Result,board_value)

def play(fp,fp_algo,fp_cutoff,sp,sp_algo,sp_cutoff,trace_state_output):
    #print "fp",fp
    global end
    while end==False:
         next_state(fp,fp_algo,fp_cutoff)
         #print "Returned"
         if end==True:
             return
         print_next_state(trace_state_output)
         next_state(sp,sp_algo,sp_cutoff)
         if end==True:
             return 
         print_next_state(trace_state_output)
         
def next_state(localplayer,task,cutoff):
    task1=int(task)
    cutoff1=int(cutoff)
    if task1==1:
        #print "in task"
        greedy_search(localplayer)
    elif task1==2:
        minmax_search(localplayer,cutoff1)
    elif task1==3:
        alpha_beta_pruning(localplayer,cutoff1)
    
def make_move(localplayer,i,j,result,board_value):
     global board_beg
     global player_score
     global opponent_score
     if localplayer==player :
        player_score=result[1]
        opponent_score=result[2]
     elif localplayer==opponent :
         opponent_score=result[1]
         player_score=result[2]
     board_beg[i][j]=localplayer
     #print "res", res
     
     for item in result[3]:
         a=directions[item][0]
         b=directions[item][1]
         board_beg[i+a][j+b]=localplayer

def evaluation(localplayer,i,j):
     raid_pos_x=[]
     raid_pos_y=[]
     #print board_value
     global player_score
     global opponent_score
     player_score_local=0
     opponent_score_local=0
     if localplayer==player :
        player_score_local=player_score
        opponent_score_local=opponent_score
     elif localplayer==opponent :
        player_score_local=opponent_score
        opponent_score_local=player_score
     player_score_local=player_score_local+board_value[i][j]
     #print "in evalfucntion",player_score
     if possible_raid_pos(localplayer,i,j):
        #print "pos_i",i,"pos_j",j
        #print board_beg
        for a in range(4):
            #opponent(localplayer,pos_i,pos_j)
            #resultFlag=valid(localplayer,pos_i,pos_j)
            x=i+directions[a][0]
            y=j+directions[a][1]
            if (x>=0 and x<5 and y>=0 and y<5 and board_beg[x][y]!="*" and board_beg[x][y]!=localplayer):
               #print "entered"
               player_score_local=player_score_local+board_value[x][y]
               opponent_score_local=opponent_score_local-board_value[x][y]
               raid_pos_x.append(a)
               raid_pos_y.append(i)
     fn=player_score_local-opponent_score_local
     #print "eva", eva
     return (fn,player_score_local,opponent_score_local,raid_pos_x)

def possible_raid_pos(localplayer,i,j):
    if((i-1>=0 and board_beg[i-1][j]==localplayer) or(i+1<5 and board_beg[i+1][j]==localplayer)or(j-1>=0 and board_beg[i][j-1]==localplayer)or(j+1<5 and board_beg[i][j+1]==localplayer) ):
        return True
    else:
        return False
    
def minmax_search(localplayer,cutoff):
    depth=0
    prune=False
    minus_inf=float('-inf')
    plus_inf=float('inf')
    result=max_value(localplayer,cutoff,depth,'root',prune,minus_inf,plus_inf,board_value)
    if result[1]==-1 and result[2]==-1:
            global end
            end=True
    else:
        res=evaluation(localplayer,result[1],result[2])
        #print "eva=",res
        make_move(localplayer,result[1],result[2],res,board_value) 

def max_value(localplayer,cutoff,depth,curpos,prune,a,b,board_value):
    global board_beg
    global player_score
    global opponent_score
    global traverse_output
    #print "cutoff", cutoff
    #print "depth", depth
   
    if depth==cutoff:
        if localplayer==player :
           print_traverse_log(curpos,depth,player_score-opponent_score,a,b)
           #if task in [2,3]:
           #   traverse_output.write("\n"+str(curpos)+","+str(depth)+","+printInf(str(v)))
           #if task==3:
           #   traverse_output.write(","+printInf(str(a))+","+printInf(str(b)))
           return (player_score-opponent_score,-1,-1)
        else:
           print_traverse_log(curpos,depth,opponent_score-player_score,a,b)
           #if task in [2,3]:
           #   traverse_output.write("\n"+str(curpos)+","+str(depth)+","+printInf(str(v)))
           #if task==3:
           #   traverse_output.write(","+printInf(str(a))+","+printInf(str(b)))
           return (opponent_score-player_score,-1,-1)
    i=-1
    j=-1
    v=float('-inf')
    #print board_beg
    for row in range(5):
        for col in range(5):
            #print "pos_i",row,"pos_j",col
            
            if board_beg[row][col]=='*':
               #print "*",row, col
               #print "pos_i",row,"pos_j",col
               tempstate=[line[:] for line in board_beg]
               tempplayer=player_score
               tempopponent=opponent_score
               print_traverse_log(curpos,depth,v,a,b)
               #if task in [2,3]:
               #   traverse_output.write("\n"+str(curpos)+","+str(depth)+","+printInf(str(v)))
               #if task==3:
               #   traverse_output.write(","+printInf(str(a))+","+printInf(str(b)))
               make_move(localplayer,row,col,evaluation(localplayer,row,col),board_value)
               cur=min_value(opponent_player(localplayer),cutoff,depth+1,pos(row,col),prune,a,b)
               temp=cur[0]-v
               if temp>0:
                   v=cur[0];
                   i=row;
                   j=col; 
               board_beg=tempstate
               player_score=tempplayer
               opponent_score=tempopponent
               if prune:
                  temp2=v-b  
                  if temp2>=0:
                     print_traverse_log(curpos,depth,v,a,b)
                     return (v,i,j)
                  if(a>v):
                      a=a
                  else:
                      a=v
    if i==-1 and j==-1:
        if localplayer==player :
           print_traverse_log(curpos,depth,player_score-opponent_score,a,b)	
           #if task in [2,3]:
           #   traverse_output.write("\n"+str(curpos)+","+str(depth)+","+printInf(str(v)))
           #if task==3:
           #   traverse_output.write(","+printInf(str(a))+","+printInf(str(b)))
           return (player_score-opponent_score,-1,-1)
        else:
            print_traverse_log(curpos,depth,opponent_score-player_score,a,b)
            return (opponent_score-player_score,-1,-1)
    if True:
        print_traverse_log(curpos,depth,v,a,b)   
    else:
        pass
    return (v,i,j)
    
def min_value(localplayer,cutoff,depth,curpos,prune,a,b):
    global board_beg
    global player_score
    global opponent_score
    
    if depth==cutoff:
        if localplayer==opponent:
            print_traverse_log(curpos,depth,player_score-opponent_score,a,b)
            #if task in [2,3]:
            #  traverse_output.write("\n"+str(curpos)+","+str(depth)+","+printInf(str(v)))
            #if task==3:
            #  traverse_output.write(","+printInf(str(a))+","+printInf(str(b)))
            return (player_score-opponent_score,-1,-1)
        else:
            print_traverse_log(curpos,depth,-player_score+opponent_score,a,b)
            #if task in [2,3]:
            #  traverse_output.write("\n"+str(curpos)+","+str(depth)+","+printInf(str(v)))
            #if task==3:
            #  traverse_output.write(","+printInf(str(a))+","+printInf(str(b)))
            return (opponent_score-player_score,-1,-1)
    v=float('inf')
    i=-1
    j=-1
    for row in range(5):
        for col in range(5):
            if board_beg[row][col]=='*':
               tempstate=[r[:] for r in board_beg]
               tempplayer=player_score
               tempopponent=opponent_score
               print_traverse_log(curpos,depth,v,a,b)
               #if task in [2,3]:
               #   traverse_output.write("\n"+str(curpos)+","+str(depth)+","+printInf(str(v)))
               #if task==3:
               #traverse_output.write(","+printInf(str(a))+","+printInf(str(b)))
               make_move(localplayer,row,col,evaluation(localplayer,row,col),board_value)
               cur=max_value(opponent_player(localplayer),cutoff,depth+1,pos(row,col),prune,a,b,board_value)
               temp=cur[0]-v
               if temp<0:
                  v=cur[0];
                  i=row;
                  j=col;
               board_beg=tempstate
               player_score=tempplayer
               opponent_score=tempopponent 
               
               if prune:
                  temp2=v-a               
                  if temp2<=0 :
                     print_traverse_log(curpos,depth,v,a,b)
                     return (v,i,j)
                  if (b<v):
                      b=b
                  else:
                      b=v
                  
    if i==-1 and j==-1:
        if localplayer==opponent:
            print_traverse_log(curpos,depth,player_score-opponent_score,a,b)
            #if task in [2,3]:
            #  traverse_output.write("\n"+str(curpos)+","+str(depth)+","+printInf(str(v)))
            #if task==3:
            #  traverse_output.write(","+printInf(str(a))+","+printInf(str(b)))
            return (player_score-opponent_score,-1,-1)
        else:
            print_traverse_log(curpos,depth,-player_score+opponent_score,a,b)
            #if task in [2,3]:
            #  traverse_output.write("\n"+str(curpos)+","+str(depth)+","+printInf(str(v)))
            #if task==3:
            #  traverse_output.write(","+printInf(str(a))+","+printInf(str(b)))
            return (opponent_score-player_score,-1,-1)
    if True:
        print_traverse_log(curpos,depth,v,a,b)   
    else:
        pass
    #print_traverse_log(curpos,depth,v,a,b)
    #if task in [2,3]:
    #   traverse_output.write("\n"+str(curpos)+","+str(depth)+","+printInf(str(v)))
    #if task==3:
    #  traverse_output.write(","+printInf(str(a))+","+printInf(str(b)))
    return (v,i,j)
    
def opponent_player(localplayer):
    if localplayer==player:
        return opponent
    elif localplayer==opponent:
        return player
    
def alpha_beta_pruning(localplayer,cutoff):
    prune=True
    minus_inf=float('-inf')
    plus_inf=float('inf')
    result=max_value(localplayer,cutoff,0,'root',prune,minus_inf,plus_inf,board_value)
    if result[1]==-1 and  result[2]==-1:
            global end
            end=True
    else: make_move(localplayer,result[1],result[2],evaluation(localplayer,result[1],result[2]),board_value)
    
def print_next_state(output):
    #global next_state_output
    #i=0
    #next_state_str=str()
    '''while(i<len(board_beg)):
	    line=str(board_beg[i]).replace('[','')
	    line=line.replace(']','')
	    line=line.replace(',','')
	    line=line.replace("\'",'')
	    line=line.replace("",'')
	    next_state_str=line+'\n'
	    i=i+1
    #next_state_str=next_state_str.rstrip('\n')'''
    #string=["".join(item) for item in board_beg]
    #print [item [:] for item in board_beg]
    output.write( "\r\n".join(["".join(item) for item in board_beg]))
    output.write("\n")
    
def pos(i,j):
    return chr(ord('A')+j)+str(i+1)

def print_traverse_log(curpos,depth,v,a,b):
    global traverse_output
    if task in [2,3]:
       traverse_output.write("\n"+str(curpos)+","+str(depth)+","+printInf(str(v)))
    if task==3:
       traverse_output.write(","+printInf(str(a))+","+printInf(str(b)))
def printInf(s):
    global traverse_output
    if  s=="inf" :return "Infinity"
    elif s=="-inf":return "-Infinity"
    return s
    
    
#tuple_in_dir = lambda tuple1, direction: (tuple1[0]+direction[0], tuple1[1]+direction[1])
#tuple_valid = lambda tuple1: (tuple1[0] >= 0 and tuple1[0] < 5 and tuple1[1] >= 0 and tuple1[1] < 5)

task1=0
def main(inputFile):
    task=readfile(inputFile)
    global traverse_state_output
    global next_state_output
    #print task
    #print "first player",player
    if task[0]!=4:
        next_state(player,task[0],task[1])
        #print "ended"
        print_next_state(next_state_output)
	if task[0]!=1:next_state_output.truncate(next_state_output.tell()-1)
    else:
        #print "here"
        play(task[1],task[2],task[3],task[4],task[5],task[6],task[7])
        
        #task[7].truncate(task[7].tell()-1)
    #task1=task[2]
    #print "Depth", depth
    #print "Task" , task[2]
    #print "Board", board_beg
    #if task[2]==1:
    #    greedy_search(player)
    #elif task[2]==2:
    #    minmax_search(player,depth)
    #global next_state_output
    #for item in board_beg:
    #    next_state_output.write("".join(item) + "\n")
if __name__=='__main__':
	main(sys.argv[2])
