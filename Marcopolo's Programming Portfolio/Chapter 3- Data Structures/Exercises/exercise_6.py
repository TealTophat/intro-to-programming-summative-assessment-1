invitees = ["Abraham Lincoln","Albert Einstein","Michael Jackson"]
print("Dear " + invitees[0] + ", \
      I hereby formally invite you to attend a dinner party hosted by yours truly.")
print("Dear " + invitees[1] + ", \
      I hereby formally invite you to attend a dinner party hosted by yours truly.")
print("Dear " + invitees[2] + ", \
      I hereby formally invite you to attend a dinner party hosted by yours truly.")
print("Unfortunately, Albert Einstein will not be available to attend today's dinner party.")
invitees.remove("Albert Einstein")
invitees.append("Nikola Tesla")
print("Dear " + invitees[0] + ", \
      I hereby formally invite you to attend a dinner party hosted by yours truly.")
print("Dear " + invitees[1] + ", \
      I hereby formally invite you to attend a dinner party hosted by yours truly.")
print("Dear " + invitees[2] + ", \
      I hereby formally invite you to attend a dinner party hosted by yours truly.")
print("Due to technical issues, we will only be able to accommodate two guests\
       for the dinner party. Many apologies to the rest of the guests who cannot participate.")
print("Apologies to " + invitees[2] + ", as you will not be able to be accomodated.")
invitees.pop(2)
print("Dear " + invitees[0] + ", \
      Fortunately, we are still able to accommodate you at this time. Thank you for staying with us.")
print("Dear " + invitees[1] + ", \
      Fortunately, we are still able to accommodate you at this time. Thank you for staying with us.")
del invitees[1]
del invitees[2]
print(invitees)