## Project 2 ##
import pandas as pd

data= pd.read_excel("C:/Users/rajesh/Desktop/DS project/project 2/Data.xlsx")
data.isna().sum() #nan exists
data_new= data.iloc[0:]
data_new.columns


## replacing M&MF columns with scores
data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I feel lonely]"].replace({'Never':0,'Sometimes':1,'Always':2},inplace=True)
data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I cry a lot]"].replace({'Never':0,'Sometimes':1,'Always':2},inplace=True)
data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I am unhappy]"].replace({'Never':0,'Sometimes':1,'Always':2},inplace=True)
data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I feel nobody likes me]"].replace({'Never':0,'Sometimes':1,'Always':2},inplace=True)
data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I worry a lot]"].replace({'Never':0,'Sometimes':1,'Always':2},inplace=True)
data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I have problems sleeping]"].replace({'Never':0,'Sometimes':1,'Always':2},inplace=True)
data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I wake up in the night]"].replace({'Never':0,'Sometimes':1,'Always':2},inplace=True)
data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I am shy]"].replace({'Never':0,'Sometimes':1,'Always':2},inplace=True)
data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I feel scared]"].replace({'Never':0,'Sometimes':1,'Always':2},inplace=True)
data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I worry when I am at school]"].replace({'Never':0,'Sometimes':1,'Always':2},inplace=True)
data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I get very angry]"].replace({'Never':0,'Sometimes':1,'Always':2},inplace=True)
data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I lose my temper]"].replace({'Never':0,'Sometimes':1,'Always':2},inplace=True)
data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I hit out when I am angry]"].replace({'Never':0,'Sometimes':1,'Always':2},inplace=True)
data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I do things to hurt people]"].replace({'Never':0,'Sometimes':1,'Always':2},inplace=True)
data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I am calm]"].replace({'Never':2,'Sometimes':1,'Always':0},inplace=True)
data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I break things on purpose]"].replace({'Never':0,'Sometimes':1,'Always':2},inplace=True)


#Adding the scores of M&MF into a new column

emotional_scores= data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I feel lonely]"] + data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I cry a lot]"] + data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I am unhappy]"]+ data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I feel nobody likes me]"] + data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I worry a lot]"] + data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I have problems sleeping]"] + data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I wake up in the night]"] + data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I am shy]"] + data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I feel scared]"] + data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I worry when I am at school]"]  
behavioral_scores= data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I get very angry]"] + data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I lose my temper]"] + data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I hit out when I am angry]"] + data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I do things to hurt people]"] + data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I am calm]"] + data_new["24. Remember, there are no right or wrong answers, just pick which is right for you. [I break things on purpose]"]

# renaming the scores according to the sheet

#for emotional scores

for i in range(len(emotional_scores)):
    if emotional_scores[i]>=0 and emotional_scores[i] <=9:
        emotional_scores[i]= 'expected normal'
    elif emotional_scores[i]>=10 and emotional_scores[i]<=11:
        emotional_scores[i]= 'borderline difficulties'
    elif emotional_scores[i]>=12:
        emotional_scores[i]= 'clinically significant difficulties'
        
# for behavioral scores
        
for i in range(len(behavioral_scores)):
    if behavioral_scores[i]>=0 and behavioral_scores[i] <=5:
        behavioral_scores[i]= 'expected normal'
    elif behavioral_scores[i]==6:
        behavioral_scores[i]= 'borderline difficulties'
    elif behavioral_scores[i]>=7:
        behavioral_scores[i]= 'clinically significant difficulties'
        
        
# addding the two columns into the dataframe

data_new["emotional_scores"]= emotional_scores
data_new["behavioral_scores"]= behavioral_scores

emotional_pie= pd.DataFrame(data_new["emotional_scores"].value_counts())
behavioral_pie= pd.DataFrame(data_new["behavioral_scores"].value_counts())

#pie chart for scores
import matplotlib.pyplot as plt

#pie chart for behavioral difficulties
fig, ax= plt.subplots(figsize=(10,7))
ax.pie(behavioral_pie.behavioral_scores, labels= behavioral_pie.index, autopct= '%.1f%%')
ax.set_title('pie chart for behavioral difficulties')
plt.tight_layout()

# pie chart for emotional difficulties

fig, ax= plt.subplots(figsize=(10,7))
ax.pie(emotional_pie.emotional_scores, labels= emotional_pie.index, autopct= '%.1f%%')
ax.set_title('pie chart for emotional difficulties')
plt.tight_layout()

# replacing other columns with scores

data_new["17. How often do you go out to play outside?"].replace({'A few days each week':1, 'Hardly ever':2, "I don't play":3, 'Most days':4}, inplace= True)
data_new["18. Do you have enough time for play?"].replace({'No, I need a lot more':1, 'No, I would like to have a bit more':2, "Yes, I have loads":3, "Yes, it's just about enough":4}, inplace= True)
data_new["22. Tell us if you agree or disagree with the following: [I am doing well with my school work]"].replace({"Strongly agree":1, "Agree":2, "Disagree":3, "Strongly disagree":4, "Don't agree or disagree":5}, inplace=True)
data_new["22. Tell us if you agree or disagree with the following: [I feel part of my school community]"].replace({"Strongly agree":1, "Agree":2, "Disagree":3, "Strongly disagree":4, "Don't agree or disagree":5}, inplace=True)
data_new["22. Tell us if you agree or disagree with the following: [I have lots of choice over things that are important to me]"].replace({"Strongly agree":1, "Agree":2, "Disagree":3, "Strongly disagree":4, "Don't agree or disagree":5}, inplace=True)
data_new["22. Tell us if you agree or disagree with the following: [There are lots of things I'm good at]"].replace({"Strongly agree":1, "Agree":2, "Disagree":3, "Strongly disagree":4, "Don't agree or disagree":5}, inplace=True)
data_new["27. If yes, how are you keeping in touch (tick all you use)?"].value_counts()


# removing day, month and year  columns
data_new= data_new.drop(["Year"], axis=1)
data_new= data_new.drop(["Month"], axis=1)
data_new= data_new.drop(["Day"], axis=1)
data_new= data_new.drop(['ID'],axis=1)


# calculating hours slept
data_new["4. What time did you fall asleep YESTERDAY (to the nearest half hour)?"] = pd.to_datetime(data_new["4. What time did you fall asleep YESTERDAY (to the nearest half hour)?"])
data_new["5. What time did you wake up TODAY (to the nearest half hour)?"] = pd.to_datetime(data_new["5. What time did you wake up TODAY (to the nearest half hour)?"])

hours_slept= []
for i in range(len(data_new)):
    j= data_new["5. What time did you wake up TODAY (to the nearest half hour)?"][i] - data_new["4. What time did you fall asleep YESTERDAY (to the nearest half hour)?"][i]
    hours_slept.append(j)
 
hours_slept= pd.DataFrame(hours_slept)

hours_slept[0]= hours_slept[0].astype(str).map(lambda x: x[7:]) #slcing the column to remove the days

for i in range(len(hours_slept)):
    hours_slept[0][i]= hours_slept[0][i].replace(" ","")
    hours_slept[0][i]= hours_slept[0][i].replace("+","")
    
data_new.insert(11, 'hours_slept', hours_slept) #adding hours slept column to the dataset

data_new.hours_slept.value_counts()

hours_slept_pie= pd.DataFrame(hours_slept.value_counts())

fig, ax= plt.subplots(figsize=(10,7))
ax.pie(hours_slept_pie[0], labels= hours_slept_pie.index, autopct= '%.1f%%')
ax.set_title('pie chart for sleeping hours')
plt.tight_layout()

# catogorising breakfast column 
breakfast= data_new["1. What did you eat for breakfast YESTERDAY?"].value_counts()

breakfast_items= []

healthy_cereal=['Healthy cereal','fruits','Fruit']
sugary_cereal= ['Sugary cereal']
baked= ['Toast' ,'Croissant','croissant' ,'bread' , 'Bread' , 'cake' , 'brioche' , 'Brioche' , 'Brioch' , 'biscuit' , 'crumpet' ,'Crumpet' , 'CRUMPET' , 'waffle' , 'Waffle' , 'crackerbread' , 'sandwich' , 'Bun']
protein=['egg' , 'sausage' , 'bacon' , 'Bacon' , 'cheese' , 'Egg' , 'omlet' , 'yogurt' , 'Yoghurt']
for i in range(len(data_new)):
    if any(word in data_new["1. What did you eat for breakfast YESTERDAY?"][i] for word in healthy_cereal):
        breakfast_items.append('Healthy cereal')
    elif any(word in data_new["1. What did you eat for breakfast YESTERDAY?"][i] for word in sugary_cereal):
        breakfast_items.append('Sugary cereal')
    elif any( word in data_new["1. What did you eat for breakfast YESTERDAY?"][i] for word in baked):
        breakfast_items.append('Baked')
    elif any(word in data_new["1. What did you eat for breakfast YESTERDAY?"][i] for word in protein):
        breakfast_items.append('Protein')
    else:
        breakfast_items.append('Others')
breakfast_items= pd.DataFrame(breakfast_items)     

# pie chart for breakfast
breakfast_pie= pd.DataFrame(breakfast_items.value_counts())

fig, ax= plt.subplots(figsize=(10,7))
ax.pie(breakfast_pie[0], labels= breakfast_pie.index, autopct= '%.1f%%')
ax.set_title('pie chart for distrubution of breakfast')
plt.tight_layout()

# adding the categorised column into the data

data_new= data_new.drop(["1. What did you eat for breakfast YESTERDAY?"], axis=1)  

data_new.insert(7, 'breakfast_eaten', breakfast_items)

# categorising playing area column

places_to_play= data_new["19. What type of places do you play in?"].value_counts()

places= data_new["19. What type of places do you play in?"].copy()
places= pd.DataFrame(places)

for i in range(2,986):    
    if "bush" in places["19. What type of places do you play in?"][i]:
        places['19. What type of places do you play in?'][i]= 'In a place with bushes, trees and flowers'
    if 'Local grassy areas' in places['19. What type of places do you play in?'][i]:
        places['19. What type of places do you play in?'][i]= 'On local grassy areas'
    if 'local grassy area' in places['19. What type of places do you play in?'][i]:
        places['19. What type of places do you play in?'][i]= 'On local grassy areas'
    if 'bike or skate park' in places['19. What type of places do you play in?'][i]:
        places['19. What type of places do you play in?'][i]= 'On the bike or skate park'
    if 'bike' in places['19. What type of places do you play in?'][i]:
        places['19. What type of places do you play in?'][i]= 'On the bike or skate park'
    if 'park' in places['19. What type of places do you play in?'][i]:
        places['19. What type of places do you play in?'][i]= 'On the bike or skate park'
    if 'Out the front of my house' in places['19. What type of places do you play in?'][i]:
        places['19. What type of places do you play in?'][i]= 'Out the front of my house'
    if 'near my house' in places['19. What type of places do you play in?'][i]:
        places['19. What type of places do you play in?'][i]= 'Out the front of my house'
    if 'street' in places['19. What type of places do you play in?'][i]:
        places['19. What type of places do you play in?'][i]= 'Out the front of my house'
    if 'garden' in places['19. What type of places do you play in?'][i]:
        places['19. What type of places do you play in?'][i]= 'In the garden'
    if 'In my house' in places['19. What type of places do you play in?'][i]:
        places['19. What type of places do you play in?'][i]= 'In their homes'
    if 'in my house' in places['19. What type of places do you play in?'][i]:
        places['19. What type of places do you play in?'][i]= 'In their homes'
    else:
        places['19. What type of places do you play in?'][i]= places['19. What type of places do you play in?'][i]

places_new= places['19. What type of places do you play in?'].value_counts()
places_new= pd.DataFrame(places_new)

# pie chart for places to play
fig, ax= plt.subplots(figsize=(10,7))
ax.pie(places_new['19. What type of places do you play in?'], labels= places_new.index, autopct= '%.1f%%')
ax.set_title('pie chart for places to play')
plt.tight_layout()

# dropping the 19 column and adding the places column to the data
data_new= data_new.drop(['19. What type of places do you play in?'], axis=1)
data_new.insert(25, '19. What type of places do you play in?', places)

#dropping columns
data_new.columns
data_new= data_new.drop(['4. What time did you fall asleep YESTERDAY (to the nearest half hour)?'], axis=1)
data_new= data_new.drop(['5. What time did you wake up TODAY (to the nearest half hour)?'], axis=1)
data_new= data_new.drop(['24. Remember, there are no right or wrong answers, just pick which is right for you. [I feel lonely]',
       '24. Remember, there are no right or wrong answers, just pick which is right for you. [I cry a lot]',
       '24. Remember, there are no right or wrong answers, just pick which is right for you. [I am unhappy]',
       '24. Remember, there are no right or wrong answers, just pick which is right for you. [I feel nobody likes me]',
       '24. Remember, there are no right or wrong answers, just pick which is right for you. [I worry a lot]',
       '24. Remember, there are no right or wrong answers, just pick which is right for you. [I have problems sleeping]',
       '24. Remember, there are no right or wrong answers, just pick which is right for you. [I wake up in the night]',
       '24. Remember, there are no right or wrong answers, just pick which is right for you. [I am shy]',
       '24. Remember, there are no right or wrong answers, just pick which is right for you. [I feel scared]',
       '24. Remember, there are no right or wrong answers, just pick which is right for you. [I worry when I am at school]',
       '24. Remember, there are no right or wrong answers, just pick which is right for you. [I get very angry]',
       '24. Remember, there are no right or wrong answers, just pick which is right for you. [I lose my temper]',
       '24. Remember, there are no right or wrong answers, just pick which is right for you. [I hit out when I am angry]',
       '24. Remember, there are no right or wrong answers, just pick which is right for you. [I do things to hurt people]',
       '24. Remember, there are no right or wrong answers, just pick which is right for you. [I am calm]',
       '24. Remember, there are no right or wrong answers, just pick which is right for you. [I break things on purpose]'], axis=1)

#dropping na values in data_new
data_new= data_new.dropna()

# label encoding data
from sklearn.preprocessing import LabelEncoder
lb= LabelEncoder()

# label encoding columns with two classes
data_new['Do you have any other children living in your house with you?']= lb.fit_transform(data_new['Do you have any other children living in your house with you?'])
data_new['Gender']= lb.fit_transform(data_new['Gender'])
data_new['14. From your house, can you easily walk to a park (for example a field or grassy area)?']= lb.fit_transform(data_new['14. From your house, can you easily walk to a park (for example a field or grassy area)?'])
data_new['15. From your house, can you easily walk to somewhere you can play?']= lb.fit_transform(data_new['15. From your house, can you easily walk to somewhere you can play?'])
data_new['16. Do you have a garden?']= lb.fit_transform(data_new['16. Do you have a garden?'])
data_new["25. Are you able to keep in touch with your family that you don't live with? (grand parents, Uncle, Aunt, Cousins, etc)"]= lb.fit_transform(data_new["25. Are you able to keep in touch with your family that you don't live with? (grand parents, Uncle, Aunt, Cousins, etc)"])
data_new['26. Are you able to keep in touch with your friends?']= lb.fit_transform(data_new['26. Are you able to keep in touch with your friends?'])

#dummy variables for columns
going_school= pd.get_dummies(data_new['Are you still going to school?'])
data_new= pd.concat([data_new, going_school], axis=1)
data_new= data_new.drop(['Are you still going to school?'], axis=1)


fruits_veg_dummies= pd.get_dummies(data_new['2. Did you eat any fruit and vegetables YESTERDAY? '])
data_new= pd.concat([data_new,fruits_veg_dummies], axis=1)
data_new= data_new.drop(['2. Did you eat any fruit and vegetables YESTERDAY? '], axis=1)


noof_inhouse= pd.get_dummies(data_new['How many people live in your home with you (including adults)?'])
data_new= pd.concat([data_new,noof_inhouse],axis=1)
data_new= data_new.drop(['How many people live in your home with you (including adults)?'], axis=1)


year_child= pd.get_dummies(data_new['What year are you in now?'])
data_new= pd.concat([data_new, year_child], axis=1)
data_new= data_new.drop(['What year are you in now?'], axis=1)


breakfast_eaten= pd.get_dummies(data_new['breakfast_eaten'])
data_new= pd.concat([data_new, breakfast_eaten], axis=1)
data_new= data_new.drop(['breakfast_eaten'], axis=1)



noof_sports= pd.get_dummies(data_new["6. In the last 7 days, how many days did you do sports or exercise for at least 1 hour in total. This includes doing any activities (including online activities) or playing sports where your heart beat faster, you breathed faster and you felt warmer?"])
data_new= pd.concat([data_new, noof_sports], axis=1)
data_new= data_new.drop(["6. In the last 7 days, how many days did you do sports or exercise for at least 1 hour in total. This includes doing any activities (including online activities) or playing sports where your heart beat faster, you breathed faster and you felt warmer?"], axis=1)


hours_slept= pd.get_dummies(data_new['hours_slept'])
data_new= pd.concat([data_new, hours_slept], axis=1)
data_new= data_new.drop(['hours_slept'], axis=1)


allplaces_toplay= pd.get_dummies(data_new["20. Can you play in all the places you would like to?"])
data_new= pd.concat([data_new, allplaces_toplay],axis=1)
data_new=data_new.drop(["20. Can you play in all the places you would like to?"],axis=1)



typeof_place= pd.get_dummies(data_new['19. What type of places do you play in?'])
data_new= pd.concat([data_new, typeof_place],axis=1)
data_new=data_new.drop(['19. What type of places do you play in?'],axis=1)



relax_place = pd.get_dummies(data_new['21. Do you have somewhere at home where you have space to relax?'])
data_new= pd.concat([data_new, relax_place],axis=1)
data_new=data_new.drop(['21. Do you have somewhere at home where you have space to relax?'],axis=1)



#taking only the first value from the remaining columns
data_new['7. In the last 7 days, how many days did you watch TV/play online games/use the internet etc. for 2 or more hours a day (in total)?']= data_new['7. In the last 7 days, how many days did you watch TV/play online games/use the internet etc. for 2 or more hours a day (in total)?'].astype(str).map(lambda x: x[:1])
data_new['8. In the last 7 days, how many days did you feel tired?']= data_new['8. In the last 7 days, how many days did you feel tired?'].astype(str).map(lambda x: x[:1])
data_new['9. In the last 7 days, how many days did you feel like you could concentrate/pay attention well on your school work?']= data_new['9. In the last 7 days, how many days did you feel like you could concentrate/pay attention well on your school work?'].astype(str).map(lambda x: x[:1])
data_new['10. In the last 7 days, how many days did you drink at least one fizzy drink (e.g. coke, sprite, thumsup)?']= data_new['10. In the last 7 days, how many days did you drink at least one fizzy drink (e.g. coke, sprite, thumsup)?'].astype(str).map(lambda x: x[:1])
data_new['11. In the last 7 days, how many days did you eat at least one sugary snack (e.g. chocolate bar, sweets)?']= data_new['11. In the last 7 days, how many days did you eat at least one sugary snack (e.g. chocolate bar, sweets)?'].astype(str).map(lambda x: x[:1])
data_new['12. In the last 7 days, how many days did you eat take away foods (e.g. Chinese takeaway)?']= data_new['12. In the last 7 days, how many days did you eat take away foods (e.g. Chinese takeaway)?'].astype(str).map(lambda x: x[:1])

#replacing 27th column with one value

keeping_touch= data_new['27. If yes, how are you keeping in touch (tick all you use)?']
keeping_touch= pd.DataFrame(keeping_touch)
for i in keeping_touch.index:    
    if 'I live near' in keeping_touch['27. If yes, how are you keeping in touch (tick all you use)?'][i]:
        keeping_touch['27. If yes, how are you keeping in touch (tick all you use)?'][i]= 'I live near by them'
    elif 'By phone' in keeping_touch['27. If yes, how are you keeping in touch (tick all you use)?'][i]:
        keeping_touch['27. If yes, how are you keeping in touch (tick all you use)?'][i] = 'By phone'
    else:
        keeping_touch['27. If yes, how are you keeping in touch (tick all you use)?'][i] = 'On social media'
keeping_touch["27. If yes, how are you keeping in touch (tick all you use)?"].replace({"I live near by them":1,"By phone":2,"On social media":3},inplace=True)
data_new= data_new.drop(['27. If yes, how are you keeping in touch (tick all you use)?'], axis=1)
data_new.insert(27, '27. If yes, how are you keeping in touch (tick all you use)?', keeping_touch )

#converting the object columns to integer
data_new["7. In the last 7 days, how many days did you watch TV/play online games/use the internet etc. for 2 or more hours a day (in total)?"]=data_new["7. In the last 7 days, how many days did you watch TV/play online games/use the internet etc. for 2 or more hours a day (in total)?"].astype(str).astype(int)
data_new["8. In the last 7 days, how many days did you feel tired?"]=data_new["8. In the last 7 days, how many days did you feel tired?"].astype(str).astype(int)
data_new["9. In the last 7 days, how many days did you feel like you could concentrate/pay attention well on your school work?"]=data_new["9. In the last 7 days, how many days did you feel like you could concentrate/pay attention well on your school work?"].astype(str).astype(int)
data_new["10. In the last 7 days, how many days did you drink at least one fizzy drink (e.g. coke, sprite, thumsup)?"]=data_new["10. In the last 7 days, how many days did you drink at least one fizzy drink (e.g. coke, sprite, thumsup)?"].astype(str).astype(int)
data_new["11. In the last 7 days, how many days did you eat at least one sugary snack (e.g. chocolate bar, sweets)?"]=data_new["11. In the last 7 days, how many days did you eat at least one sugary snack (e.g. chocolate bar, sweets)?"].astype(str).astype(int)
data_new["12. In the last 7 days, how many days did you eat take away foods (e.g. Chinese takeaway)?"]=data_new["12. In the last 7 days, how many days did you eat take away foods (e.g. Chinese takeaway)?"].astype(str).astype(int)
# creating two datasets each having one output column
emotional_data= data_new.drop(['behavioral_scores'], axis=1)
behavioral_data= data_new.drop(['emotional_scores'], axis=1)

#### model building
## decision tree

emt_target= emotional_data.emotional_scores
emt_predictors= emotional_data.drop(['emotional_scores'], axis=1)

from sklearn.model_selection import train_test_split

emt_train_x, emt_test_x, emt_train_y, emt_test_y= train_test_split(emt_predictors, emt_target, test_size= 0.25)

from sklearn.tree import DecisionTreeClassifier as DT 
import numpy as np       

model= DT(criterion='entropy')        
model.fit(emt_train_x, emt_train_y)

# prediction on test data
preds_test= model.predict(emt_test_x)
np.mean(preds_test == emt_test_y) # Test Data Accuracy 

#prediction on train data

preds_train= model.predict(emt_train_x)
np.mean(preds_train == emt_train_y) # Train Data Accuracy # Over fitting in decision tree

#decision tree for behavioral data

bhv_target= behavioral_data['behavioral_scores']
bhv_predictors= behavioral_data.drop(['behavioral_scores'], axis=1)

bhv_train_x, bhv_test_x, bhv_train_y, bhv_test_y= train_test_split(bhv_predictors, bhv_target, test_size= 0.25)

model= DT(criterion='entropy')        
model.fit(bhv_train_x, bhv_train_y)

# prediction on test data
preds_test= model.predict(bhv_test_x)
np.mean(preds_test == bhv_test_y) # Test Data Accuracy 

#prediction on train data

preds_train= model.predict(bhv_train_x)
np.mean(preds_train == bhv_train_y) # Train Data Accuracy



# multinomial logistic Regression for emotional data
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import seaborn as sns


model = LogisticRegression(multi_class = "multinomial", solver = "newton-cg").fit(emt_train_x, emt_train_y)

test_preds= model.predict(emt_test_x)

# Test accuracy 
accuracy_score(emt_test_y, test_preds)

train_predict= model.predict(emt_train_x)
#train accuracy
accuracy_score(emt_train_y, train_predict) #close to not overfit

#multinomial logistic regression for behavioral data

model = LogisticRegression(multi_class = "multinomial", solver = "newton-cg").fit(bhv_train_x, bhv_train_y)

test_preds= model.predict(bhv_test_x)

# Test accuracy 
accuracy_score(bhv_test_y, test_preds)

train_predict= model.predict(bhv_train_x)
#train accuracy
accuracy_score(bhv_train_y, train_predict) #overfitting


#ordinal regression for emotional data before feature selection
####
emotional_scores= emotional_data["emotional_scores"]
emotional_scores.replace({'expected normal':1, 'borderline difficulties':2, 'clinically significant difficulties':3},inplace=True)
emotional_data= emotional_data.drop(['emotional_scores'],axis=1)
emotional_data.insert(0, 'emotional_scores', emotional_scores)


behavioral_scores= behavioral_data["behavioral_scores"]
behavioral_scores.replace({'expected normal':1, 'borderline difficulties':2, 'clinically significant difficulties':3},inplace=True)
behavioral_data= behavioral_data.drop(['behavioral_scores'],axis=1)
behavioral_data.insert(0, 'behavioral_scores', behavioral_scores)


from mord import LogisticAT
emt_target= emotional_data['emotional_scores']
emt_predictors= emotional_data.drop(['emotional_scores'], axis=1)
emt_train_x, emt_test_x, emt_train_y, emt_test_y= train_test_split(emt_predictors, emt_target, test_size= 0.25)
model = LogisticAT(alpha = 0).fit(emt_train_x, emt_train_y)  
# alpha parameter set to zero to perform no regularisation.fit(x_train,y_train)
model.coef_
model.classes_

predict = model.predict(emt_test_x) # Train predictions 

# Accuracy 
accuracy_score(emt_test_y, predict)

#ordinal regression for behavioural data

bhv_target= behavioral_data['behavioral_scores']
bhv_predictors= behavioral_data.drop(['behavioral_scores'], axis=1)
bhv_train_x, bhv_test_x, bhv_train_y, bhv_test_y= train_test_split(bhv_predictors, bhv_target, test_size= 0.25)
model = LogisticAT(alpha = 0).fit(bhv_train_x, bhv_train_y)

predict= model.predict(bhv_test_x) # train predictions
accuracy_score(bhv_test_y, predict) #accuracy


# Correlation values between each independent features
corr_emotional= emotional_data.corr()
corr_behavioral= behavioral_data.corr()
emotional_data.columns
behavioral_data.columns
#dropping columns that have very less correlation with emotional scores
emotional_data= emotional_data.drop(["3. How many times did you brush your teeth YESTERDAY?", "13. On a scale of 0 to 10 (0 being not very safe and 10 being very safe), how safe do you feel playing in your area?", "18. Do you have enough time for play?", 'Your Health ','Your School', 'Your Family', 'Your Friends', 'Your Appearance (how you look)','Your Life', "Yes, most days of the week", "26. Are you able to keep in touch with your friends?", "06:00:00", "06:30:00", "12:30:00", "12:00:00", "14:30:00" ], axis=1)
behavioral_data= behavioral_data.drop(['Gender', '3. How many times did you brush your teeth YESTERDAY?','13. On a scale of 0 to 10 (0 being not very safe and 10 being very safe), how safe do you feel playing in your area?', '18. Do you have enough time for play?', 'Your Health ','Your School', 'Your Family', 'Your Friends','Your Appearance (how you look)', 'Your Life', "25. Are you able to keep in touch with your family that you don't live with? (grand parents, Uncle, Aunt, Cousins, etc)", '26. Are you able to keep in touch with your friends?', 1, 'Year 3', 'Protein', '0 days', '02:00:00', '03:30:00', '06:00:00', '06:30:00', '08:00:00', '08:30:00', '12:00:00', '12:30:00' ], axis=1)

# decision tree after feature selection
emt_target= emotional_data.emotional_scores
emt_predictors= emotional_data.drop(['emotional_scores'], axis=1)



emt_train_x, emt_test_x, emt_train_y, emt_test_y= train_test_split(emt_predictors, emt_target, test_size= 0.25)

model= DT(criterion='entropy')        
model.fit(emt_train_x, emt_train_y)

# prediction on test data
preds_test= model.predict(emt_test_x)
np.mean(preds_test == emt_test_y) # Test Data Accuracy 

#prediction on train data

preds_train= model.predict(emt_train_x)
np.mean(preds_train == emt_train_y) # Train Data Accuracy # Over fitting in decision tree

#decision tree for behavioral data after feature selection

bhv_target= behavioral_data['behavioral_scores']
bhv_predictors= behavioral_data.drop(['behavioral_scores'], axis=1)

bhv_train_x, bhv_test_x, bhv_train_y, bhv_test_y= train_test_split(bhv_predictors, bhv_target, test_size= 0.25)

model= DT(criterion='entropy')        
model.fit(bhv_train_x, bhv_train_y)

# prediction on test data
preds_test= model.predict(bhv_test_x)
np.mean(preds_test == bhv_test_y) # Test Data Accuracy 

#prediction on train data

preds_train= model.predict(bhv_train_x)
np.mean(preds_train == bhv_train_y) # Train Data Accuracy



# multinomial logistic Regression for emotional data after feature selection
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import seaborn as sns


model = LogisticRegression(multi_class = "multinomial", solver = "newton-cg").fit(emt_train_x, emt_train_y)

test_preds= model.predict(emt_test_x)

# Test accuracy 
accuracy_score(emt_test_y, test_preds)

train_predict= model.predict(emt_train_x)
#train accuracy
accuracy_score(emt_train_y, train_predict) #close to not overfit

#multinomial logistic regression for behavioral data after feature selection

model = LogisticRegression(multi_class = "multinomial", solver = "newton-cg").fit(bhv_train_x, bhv_train_y)

test_preds= model.predict(bhv_test_x)

# Test accuracy 
accuracy_score(bhv_test_y, test_preds)

train_predict= model.predict(bhv_train_x)
#train accuracy
accuracy_score(bhv_train_y, train_predict) #overfitting


#ordinal regression for emotional data after feature selection
####


from mord import LogisticAT
emt_target= emotional_data['emotional_scores']
emt_predictors= emotional_data.drop(['emotional_scores'], axis=1)
emt_train_x, emt_test_x, emt_train_y, emt_test_y= train_test_split(emt_predictors, emt_target, test_size= 0.25)
model = LogisticAT(alpha = 0).fit(emt_train_x, emt_train_y)  
# alpha parameter set to zero to perform no regularisation.fit(x_train,y_train)
model.coef_
model.classes_

predict = model.predict(emt_test_x) # Train predictions 

# Accuracy 
accuracy_score(emt_test_y, predict)

#ordinal regression for behavioural data after feature selection

bhv_target= behavioral_data['behavioral_scores']
bhv_predictors= behavioral_data.drop(['behavioral_scores'], axis=1)
bhv_train_x, bhv_test_x, bhv_train_y, bhv_test_y= train_test_split(bhv_predictors, bhv_target, test_size= 0.25)
model = LogisticAT(alpha = 0).fit(bhv_train_x, bhv_train_y)

predict= model.predict(bhv_test_x) # train predictions
accuracy_score(bhv_test_y, predict) #accuracy
