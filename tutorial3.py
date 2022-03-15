class Person():
    def __init__(self):  #initialize the obj
        self.name=''
        self.age=''
        self.weight=''
        self.height=''
        self.ID=''

    def input_person_data(self,name,age,weight,height,ID):  #set the attribute
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.ID = ID

    def get_person_data(self):                           #get the obj attributes
        print("The person's name is: " + self.name)
        print('The person is ', self.age, ' years old')
        print('The person is ', self.weight, ' kilogram')
        print('The person is ', self.height, ' cm tall')
        print("The person's ID number is: ", self.ID)
        print('-------------------------------------------------')

def main():
    Person1 =Person()                                               #create obj person1
    Person1.input_person_data('JACK','17','80','180','1134')        #input person1's attributes
    Person2 =Person()                                               #create obj person2
    Person2.input_person_data('Queen','19','40','160','5586')       #input person2's attributes

    Person1.get_person_data()                                       #print person1's name,age,weight,height,ID...
    Person2.get_person_data()                                       #print person2's attributes

main()






