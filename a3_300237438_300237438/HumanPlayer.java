//Student 1 full name: Jason Lam
//Student 2 full name: N/A
//==================================================

/**
 * The class <b>HumanPlayer</b> is the class that controls the human's plays.
 * ... some more details here
 * this class is an implementation of the player interface. It has 2 methods, one to ask the player for an input and one to get the score for the user.
 * It is used in the HanoiTower class when it calls play for each individual player. 
 * 
 * 
 */

import java.io.Console;
public class HumanPlayer implements Player {
	int score=0;
	public void play(HanoiTowerGame game){
	// your code here
		while (game.getGameState()==GameState.PLAYING){
			Console console = System.console();
			System.out.println(game.toString());
			System.out.println("Enter the source and the destination towers each on a single line:");
			String input=console.readLine();
			int i,j;
			if (input.matches("^[1-3]$")){
				i = Integer.parseInt(input)-1;
			}
			else{
				System.out.println("invalid input");
				continue;
			}
			String input2=console.readLine();
			if (input2.matches("^[1-3]$")){
				j = Integer.parseInt(input2)-1;
			}
			else{
				System.out.println("Invalid input!!!");
				continue;
			}
			game.play(i,j);
		} 
		if(game.getGameState()==GameState.WINNER){
			score++;
			System.out.println(game.toString());
		}
	}
	public int getScore(){
		return score;
	}
}