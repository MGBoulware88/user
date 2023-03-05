class User:
    def __init__(self,first,last,email,age,member=False,points=0):
        self.first_name = first
        self.last_name = last
        self.email = email
        self.age = age
        self.is_rewards_member = member
        self.gold_card_points = points

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)

    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
            return False
        self.is_rewards_member = True
        self.gold_card_points = 200
        return True

    def spend_points(self,amount):
        if self.gold_card_points >= amount:
            self.gold_card_points-=amount
        else: print("Your balance is too low.")

gray = User('Gray','Boulware','gray@gmail.com',34)
gray.enroll()
gray.spend_points(50)


rick = User('Rick','Sanchez','rick@rick.com',67)
rick.enroll()
rick.spend_points(80)

morty = User('Morty','Smith','morty@getsome.com',15)




gray.display_info()
print('')
morty.display_info()
print('')
morty.display_info()

#BONUS

gray.enroll()

morty.spend_points(40)