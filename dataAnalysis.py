import pylab
import numpy as np
import statsmodels.api as sm
from pandas import DataFrame, Series
from sklearn.linear_model import LinearRegression
import scipy, scipy.stats
def main():
    
	candidatesOpinion = [[0 for x in range(8)] for x in range(4)] #String array candidates opinions
	for i in range(0, 4):
		for j in range(0, 8):
			'''Take from database, doesn't have to be hosted'''
			candidatesOpinion[i][j] = "Candidate " + str(j+1) + " thinks this about issue " + str(i+1)
	usersOpinion = [[0 for x in range(8)] for x in range(4)] #Int array of total agreements 
	for i in range(0, 4):
		for j in range(0, 8):
			usersOpinion[i][j] = 0 #Take from database
	totalSubmissions = 0 #Tally of total votes, take from database
	for i in range(0, 3):
		for j in range(0, 8):
			print(candidatesOpinion[i][j])
			usrInput = int(input("(Enter 1/0) Do you agree? "))
			usersOpinion[i][j] += usrInput
	for i in range(3, 4):
		for j in range(0, 8):
			usrVote = int(input(  "(Only pick one) Would you vote for candidate " + str(j+1) + " " ))
			usersOpinion[i][j] += usrVote
    
	totalSubmissions += 1
	i1=[]
	i2=[]
	i3=[]
	iV=[]
	print usersOpinion
	for i in range(0,8):
	   i1.append(usersOpinion[0][i]/totalSubmissions)
	   i2.append(usersOpinion[1][i]/totalSubmissions)
	   i3.append(usersOpinion[2][i]/totalSubmissions)
	   iV.append(usersOpinion[3][i]/totalSubmissions)
        
        #Calculate OLS betas with this data
        result1 = sm.OLS( iV, i3 ).fit()
        b1 = result1.params[0]
        result2 = sm.OLS( iV, i2 ).fit()
        b2 = result2.params[0]
        result3 = sm.OLS( iV, i1 ).fit()
        b3 = result3.params[0]
        #difference from slope of 1 denotes importance
        #lower the difference = greater the importance of the issue
	diff1 = 1 - b1
	diff2 = 1 - b2
	diff3 = 1 - b3
	print diff1
	print diff2
	print diff3

	
main()