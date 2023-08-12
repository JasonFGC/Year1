//Student 1 name: Jason Lam
//Student 2 name: No partner

/**
 * The class <b>ComputerRandomPlayer</b> is the class that controls the computer's plays.
 * 
 * 
 */

import java.util.*;
public class ComputerRandomPlayer implements Player {
	//generate random position at an empty cell!!
	//call game.play(position)
	public void play(TicTacToeGame game){
		if (game.getGameState()==GameState.PLAYING){
			System.out.println("Player two's turn.");
			Random rng = new Random();
			int x=rng.nextInt(game.getColumns()*game.getLines())-1;
			if (game.getGameState()==GameState.PLAYING){
				System.out.println("O to play: "+ (x+1));
			}
			game.play(x);
		}
		else{
			System.out.println("Error. Game is not playable.");
		}
	}

}

