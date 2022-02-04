
#MSc Bioinformatics 2021/2022
#Python Assignment

def Task1function(): #task 1 function start.
    
        pop_array = []    #initial population list.
        popsize = 100     #Setting the population size, 'popsize', to 100. 

        
        #The below four lines of code creates a population size of 100. "popsize/2" for each as we want an equal number of 'A' and 'B' alleles. 
        for i in range(0, int(popsize/2)):
            pop_array.append('A')
        for i in range(int(popsize/2), popsize):
             pop_array.append('B')

    
        import random   #This module is needed as this assignment utilises the random.sample, random.randint and random.choice functions. 
       
        
        #The two variables below are the lists to count the number of 'A' and 'B' alleles. I use this list to plot the 'Y-axis' in Figure 1.
        counter_listA = [50]   #'[50]' initialises the starting point of Allele A in figure 1.
        counter_listB = [50]
        

        for k in range(0,1000):    #This is the outer for loop, as we need this script to complete 1000 generations. 
            new_pop_rlist = []     #This is the array to which a new population will be added, randomly chosen from the 'pop_array' array. 
            

            for j in range(0,100): #This is the inner for loop. 'Range(0,100)' as we want to create a population size of '100'.
                rand_pop_value = random.choice(pop_array)  #selects population at random from the 'pop_array' array, with replacement. 
                new_pop_rlist.append(rand_pop_value)       #adds the randomly selected population to the 'new_pop_rlist' list, which represents the new population. 
            
            
            
            #the below two lines of code initialises the counter for the alleles. 
            A_count = 0
            B_count = 0
            
            #the for loop below goes through the 'new_pop_rlist' array and counts the number of Alleles, either 'A' or 'B'.
            for i in new_pop_rlist:
                if i == 'A':
                    A_count += 1
                elif i == 'B':
                    B_count += 1
            
            
            #The below two lines of code adds the total count of the allels to a list, which was initialised earlier. This list then serves as the 'Y-axis' for Figure 1. 
            counter_listA.append(A_count)
            counter_listB.append(B_count)
            
            pop_array = new_pop_rlist #The new and original populations must be the same size, n = 100. 
            
            #The if statement below ensures that if either allele, 'A' or 'B' is lost from a population, then no further generations are completed.
            if new_pop_rlist.count('A') == 0 or new_pop_rlist.count('B') == 0:   
                break           
        
        #The below 8 lines of code are used to construct Figure 1. The 'Matplotlib' plotting library was utilised. 
    
        import matplotlib.pyplot as plt
        
        #Adding the X and Y axis values, as well as labels for the line graph.
        plt.plot(range(len(counter_listA)), counter_listA, label = "Allele A")
        plt.plot(range(len(counter_listB)), counter_listB, label = "Allele B")
        
        plt.legend() #adds the legend to the plot. 
        plt.title("Figure 1. Change in allele frequency over " + str(k+1) + " generations")  #adds the plot title. 
         
        #The below two lines of codes adds the axis titles. 
        plt.xlabel("Number of generations")
        plt.ylabel("Allele Frequency")
         
        plt.show() ##line of code to show the plot.

print(Task1function())  #executes function 1.

def Task2Function():  #task 2 function start.
    
        import random   
        import matplotlib.pyplot as plt   #library needed for data visualisation. 
        ipop_list = []    #This is the initial population list. 
        pop_size_2 = 100  #population size = 100. 
        
        
        
        #The three variables below are the list to count the number of 'AA', 'aa', and 'Aa'. I use this list to plot the 'Y-axis' in Figure 2.
        count_listAA = [25]  #'[25]' initialises the starting point of the AA genotype in Figure 2. 
        count_listaa = [25]
        count_listAa = [50]


        #making the initial populations that has an even distribution of alleles: 25% are “AA”, 50% “Aa” (25% ‘Aa’ and 25% ‘aA’) and 25% “aa”: 
        #we add the output of the four for loops below into a list with name, 'ipop_list', with the ipop_list.appened('') command.
        for i in range(0, int(pop_size_2/4)):
            ipop_list.append('AA')
        for i in range(int(pop_size_2/4)):
             ipop_list.append('Aa')
        for i in range(0, int(pop_size_2/4)):
            ipop_list.append('aA')
        for i in range(int(pop_size_2/4)):
             ipop_list.append('aa') 
                
        for i in range(0,500): #range = 500 as we want to run the simulation for a maximum of 500 iterations.
            rpop_list = []  #This is the array for the new, randomly generated population.
            
            count = 1 #initialise counter to '1', as '0%5 = 0', which we don't want to add to the list.   
            while len(rpop_list) < 100: #we want to build up the rpop_list up until 100. 
                  
                rand_ipop_list_value_1 = random.sample(ipop_list, 2)    #'random.sample' selects two genotypes from 'ipop_list', without replacement, and adds them to the 'rand_ipop_list_value_1' list. 
                
                rand_ipop_list_value_2 = rand_ipop_list_value_1[0][random.randint(0, 1)] + rand_ipop_list_value_1[1][random.randint(0, 1)] 
                
                ########################################################################################################################################################
                #Breaking down the above line of code:                                                                                                                 #
                ##'randint' function will return a random number from a specified list,range is specified to be (0,1) -> start at the first element, end at the second-#
                # -element in the list.                                                                                                                                #
                #'rand_ipop_list_value_1[0][random.randint(0, 1)]': returns a single allele (randomly chosen), but from the first element ('[0]') of the list.         #
                #'rand_ipop_list_value_1[1][random.randint(0, 1)]': also returns a single allele (randomly chosen), but from the second element ('[1]')of the list.    #
                #We concatenate the alleles to a string, and assign that string to the 'rand_ipop_list_value_2' variable.                                              #                                     #
                ########################################################################################################################################################
                

                if rand_ipop_list_value_2 == "aa":
                    if count%5 != 0:  #If 'aa' counter value does have a remainder when dividing by '5', then continue to add to the list. This allows 1 in 5 of the 'aa' genotypes to be rejected.
                        rpop_list.append(rand_ipop_list_value_2)
                    count += 1
                else: 
                    rpop_list.append(rand_ipop_list_value_2) #continue to add the other genotypes to the 'rpop_list' list.
                                
                    
            ipop_list = rpop_list #The original and new/randomly generated populations must be the same size.
            
            ########################################################################################################################
            #The above seven lines of code have addressed the task: "With each generation one allele from each random individual-  #
            #-should be combined with one allele from another random individual to create a new population of 100'.                #                           
            ########################################################################################################################
                 
                  
            #the below three lines of code initialises the counter for the three genotypes. 
            Aa_count = 0
            aa_count = 0
            AA_count = 0
            
            
            #the for loop below goes through the 'rpop_list' and counts the number of genotypes. 
            for k in rpop_list:
                if k == 'AA':
                    AA_count += 1
                if k == 'Aa'or k =='aA': 
                    Aa_count += 1
                elif k == 'aa':
                    aa_count += 1  
            
                   
            #The below three lines of code adds the total count of the genotypes to a list, which was initialised earlier. This list then serves as the 'Y-axis' for Figure 2. 
            count_listAA.append(AA_count)
            count_listAa.append(Aa_count)
            count_listaa.append(aa_count)
            
            
            #The if statement below allows the simmulation to run until allele "a" disappears from the population. '[-1]'-> the last element in the list.
            if count_listAa[-1] == 0 and count_listaa[-1] == 0:
                break            
        
        #The below 8 lines of code are used to construct Figure 2. The 'Matplotlib' plotting library was utilised.
            
        #Adding the X and Y axis values, as well as labels. 
        plt.plot(range(len(count_listAa)), count_listAa, label = "Aa")
        plt.plot(range(len(count_listaa)), count_listaa, label = "aa") 
        plt.plot(range(len(count_listAA)), count_listAA, label = "AA")
        
        #Adding the axis titles.
        plt.xlabel("Number of generations")
        plt.ylabel("Allele Frequency")
        
        plt.legend()  #adding the legend.
        plt.title("Figure 2. Aa vs aa vs AA: Allele frequency over " + str(i+1) + " generations")  #plot title.
        plt.show() #line of code to show the plot.

print(Task2Function()) #executes function 2. 
            
        
                    
            
                
                
                
            
            
            


