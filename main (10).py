#2.2 implement a class called player that represents a cricket player the player class stood have a method called play()which print "The player is playing cricket".Derive two classes,Batsman and Bowler, from the player class.override the play method in each derived class to print "The batsman is betting" and the bowler is bowling", respectively brittiya program to create objects of both the Batsman and bowler classes and call the play()method for each subject.
# Define the player class 
  class player:
    def play(self):
      print ("The player is playing cricket.")
# Define the Batsman class derived  from player
class Batsman(player):
  def play(self):
      print ("The Batsman is batting.")
# Define the Bowler class,derived from player
 class Bowler (player):
   def play (self):
     print ("The Bowler is Bowling.")
# create objects to Batsman and Bowler classes 
  batsman=Batsman ()
  bowlar=Bowlar()
# call the play ()method for each object 
  batman.play()
Bowler.play()


    
      