import numpy as np
from tabulate import tabulate
import copy

def printValueMatrix(stateValues):
    maze=[[stateValues[0],stateValues[5],stateValues[10],stateValues[15],stateValues[20],stateValues[25]],
          [stateValues[1],stateValues[6],stateValues[11],stateValues[16],stateValues[21],stateValues[26]],
          [stateValues[2],stateValues[7],stateValues[12],stateValues[17],stateValues[22],stateValues[27]],
          [stateValues[3],stateValues[8],stateValues[13],stateValues[18],stateValues[23],stateValues[28]],
          [stateValues[4],stateValues[9],stateValues[14],stateValues[19],"S+",stateValues[29]]]
    print(tabulate(maze,tablefmt='grid'))

def getRandomPolicy(stateTransitionRewards):
    randomPolicy=copy.deepcopy(stateTransitionRewards)
    for key,value in randomPolicy.items():
        probabilities=np.random.random(len(value))
        probabilities /= probabilities.sum()
        i=0
        for key in value:
            value[key]=probabilities[i]
            i+=1
    return randomPolicy

def oneSweepPolicyEvaluation(stateValues,stateTransitionRewards,policy):
    updatedStateValues=copy.deepcopy(stateValues)

    for state in updatedStateValues:
        if state==24:
            continue
        expectedValue=0
        for action,probability in policy[state].items():
            expectedValue+=probability*(stateValues[action]+stateTransitionRewards[state][action])
        updatedStateValues[state]=expectedValue

    return updatedStateValues

def policyImprovement(stateValues,policy):
    for currentState in policy:
        maxValue=-99
        stateWithMaxValue=-1
        for nextState in policy[currentState]:
            policy[currentState][nextState]=0
            nextValue=stateValues[nextState]
            if nextValue>maxValue:
                maxValue=nextValue
                stateWithMaxValue=nextState
        policy[currentState][stateWithMaxValue]=1   

def valueIteration(stateValues,stateTransitionRewards,policy):
    oldPolicy=copy.deepcopy(policy)
    cooldown=0
    while cooldown<10:
        printValueMatrix(stateValues)
        stateValues=oneSweepPolicyEvaluation(stateValues,stateTransitionRewards,policy)
        policyImprovement(stateValues,policy)
        if oldPolicy==policy:
            cooldown+=1
        else:
            cooldown=0
        oldPolicy=copy.deepcopy(policy)
    print(policy)
