//Student 1 full name: Jason Lam
//Student 2 full name: N/A
//==================================================



/**
 * Your documentation for this class ....
 * This class is the entire game. It sets up the towers with the appropriate disk amount, then takes inputs from the user to play the game.  It checks if the user wins after
 * every play. It also can take the information and output it in a string for the user to better understand. 
 *
 */

import java.lang.Math;
import java.lang.reflect.Constructor;

public class HanoiTowerGame {

	//This will point to the array of three towers (type of towers LinkedStack)
	private Stack[] towerValues;  
	
	//your code here
	private int level;
	private int maxMoves;
	private GameState gameState;
	private int disks;

	public HanoiTowerGame(){
		this(3);
	}
	public HanoiTowerGame(int disks){
		level=0;
		gameState=GameState.PLAYING;
		maxMoves=2*((int)Math.pow(2,disks) -1);
		this.disks=disks;
		towerValues= new Stack[3];
		for (int i = 0; i < towerValues.length; i++) {
			towerValues[i]=new LinkedStack();
		}
		for (int i = disks; i >=1; i--) {
			towerValues[0].push(i);
		}
		
	}

	// all methods should be documented: purpose of the method, input, and output
	// and where it is used in the assignment

	//This method gets the level for the user. This outputs the amount of moves that the user has done since they started playing the game. It outputs an integer.
	public int getLevel(){
		return level;
	}
	//This method gets the max amount of levels for the user. This is used to check whether the user has exhausted the maximum amount of moves that are allowed.
	public int maxLevels(){
		return maxMoves;
	}
	//This method gets the amount of disks that are in the game. The amount of disks determine how many moves are allowed to finish the game. 
	public int getDisks(){
		return disks;
	}
	//This method gets the current gamestate of the game. It is usesd in HumanPlayer to check the gamestate so that it can track the score for each player. 
	public GameState getGameState(){
		return gameState;
	}
	//This method plays a move in the game. This is used in HumanPlayer to get the inputs from and to and uses them to calculate scores and determine whether the game should be played or not.
	public void play(int from,int to){
		Object disk1=towerValues[from].peek();
		int disk1Value=(int)towerValues[from].peek();
		int disk2Value=(int)towerValues[to].peek();
		if (disk2Value==-1){
			disk2Value=disks+1;
		}		
		if (disk1==null){
			System.out.println("There is/are no disks at tower "+(String)disk1+"!!");
		}
		else{
			if (disk1Value>disk2Value){
				System.out.println("Invalid move!!");
			}
			else{
				 level++;
				 towerValues[from].pop();
				 towerValues[to].push(disk1);
				 checkWinner();
			}
		}
	}
	//This is the win condition. It checks whether the amount of disks in the third tower is the same as the amount of disks you start the game with. We dont need to check order because the play method doesnt let you place them out of order. This is used in the play method everytime a successful play is made.
	public void checkWinner(){
		
		if ((towerValues[2].size()==disks) && (level<=maxMoves)){
			gameState=GameState.WINNER;
		}
		else if (level==maxMoves){
			gameState=GameState.LOSER;
		}
	}
	//This is the method that takes the whole game and outputs it in a way that allows the user to properly see the information. It's used in the HumanPlayer class to output the towers and how many moves have been used.
	public String toString(){
		String s = "";
		LinkedStack[] towerCopies = new LinkedStack[3];
		for (int i = 0; i < towerCopies.length; i++) {
			towerCopies[i] = ((LinkedStack)towerValues[i]).copy();
		}

		for (int i = 0; i < towerCopies.length; i++) {
			s += "Tower " + (i+1) + Utils.NEW_LINE;
			int j = disks;
			while (j > towerCopies[i].size() ) {
				s += Utils.NEW_LINE;
				j -= 1;
			}
			while (!towerCopies[i].isEmpty()) {
				int temp = (int)towerCopies[i].pop() ;
				s += new String(new char[temp]).replace("\0", "-") + Utils.NEW_LINE;
			}
		}

		if (level==0){
			s+="Your goal is to move " +disks+" disks from tower 1 to 3 \n"+"Only one simple rule: no large disk on the top of a smaller one!";
		}
		else{
			s+="Moves played "+level+" Max "+maxMoves;
		}
		if (gameState==GameState.WINNER){
			s+=Utils.NEW_LINE+"You did it within the allowed number of moves!";
		}
		else if (gameState==GameState.LOSER){
			s+=Utils.NEW_LINE+"You finished the allowed number of moves!";
		}
		return s;
	}
}
