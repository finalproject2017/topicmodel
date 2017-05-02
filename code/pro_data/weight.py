import numpy as np

with open('wordBags.txt') as line:
    word_dic = line.read().splitlines()


len_list = len(word_dic)
topic_word = np.ndarray(shape=(4,len_list),dtype=np.intc)
topic_word.fill(1)

food_string = "appet beef burger cake chees chicken cook crab cream delici dessert egg fish flavor food fri grill lobster meat pizza pork portion potato salad sauc shrimp soup spici steak sushi tast tasti"
food_list = []
service_string = "amiabl accommod attent complaint courteous effici efficient explain hostess friendli knowledg ineffici profession polit question quick quickli serv server servic slow staff suggest waiter waitress"
service_list = []
value_string = "averag cheap cost cheaper cheapest cheapli expens fair fairli justifi monei price pricei priceless reason steep valu valuabl"
value_list = []
atmosphere_string = "ambianc atmosph atmospher comfort cozi decor decoracion interior loud loudli nois noisi music patio quiet sett view romant romanc romantic"
atmosphere_list =[]


for word in food_string.split():
    food_list.append(word)
for word in service_string.split():
    service_list.append(word)
for word in value_string.split():
    value_list.append(word)
for word in atmosphere_string.split():
    atmosphere_list.append(word)


assign_weight = 1000000

for word in food_list:
    if word in word_dic:
        position = word_dic.index(word)
        topic_word[0][position] = assign_weight
for word in service_list:
    if word in word_dic:
        position = word_dic.index(word)
        topic_word[1][position] = assign_weight
for word in value_list:
    if word in word_dic:
        position = word_dic.index(word)
        topic_word[2][position] = assign_weight
for word in atmosphere_list:
    if word in word_dic:
        position = word_dic.index(word)
        topic_word[3][position] = assign_weight



vocal = tuple(word_dic)

print(type(vocal))

print(type(vocal[0]))
print(vocal[0])

np.save('topic_voc.npy', topic_word)





