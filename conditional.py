# userReply = input("Do you need to ship the package ? ( Enter Yes Or No ) ")
# if userReply == "Yes":
#     print(" We can help you ship that package! ")
# else:
#     print("Please come back when you need to ship the package . Thank you . ")
userReply = input("Would you like to   buy stamps ,buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")#input
  #condtion starts
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":# USER GOES WITH ENVELOPE
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":# USER GOES WITH THE COPY
    copies = input("How many copies would you like? (Enter a number) ")#GAVE THE INPUT 
    print("Here are {} copies.".format(copies))# .FORMAT IS USED
else:
    print("Thank you, please come again.")      