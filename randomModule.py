import random

#random values from float
print(f"random.random() = {random.random()}")  #0.0 ≤ value < 1.0

#fixing random sequence
#random.seed(34)  #> value fix kar dega  jaruri nhi hai 34 hi do kucch bhi de do

#random values from integer
print(f"random.randint(1,10) = {random.randint(1,10)}")  # start ≤ value ≤ end
print(f"random.randint(1,6) = {random.randint(1,6)}")

print(f"random.random() = {random.random()}")

#random values (float) in a range
print(f"random.uniform(10,25) = {random.uniform(10,25)}")  #a ≤ value ≤ b   Ye float (decimal) value deta hai

#we can also use this random function over the iterable objects
fruits=["Apple","Orange","Grapes","Pineapple","Guava","Lichi"]
print(f"random.choice(fruits) = {random.choice(fruits)}")

#picking multiple items (repeatation is not allowed here)
print(f"random.sample(fruits,2) = {random.sample(fruits,2)}")

#shuffling a list using shuffle()
cards = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(cards)
print(f'Cards after shuffling : {cards}')