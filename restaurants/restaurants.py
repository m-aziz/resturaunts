#description: Answers questions about the resturaunt database
#author: Aziz, Muhammad
#date: 11.20.18

#Main
restFile = open('restaurants.txt','r')
linez = restFile.readlines()

#create 2D List of string with blanks removed" 
rest2DList = [[s.lstrip().rstrip() for s in x.split(',')]
              for x in linez]


#Cuisine and Highest Rating
rating = float(rest2DList[0][4])
cuisine = str(rest2DList[0][2])
for num in range(1,len(rest2DList)):
    if float(rest2DList[num][4]) > rating:
        rating = float(rest2DList[num][4])
        cuisine = str(rest2DList[num][2])
print()
print("The cuisine with the highest average rating of",rating,"is",cuisine)

#Cuisine and Lowest Rating
rating = float(rest2DList[0][4])
cuisine = str(rest2DList[0][2])
for num in range(1,len(rest2DList)):
    if float(rest2DList[num][4]) < rating:
        rating = float(rest2DList[num][4])
        cuisine = str(rest2DList[num][2])
print()
print("The cuisine with the lowest average rating of",rating,"is",cuisine)

#Resturaunt and Highest Rating
rating = float(rest2DList[0][4])
restaurant = str(rest2DList[0][0])
for num in range(1,len(rest2DList)):
    if float(rest2DList[num][4]) > rating:
        rating = float(rest2DList[num][4])
        restaurant = str(rest2DList[num][0])
print()
print("The restaurant with the highest average rating of",rating,"is",restaurant)

#Resturaunt and Highest Dollar Rating
dollar_rating = len(rest2DList[0][3])
string_form_rating = str(rest2DList[0][3])
restaurant = str(rest2DList[0][0])
string_form_rating = str(rest2DList[0][3])
for num in range(1,len(rest2DList)):
    if len(rest2DList[num][3]) > dollar_rating:
        dollar_rating = int(len(rest2DList[num][3]))
        string_form_rating = str(rest2DList[num][3])
        restaurant = str(rest2DList[num][0])
print()
print("The restaurant with the most expensive dollar rating of",string_form_rating,"is",restaurant)

#Boston Resturaunt and Lowest Rating
boston_list = []
for num in range(0,len(rest2DList)):
    if str(rest2DList[num][1]) == "Boston":
        boston_list.append(rest2DList[num])
low_boston_rating = float(boston_list[0][4])
boston_resturaunt = str(boston_list[0][0])
for num in range(1,len(boston_list)):
    if float(boston_list[num][4]) < low_boston_rating:
        low_boston_rating = float(boston_list[num][4])
        boston_resturaunt = str(boston_list[num][0])
print()
print("The Boston restaurant with the lowest average rating of",low_boston_rating,"is",boston_resturaunt)
    
              
    
    
