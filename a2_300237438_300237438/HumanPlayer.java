//Student 1 name: Jason Lam
//Student 2 name: No Partner
/**
 * The class <b>HumanPlayer</b> is the class that controls the human's plays.
 * 
 * 
 */
import java.io.Console;
public class HumanPlayer implements Player {
	//read a position to play from the console and call 
	// game.play(position): if the level was advanced after the call, then finish, otherwise repeat and get another position
	public void play(TicTacToeGame game){
		if (game.getGameState()==GameState.PLAYING){
			Console console = System.console();
			System.out.println("Player one's turn.");
			try{
				System.out.println(game.toString());
				String input=console.readLine();
				int i = Integer.parseInt(input)-1;
				game.play(i);
			} 
			catch (NumberFormatException e){
				System.out.println("Invalid input. Input must be a number between 0 and "+ game.getColumns()*game.getLines()+".");
			}
		}
		else{
			System.out.println("Error. Game is not playable.");
		}
	}
}