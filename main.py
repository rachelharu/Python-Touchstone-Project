#main program
def main():
  #variable initialization
  destination = ""
  distance = 0
  rate = 0


# greet user with a prompt to input their destination and save as variable
destination = str(
  input("Hello there, this is RideTimer please enter your destination: "))
#while true to catch any errors of user input
while True:
  try:
    # prompt user to input their distance from destination and save as variable.
    distance = int(
      input("Please enter the distance(in miles) of " + destination + ": "))
  except ValueError:
    print("Please enter in a number.")
  else:
    break
# another while loop to catch any user input errors
while True:
  try:
    # prompt user to input their speed in miles per hour(mph) and save as variable.
    rate = int(input("Please enter how many miles per hour you are going: "))
  except ValueError:
    print("Please enter in a number.")
  else:
    break

#creation of list for closing messages
closingList = [
  "bring some cd's or an ipod to help pass the time.",
  "bring a movie or a newspaper to help pass the time.",
  "bring a book to help pass the time",
  "looks like you'll need to book a hotel for such a long trip."
]
# conversion math to convert distance divded by rate(mph) to get the time
time = distance / rate
#if else statements to check which closing message will be displayed based on the time from destination.
if time <= 1.0:
  print("You are about " + str("{0:.1f}".format(time)) + " hours from " +
        destination + " " + closingList[0])
elif time > 1.0 and time <= 3.0:
  print("You are about " + str("{0:.1f}".format(time)) + " hours from " +
        destination + " " + closingList[1])
elif time > 3.0 and time <= 10:
  print("You are about " + str("{0:.1f}".format(time)) + " hours from " +
        destination + " " + closingList[2])
else:
  if time < 10:
    print("You are about " + str("{0:.1f}".format(time)) + " hours from " +
          destination + " " + closingList[3])

#program run
main()
