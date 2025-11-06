class Player:
    """Player class"""
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.choice = None
        self.win_history = []
    
    def make_choice(self, choice):
        """Store player's choice"""
        self.choice = choice
    
    def add_win(self):
        """Add a win to player's record"""
        self.score += 1
        self.win_history.append('W')
    
    def add_loss(self):
        """Add a loss to player's record"""
        self.win_history.append('L')
    
    def add_draw(self):
        """Add a draw to player's record"""
        self.win_history.append('D')
    
    def get_stats(self):
        """Return player statistics"""
        total = len(self.win_history)
        wins = self.win_history.count('W')
        losses = self.win_history.count('L')
        draws = self.win_history.count('D')
        return {
            'total': total,
            'wins': wins,
            'losses': losses,
            'draws': draws,
            'win_rate': (wins / total * 100) if total > 0 else 0
        }


class Computer(Player):
    """Computer player class"""
    def __init__(self):
        super().__init__("Computer")
        self.counter = 0
    
    def generate_choice(self):
        """Generate computer's choice using pseudo-random algorithm"""
        choices = ['Rock', 'Paper', 'Scissors']
        
        # Simple pseudo-random number generation (Linear Congruential Generator variant)
        seed = id(self) + self.counter
        self.counter += 1
        
        # Combine object memory address with counter
        pseudo_random = (seed * 1103515245 + 12345) % 2147483648
        index = pseudo_random % 3
        
        self.choice = choices[index]
        return self.choice


class RockPaperScissorsGame:
    """Rock Paper Scissors Game class"""
    def __init__(self):
        self.player = Player("Player")
        self.computer = Computer()
        self.round_count = 0
        self.game_rules = {
            ('Rock', 'Scissors'): True,
            ('Paper', 'Rock'): True,
            ('Scissors', 'Paper'): True,
            ('Rock', 'Paper'): False,
            ('Paper', 'Scissors'): False,
            ('Scissors', 'Rock'): False,
        }
        self.emoji_map = {
            'Rock': '✊',
            'Paper': '✋',
            'Scissors': '✂️'
        }
    
    def print_banner(self):
        """Display game banner"""
        print("\n" + "="*50)
        print("🎮 ROCK PAPER SCISSORS GAME 🎮".center(50))
        print("="*50)
    
    def get_user_input(self):
        """Get user input"""
        choices = {'1': 'Rock', '2': 'Paper', '3': 'Scissors'}
        
        print("\n" + "-"*30)
        print("Make your choice:")
        print("1. ✊ Rock")
        print("2. ✋ Paper")
        print("3. ✂️  Scissors")
        print("4. 📊 View Statistics")
        print("5. 🚪 Quit Game")
        print("-"*30)
        
        user_input = input("Enter number (1-5): ").strip()
        
        if user_input in choices:
            return choices[user_input]
        elif user_input == '4':
            return 'stats'
        elif user_input == '5':
            return 'quit'
        else:
            return 'invalid'
    
    def determine_winner(self):
        """Determine the winner of the round"""
        p_choice = self.player.choice
        c_choice = self.computer.choice
        
        if p_choice == c_choice:
            return 'draw'
        
        if self.game_rules.get((p_choice, c_choice), False):
            return 'player'
        else:
            return 'computer'
    
    def display_choices(self):
        """Display both players' choices"""
        p_emoji = self.emoji_map[self.player.choice]
        c_emoji = self.emoji_map[self.computer.choice]
        
        print("\n" + "="*40)
        print(f"👤 {self.player.name}: {p_emoji} {self.player.choice}")
        print(f"🤖 {self.computer.name}: {c_emoji} {self.computer.choice}")
        print("="*40)
    
    def display_result(self, winner):
        """Display round result"""
        if winner == 'draw':
            print("\n🤝 It's a DRAW!")
            self.player.add_draw()
            self.computer.add_draw()
        elif winner == 'player':
            print("\n🎉 Congratulations! You WIN!")
            self.player.add_win()
            self.computer.add_loss()
        else:
            print("\n😢 Sorry! Computer WINS!")
            self.player.add_loss()
            self.computer.add_win()
        
        print(f"\n📊 Current Score")
        print(f"   {self.player.name}: {self.player.score} points")
        print(f"   {self.computer.name}: {self.computer.score} points")
    
    def show_statistics(self):
        """Show detailed game statistics"""
        print("\n" + "="*50)
        print("📊 GAME STATISTICS 📊".center(50))
        print("="*50)
        
        p_stats = self.player.get_stats()
        c_stats = self.computer.get_stats()
        
        print(f"\n[{self.player.name} Stats]")
        print(f"  Total Games: {p_stats['total']}")
        print(f"  Wins: {p_stats['wins']}")
        print(f"  Losses: {p_stats['losses']}")
        print(f"  Draws: {p_stats['draws']}")
        print(f"  Win Rate: {p_stats['win_rate']:.1f}%")
        
        print(f"\n[{self.computer.name} Stats]")
        print(f"  Total Games: {c_stats['total']}")
        print(f"  Wins: {c_stats['wins']}")
        print(f"  Losses: {c_stats['losses']}")
        print(f"  Draws: {c_stats['draws']}")
        print(f"  Win Rate: {c_stats['win_rate']:.1f}%")
        
        # Recent 10 games history
        if self.player.win_history:
            print(f"\n[Last 10 Games History]")
            recent = self.player.win_history[-10:]
            record_str = " ".join(recent)
            print(f"  {record_str}")
            print("  (W: Win, L: Loss, D: Draw)")
    
    def play_round(self):
        """Play one round of the game"""
        self.round_count += 1
        
        print(f"\n{'='*50}")
        print(f"🏁 ROUND {self.round_count} 🏁".center(50))
        print('='*50)
        
        # Get user input
        while True:
            user_choice = self.get_user_input()
            
            if user_choice == 'quit':
                return False
            elif user_choice == 'stats':
                self.show_statistics()
                continue
            elif user_choice == 'invalid':
                print("❌ Invalid input! Please try again.")
                continue
            else:
                self.player.make_choice(user_choice)
                break
        
        # Computer makes choice
        self.computer.generate_choice()
        
        # Countdown effect
        print("\nRock...")
        print("Paper...")
        print("Scissors...")
        print("SHOOT!")
        
        # Display results
        self.display_choices()
        winner = self.determine_winner()
        self.display_result(winner)
        
        return True
    
    def show_final_results(self):
        """Display final game results"""
        print("\n" + "="*50)
        print("🏆 GAME OVER! FINAL RESULTS 🏆".center(50))
        print("="*50)
        
        p_stats = self.player.get_stats()
        c_stats = self.computer.get_stats()
        
        print(f"\nTotal Rounds Played: {self.round_count}")
        print(f"{self.player.name}: {p_stats['wins']} wins, {p_stats['losses']} losses, {p_stats['draws']} draws")
        print(f"{self.computer.name}: {c_stats['wins']} wins, {c_stats['losses']} losses, {c_stats['draws']} draws")
        
        if p_stats['wins'] > c_stats['wins']:
            print(f"\n🥇 CONGRATULATIONS! {self.player.name} is the CHAMPION!")
        elif p_stats['wins'] < c_stats['wins']:
            print(f"\n🥈 {self.computer.name} wins this time. Try again!")
        else:
            print("\n🤝 It's a TIE! Well played!")
        
        print("\nThank you for playing! Goodbye! 👋")
    
    def run(self):
        """Run the game"""
        self.print_banner()
        print("\nWelcome to Rock Paper Scissors!")
        print("Challenge the computer and check your statistics anytime!")
        
        try:
            while self.play_round():
                pass
            
            if self.round_count > 0:
                self.show_final_results()
            else:
                print("\nLeaving without playing. Goodbye! 👋")
                
        except KeyboardInterrupt:
            print("\n\nGame interrupted.")
            if self.round_count > 0:
                self.show_final_results()
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            print("Exiting game.")


game = RockPaperScissorsGame()
game.run()