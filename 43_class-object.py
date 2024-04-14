class Information:
    Name = "Dhruv"
    Age  = 21
    City = "Mehsana"
    def  display_info(self):
        print(f"Name : {self.Name}\nAge : {self.Age}\nCity : {self.City}")
        
# Create object of the class
person1 = Information()
person1.Name = "Tony"
person1.Age = 21
person1.City = "Ahemdabad"

person1.display_info()