#strip() - remove spaces from both ends
text="    Hello Guys    "
print(f"text.strip() - {text.strip()}")
print(f"text.lstrip() - {text.lstrip()}")
print(f"text.rstrip() - {text.rstrip()}")

#replace() - find and replace
message="I love java programmming"
message=message.replace('java','python') # string is immutable soo string me change nhi ho raha
print("message",message)

#split() - breaks string into list
csv_data="Raj,Student,CSE,UCER,Prayagraj"
csv_list=csv_data.split(",")
print(f"csv_list={csv_list}")

#join() - opposite of split
words=['How', 'are', 'you']
sentence=" ".join(words)
print(f"Sentence - {sentence}")