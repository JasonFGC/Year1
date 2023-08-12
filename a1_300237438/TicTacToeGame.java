import javax.swing.border.EmptyBorder;

/**
 * The class <b>TicTacToeGame</b> is the
 * class that implements the Tic Tac Toe Game.
 * It contains the grid and tracks its progress.
 * It automatically maintain the current state of
 * the game as players are making moves.
 *
 * @author Guy-Vincent Jourdan, University of Ottawa
 */
public class TicTacToeGame {

   /**
	* The board of the game, stored as a single array.
	*/
	private CellValue[] board;


   /**
	* level records the number of rounds that have been
	* played so far. Starts at 0.
	*/
	private int level;

   /**
	* gameState records the current state of the game.
	*/
	private GameState gameState;


   /**
	* lines is the number of lines in the grid
	*/
	private final int lines;

   /**
	* columns is the number of columns in the grid
	*/
	private final int columns;


   /**
	* sizeWin is the number of cell of the same type
	* that must be aligned to win the game. 
	* For simplicity, it will be always 3 in this assignment.
	*/
	private final int sizeWin; 


   /**
	* default constructor, for a game of 3x3, which must
	* align 3 cells
	*/
	public TicTacToeGame(){  
		// your code here
		level =0;
		lines=3;
		columns=3;
		sizeWin=3;
		gameState=GameState.PLAYING;
		board=new CellValue[lines*columns];
		for (int i =0;i<9;i++){
			board[i]=CellValue.EMPTY;
		}
	}

   /**
	* constructor allowing to specify the number of lines
	* and the number of columns for the game. 3 cells must
	* be aligned.
   	* @param lines
    *  the number of lines in the game
    * @param columns
    *  the number of columns in the game
  	*/
	public TicTacToeGame(int lines, int columns){
		// your code here
		level =0;
		this.lines=lines;
		this.columns=columns;
		sizeWin=3;
		board=new CellValue[(lines*columns)];
		for (int i =0;i<(lines*columns);i++){
			board[i]=CellValue.EMPTY;
		}
		gameState=GameState.PLAYING;
	}

   /**
	* constructor allowing to specify the number of lines
	* and the number of columns for the game, as well as
	* the number of cells that must be aligned to win.
   	* @param lines
    *  the number of lines in the game
    * @param columns
    *  the number of columns in the game
    * @param sizeWin
    *  the number of cells that must be aligned to win.
  	*/
	public TicTacToeGame(int lines, int columns, int sizeWin){
		// your code here
		level =0;
		this.lines=lines;
		this.columns=columns;
		this.sizeWin=sizeWin;
		board=new CellValue[(lines*columns)];
		for (int i =0;i<(lines*columns);i++){
			board[i]=CellValue.EMPTY;
		}
		gameState=GameState.PLAYING;
	}



   /**
	* getter for the variable lines
	* @return
	* 	the value of lines
	*/
	public int getLines(){
		// your code here
		return lines;
	}

   /**
	* getter for the variable columns
	* @return
	* 	the value of columns
	*/
	public int getColumns(){
		// your code here
		return columns;
	}

   /**
	* getter for the variable level
	* @return
	* 	the value of level
	*/
	public int getLevel(){
		// your code here
		return level;
	}


   /**
	* getter for the variable gameState
	* @return
	* 	the value of gameState
	*/
	public GameState getGameState(){
		// your code here
		return gameState;
	}

   /**
	* getter for the variable sizeWin
	* @return
	* 	the value of sizeWin
	*/
	public int getSizeWin(){
		// your code here
		return sizeWin;
	}

   /**
	* returns the cellValue that is expected next,
	* in other word, which played (X or O) should
	* play next.
	* This method does not modify the state of the
	* game.
	* @return
    *  the value of the enum CellValue corresponding
    * to the next expected value.
  	*/
	public CellValue nextCellValue(){
		// your code here
		if (level==0)
			return CellValue.X;
		else if (level%2==0)
			return CellValue.X;
		else
			return CellValue.O;
	}

   /**
	* returns the value  of the cell at
	* index i.
	* If the index is invalid, an error message is
	* printed out. The behaviour is then unspecified
   	* @param i
    *  the index of the cell in the array board
    * @return
    *  the value at index i in the variable board.
  	*/
	public CellValue valueAt(int i) {
		if (i>board.length || i<0){
			System.out.println("Error. Invalid index.");
			return CellValue.EMPTY;
		}
		else
			return board[i];
		// your code here
	}

   /**
	* This method is called by the next player to play
	* at the cell  at index i.
	* If the index is invalid, an error message is
	* printed out. The behaviour is then unspecified
	* If the chosen cell is not empty, an error message is
	* printed out. The behaviour is then unspecified
	* If the move is valide, the board is updated, as well
	* as the state of the game.
	* To faciliate testing, it is acceptable to keep playing
	* after a game is already won. If that is the case, the
	* a message should be printed out and the move recorded.
	* the  winner of the game is the player who won first
   	* @param i
    *  the index of the cell in the array board that has been
    * selected by the next player
  	*/
	public void play(int i) {
		if (i>=board.length || i<0)
			System.out.println("Error. Invalid Index");
		else if (board[i]!=CellValue.EMPTY)
			System.out.println("Error. This space is already taken.");
		else if (board[i]==CellValue.EMPTY && gameState==GameState.PLAYING){
			if (nextCellValue()==CellValue.X){
				board[i]=CellValue.X;
				level++;
				setGameState(i);
		}
			else if (nextCellValue()==CellValue.O){
				board[i]=CellValue.O;
				level++;
				setGameState(i);
			}
		}
		else if (gameState==GameState.XWIN){
			System.out.println("X has won the game. Move has been recorded.");
			level++;
		}
		else if (gameState==GameState.OWIN){
			System.out.println("O has won the game. Move has been recorded.");
			level++;
		}
		else if (gameState==GameState.DRAW)
			System.out.println("The game is a draw.");

		// your code here

	}


   /**
	* A helper method which updates the gameState variable
	* correctly after the cell at index i was just set.
	* The method assumes that prior to setting the cell
	* at index i, the gameState variable was correctly set.
	* it also assumes that it is only called if the game was
	* not already finished when the cell at index i was played
	* (the the game was playing). Therefore, it only needs to
	* check if playing at index i has concluded the game
	* So check if 3 cells are formed to win.
//   	* @param i
    *  the index of the cell in the array board that has just
    * been set
  	*/

	private void setGameState(int index){
		// your code here
		if (board[index] == CellValue.X){
			if (((board[0]==CellValue.X)&&(board[1]==CellValue.X)&&(board[2]==CellValue.X))||((board[0]==CellValue.X)&&(board[3]==CellValue.X)&&(board[6]==CellValue.X))||((board[0]==CellValue.X)&&(board[4]==CellValue.X)&&(board[8]==CellValue.X))|| ((board[3]==CellValue.X)&&(board[4]==CellValue.X)&&(board[5]==CellValue.X)) || ((board[6]==CellValue.X)&&(board[7]==CellValue.X)&&(board[8]==CellValue.X))|| ((board[1]==CellValue.X)&&(board[4]==CellValue.X)&&(board[7]==CellValue.X)) || ((board[2]==CellValue.X)&&(board[5]==CellValue.X)&&(board[8]==CellValue.X)) || ((board[2]==CellValue.X)&&(board[4]==CellValue.X)&&(board[6]==CellValue.X))){
				gameState=GameState.XWIN;
			}
			else if ((board[0]!=CellValue.EMPTY)&&(board[1]!=CellValue.EMPTY)&&(board[2]!=CellValue.EMPTY)&&(board[3]!=CellValue.EMPTY)&&(board[4]!=CellValue.EMPTY)&&(board[5]!=CellValue.EMPTY)&&(board[6]!=CellValue.EMPTY)&&(board[8]!=CellValue.EMPTY)){
				gameState=GameState.DRAW;
			}
		}
		else if (board[index]==CellValue.O){
			if (((board[0]==CellValue.O)&&(board[1]==CellValue.O)&&(board[2]==CellValue.O))||((board[0]==CellValue.O)&&(board[3]==CellValue.O)&&(board[6]==CellValue.O))||((board[0]==CellValue.O)&&(board[4]==CellValue.O)&&(board[8]==CellValue.O))|| ((board[3]==CellValue.O)&&(board[4]==CellValue.O)&&(board[5]==CellValue.O)) || ((board[6]==CellValue.O)&&(board[7]==CellValue.O)&&(board[8]==CellValue.O))|| ((board[1]==CellValue.O)&&(board[4]==CellValue.O)&&(board[7]==CellValue.O)) || ((board[2]==CellValue.O)&&(board[5]==CellValue.O)&&(board[8]==CellValue.O)) || ((board[2]==CellValue.O)&&(board[4]==CellValue.O)&&(board[6]==CellValue.O)))	{
				gameState=GameState.OWIN;
			}	
			else if ((board[0]!=CellValue.EMPTY)&&(board[1]!=CellValue.EMPTY)&&(board[2]!=CellValue.EMPTY)&&(board[3]!=CellValue.EMPTY)&&(board[4]!=CellValue.EMPTY)&&(board[5]!=CellValue.EMPTY)&&(board[6]!=CellValue.EMPTY)&&(board[8]!=CellValue.EMPTY)){
				gameState=GameState.DRAW;
			}
		}
		}
		
		
		

	



	final String NEW_LINE = System.getProperty("line.separator");
	// returns the OS dependent line separator

   /**
	* Returns a String representation of the game matching
	* the example provided in the assignment's description
	*
   	* @return
    *  String representation of the game
  	*/

	public String toString(){
		
		String currentturn="",gridhori="",finished="";
		String[] grid = new String[columns*lines];
		String[] rows = new String[columns];
		if (level%2==0){
			currentturn="X to play:";
		}
		else
			currentturn="O to play";
		for (int i=0;i<(4*columns-1);i++){
			gridhori+="-";
		}
		for (int i=0;i<columns*lines;i++){
			if(board[i]==CellValue.X){
				grid[i]="X";
			}
			else if (board[i]==CellValue.O){
				grid[i]="O";
			}
			else if (board[i]==CellValue.EMPTY){
				grid[i]=" ";
			}
		}
		rows[0]=" "+grid[0]+" | "+grid[1]+" | "+grid[2];
		rows[1]=" "+grid[3]+" | "+grid[4]+" | "+grid[5];
		rows[2]=" "+grid[6]+" | "+grid[7]+" | "+grid[8];
		
		finished=rows[0]+ NEW_LINE + gridhori + NEW_LINE + rows[1] + NEW_LINE + gridhori + NEW_LINE + rows[2];
		return finished+NEW_LINE+currentturn;
	}
		// your code here
		// use NEW_LINE defined above rather than \n
		

}


