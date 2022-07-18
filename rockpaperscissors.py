import random 
import time
import cmd

class RockPaperScissors(cmd.Cmd):
    intro = """
    Welcome to Rock Paper Scissors! 
    
    To challenge a computer, begin by typing 'start' and then by choosing rock, paper or scissors.
    
    To leave, type 'exit'. 
    """
    
    prompt = "Rock, Paper, Scissors "
    
    def loading(self):
        print("REAAAAADY?")
        time.sleep(3)
        print("Rock")
        time.sleep(0.5)
        print("Paper")
        time.sleep(0.5)
        print("Scissors")
        time.sleep(0.5)
        print("Shoot!")
        time.sleep(0.5)
    
    def celebration(self):
        print("Hooray!!!")
        time.sleep(1)
        for i in range(3):
            print("Clap")
            time.sleep(0.2)
            print("Clap Clap")
            time.sleep(0.2)
            print("Clap Clap Clap")
            time.sleep(0.2)
            print("Clap Clap")
            time.sleep(0.2)
        print("Clap")
        print("Press 'start' to play again.")
            
    def loss(self):
        print("W")
        time.sleep(0.1)
        for i in range(10):
            print("A")
            time.sleep(0.1)
        print("H")
        time.sleep(0.5)
        print(":(")
        print("Press 'start' to play again.")
            
    def gunloss(self):
        time.sleep(0.1)
        print("NO TIME TO EXPLAIN, GRAB A CACTUS")
        time.sleep(0.1)
        for i in range(10):
            print("Pew")
            time.sleep(0.1)
            print("Pew Pew")
            time.sleep(0.1)
        print("Pew")
        print("Are you still there?")
        answer = input("Y/N ")
        if answer == "Y":
            print("Phew... let's play again?")
            print("Press 'start' to play again.")

        else:
            print("RIP :(")
            time.sleep(1)
            print("Moment of silence as we quit the program...")
            time.sleep(3)
            print("See ya later alligator.")
            return True
                
    def computerSelect(self):
        computerSelect = ""
        selection = ["Rock", "Paper", "Scissors", "Gun"]
        choice = random.choice(selection)
        computerSelect += choice 
        return computerSelect 

    def do_start(self, args):
        """ Start the game."""
        playerchoice = input("Choose rock, paper or scissors: ").title()
        computerchoice = self.computerSelect()
        selection = ["Rock", "Paper", "Scissors", "Gun"]
        
        if playerchoice not in selection:
            return TypeError
        
        def display():
            time.sleep(1)
            print("You chose: " + playerchoice)
            time.sleep(1)
            print("Computer chose: " + computerchoice)
            time.sleep(1)
        
        self.loading()
        
        if playerchoice == computerchoice:
            if (playerchoice and computerchoice) == "Gun":
                display()
                print("Well well well partner, seems like we got ourselves into a little stand off")
                time.sleep(1)
                print("One")
                time.sleep(1)
                print("Two")
                time.sleep(1)
                print("Three!")
                time.sleep(0.1)
                self.gunloss()
            else:
                display()
                print(f"Both players selected {playerchoice}. It's a tie!")
            
        elif playerchoice == "Rock":
            if computerchoice == "Scissors":
                display()
                print("Rock smashes scissors! You win!")
                self.celebration()
            elif computerchoice == "Paper":
                display()
                print("Paper covers rock! You lose.")
                self.loss()
            elif computerchoice == "Gun":
                display()
                self.gunloss()
                
                
        elif playerchoice == "Paper":
            if computerchoice == "Rock":
                display()
                print("Paper covers rock! You win!")
                self.celebration()
            elif computerchoice == "Scissors":
                display()
                print("Scissors cuts paper! You lose.")
                self.loss()
            elif computerchoice == "Gun":
                display()
                self.gunloss()
                
        elif playerchoice == "Scissors":
            if computerchoice == "Paper":
                display()
                print("Scissors cuts paper! You win!")
                self.celebration()
            elif computerchoice == "Rock":
                display()
                print("Rock smashes scissors! You lose.")
                self.loss()
            elif computerchoice == "Gun":
                display()
                time.sleep(1)
                self.gunloss()
                
        elif playerchoice == "Gun":
            selection = ["Rock", "Paper", "Scissors", "Gun"]
            display()
            if computerchoice in selection:
                time.sleep(1)
                print("BANG!")
                time.sleep(0.5)
                print("Last one standing wins. You win partner.")
    
    def do_exit(self, args):
        """Quits the program."""
        print("Exiting...")
        time.sleep(1)
        print("See ya later alligator.")
        return True
    
    def onecmd(self, line):
        try:
            return super().onecmd(line)
        except:
            # display error message
            return print("Does not exist. Try again.") #

if __name__ == '__main__':
    RockPaperScissors().cmdloop()
    
    
                

