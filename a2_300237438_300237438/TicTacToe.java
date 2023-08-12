import java.util.Random;
//Student 1 name: Jason Lam
//Student 2 name: No partner

/**
 * The class <b>TicTacToe</b> is the class that implements the actual Tic Tac
 * Toe game, where it
 * controls the human and computer activity and prints the result of the game at
 * the end. It also
 * asks the player if he/she wants to continue playing once this game is over.
 * 
 * 
 */

public class TicTacToe {

    /**
     * <b>main</b> of the application. Creates the instance of GameController
     * and starts the game. If two parameters line and column
     * are passed, they are used.
     * Otherwise, a default value is used. Defaults values are also
     * used if the paramters are too small (less than 2).
     * 
     * @param args
     *             command line parameters
     */
    public static void main(String[] args) {
        StudentInfo.display();
        
		
		//default values used if args are not there:
        int lines = 3;
        int columns = 3;
        int win = 3;

        //change lines, columns and win based on the args values
        if (args.length >= 2) {
            lines = Integer.parseInt(args[0]);
            if(lines<2){
                System.out.println("Invalid argument, using default...");
                lines = 3;
            }
            columns = Integer.parseInt(args[1]);
            if(columns<2){
                System.out.println("Invalid argument, using default...");
                columns = 3;
            }
        }
		
        if (args.length > 3){
            System.out.println("Too many arguments. Only the first 3 are used.");
        } 

		//define an array (say p) of two players (use interface playe for the refernce)
		// The first playe is an object of type HumanPlayer and 
		// the second player is an object of type  ComputerRandomPlayer()
		Player[] p = new Player[] {new HumanPlayer(), new ComputerRandomPlayer()};
        TicTacToeGame game = new TicTacToeGame(lines, columns,win);
		//choose player randomly (p[0] or p[1]) 
		Random rng = new Random();
        int x = rng.nextInt(2);
        int starter=0;
        if (x==0){
            starter=0;
        }
        else if (x==1){
            starter=1;
        }
        
		// create a refernce to an object of type TicTacToeGame
        
		// loop until the input is not 'y' 
		do {
            game=new TicTacToeGame(lines,columns,win);
            if (starter==0){
                game.setLevel(0);
                starter=1;
                p[0].play(game);
            }
            else if (starter==1){
                game.setLevel(1);
                starter=0;
                p[1].play(game);
            }
		     // create object for TicTacToeGame
		     // for loop that prints who's turn it is, the board, and who is to play, until
                // the game ends
            while(game.getGameState()==GameState.PLAYING){
                if (game.getLevel()%2==0){
                    p[0].play(game);
                }
                else {
                    p[1].play(game);
            }
            System.out.println(game);
            if (game.getGameState()==GameState.OWIN){
                System.out.println("OWIN.");
            }
            else if (game.getGameState()==GameState.XWIN){
                System.out.println("XWIN.");
            }
            else if (game.getGameState()==GameState.DRAW){
                System.out.println("DRAW.");
            }
           System.out.println("Play again (Y) ?: ");
        }
		     // prints result of game and ask if you want to play again
		}while(Utils.console.readLine().compareToIgnoreCase("y") == 0);


    }
}
