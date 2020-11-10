import random
class ArmedBandit1:
    name = "a1"
    times_spun = 0;
    money_earned = 0
    def spin(self):
        return random.randrange(10)
class ArmedBandit2:
    name = "a2"
    times_spun = 0 
    money_earned = 0
    def spin(self):
        return random.randrange(10)+2
class ArmedBandit3:
    name = "a3"
    times_spun = 0
    money_earned = 0
    def spin(self):
        return random.randrange(10)+5
class ArmedBandit4:
    name = "a4"
    times_spun = 0 
    money_earned = 0
    def spin(self):
        return random.randrange(10)+6
class ArmedBandit5:
    name = "a5"
    times_spun = 0
    money_earned = 0
    def spin(self):
        return 10

a1 = ArmedBandit1()
a2 = ArmedBandit2()
a3 = ArmedBandit3()
a4 = ArmedBandit4()
a5 = ArmedBandit5()
e_greedy_percent = 0.4 #explore random ones 40% of the time and 60% the best
total_money = 0
bandit_list = [a1,a2,a3,a4,a5]
best_bandit = bandit_list[0]

#``````````````````````````````````````````````````````````````
#def explore_all(b_b,bandit_list):
   # for t in range(5):
    #    x = bandit_list[t].spin()
     #   bandit_list[t].times_spun+=1
      #  bandit_list[t].money_earned+=x
       # if((bandit_list[t].money_earned/bandit_list[t].times_spun) > b_b.money_earned/b_b.times_spun):
        #    b_b = bandit_list[t]
 #   return b_b

#``````````````````````````````````````````````````````````

def explore_random(b_b):

    global bandit_list
    t = random.randrange(5)
    x = bandit_list[t].spin()
    bandit_list[t].times_spun+=1
    bandit_list[t].money_earned+=x
    global total_money 
    total_money+= x

    if(b_b.money_earned > 0):
        if((bandit_list[t].money_earned/bandit_list[t].times_spun) > b_b.money_earned/b_b.times_spun):
                    b_b = bandit_list[t]
    return b_b

#````````````````````````````````````````````````````````

def exploit_best(b_b):
    x = b_b.spin()
   # best_bandit.times_spun+=1  I'm not going to record these since this would be exploring while exploiting
   # best_bandit.money_earned+=x
    global total_money
    total_money += x
    return b_b
#`````````````````````````````````````````````````````````    

total_runs = 100
i = 0
answer = input("Say G for Greedy (Epsilon = 0), or E for Epsilon Greedy (Epsilon = .4) \n")
if(answer == "G"):
    e_greedy_percent = 0.4
while( i < total_runs ):
    if(i < (total_runs - (total_runs * e_greedy_percent))):
        best_bandit = explore_random(best_bandit)
    else:
        best_bandit = exploit_best(best_bandit)
    i+=1
print("Total Money: "+str(total_money))
print("Best Bandit: "+best_bandit.name)
