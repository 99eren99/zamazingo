import helper

#-1 reward for all transitions except terminal state
#+1 reward for transitions to terminal state
#{ <state> : { <next state> : <reward> } , <state> : { <next state> : <reward> , <next state> : <reward> }}
stateTransitionRewards={
    0:{5:-1},
    1:{2:-1},
    2:{1:-1,3:-1},
    3:{2:-1,4:-1,8:-1},
    4:{3:-1,9:-1},
    5:{0:-1,6:-1},
    6:{5:-1,7:-1},
    7:{6:-1,8:-1},
    8:{3:-1,7:-1},
    9:{4:-1,14:-1},
    10:{11:-1,15:-1},
    11:{10:-1,12:-1},
    12:{11:-1,13:-1,17:-1},
    13:{12:-1},
    14:{9:-1,19:-1},
    15:{10:-1,20:-1},
    16:{21:-1},
    17:{12:-1,18:-1},
    18:{17:-1,19:-1},
    19:{14:-1,18:-1},
    20:{15:-1,25:-1},
    21:{16:-1,22:-1},
    22:{21:-1,23:-1,27:-1},
    23:{22:-1,28:-1},
    25:{20:-1,26:-1},
    26:{25:-1,27:-1},
    27:{22:-1,26:-1},
    28:{23:-1,29:-1},
    29:{24:1,28:-1}
}

#{ <state> : <state value> , <state> : <state value> }
stateValues={
    0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0,24:0,25:0,
    26:0,27:0,28:0,29:0
}

#policy format:{ <state> : {<next state>:<transition probability>, <next state>:<transition probability>},
#                <state> : {<next state>:<transition probability>, <next state>:<transition probability>}}
policy=helper.getRandomPolicy(stateTransitionRewards)

helper.valueIteration(stateValues,stateTransitionRewards,policy)
