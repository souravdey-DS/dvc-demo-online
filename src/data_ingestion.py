import pandas as pd
import numpy as np
import os


df = pd.read_csv("https://raw.githubusercontent.com/araj2/customer-database/master/Ecommerce%20Customers.csv")

"""
Sample:

Email,Address,Avatar,Avg. Session Length,Time on App,Time on Website,Length of Membership,Yearly Amount Spent
mstephenson@fernandez.com,"835 Frank Tunnel
Wrightmouth, MI 82180-9605",Violet,34.49726772511229,12.655651149166752,39.57766801952616,4.082620632952961,587.9510539684005
hduke@hotmail.com,"4547 Archer Common
Diazchester, CA 06566-8576",DarkGreen,31.926272026360156,11.109460728682564,37.268958868297744,2.66403418213262,392.2049334443264
pallen@yahoo.com,"24645 Valerie Unions Suite 582
Cobbborough, DC 99414-7564",Bisque,33.000914755642675,11.330278057777512,37.11059744212085,4.104543202376424,487.54750486747207
riverarebecca@gmail.com,"1414 David Throughway
Port Jason, OH 22070-1220",SaddleBrown,34.30555662975554,13.717513665142508,36.72128267790313,3.1201787827480914,581.8523440352178
mstephens@davidson-herman.com,"14023 Rodriguez Passage
Port Jacobville, PR 37242-1057",MediumAquaMarine,33.33067252364639,12.795188551078114,37.53665330059473,4.446308318351435,599.4060920457634
alvareznancy@lucas.biz,"645 Martha Park Apt. 611
Jeffreychester, MN 67218-7250",FloralWhite,33.87103787934198,12.026925339755058,34.47687762925054,5.493507201364199,637.102447915074
katherine20@yahoo.com,"68388 Reyes Lights Suite 692

"""

# Experiment 1 : Following data needs to be stored
# 1. Remove the non-numeric columns "Email,Address,Avatar"
# 2. Store the records for which "Length of Membership" > 3

#df = df.iloc[:, 3:]
#
#df  = df[df['Length of Membership'] > 3]
#
#df.to_csv(os.path.join('data','customer.csv'))

# Experiment 2 : Following data needs to be stored
# 1. Remove the non-numeric columns "Email,Address,Avatar"
# 2. Remove the column "Avg. Session Length"
# 3. Store the records for which "Length of Membership" > 1

df = df.iloc[:, 3:]

df.drop(columns=['Avg. Session Length'], inplace = True)

df=df[df['Length of Membership']>1]


df.to_csv(os.path.join('data','customer.csv'))

