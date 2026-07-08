name=input("Student Name : ")
pcm=int(input("PCM Percentage : "))
entrance_score=int(input("Entrance Exam Score : "))
print(f"{name} you are ",end="")
if (pcm>=60 and entrance_score>=60):
    print("eligible for admission")
elif (pcm<60 and entrance_score>=60):
    print("wait listed")
else : 
    print("not eligible for admission")