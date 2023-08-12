//Student 1 name: Jason Lam
//Student 2 name: No partner
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
		if (level%2==0)
			return CellValue.X;
		else
			return CellValue.O;
	}
	public void setLevel(int i){
		level=i;
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
		CellValue[][] Board2D=new CellValue[lines][columns];
		int l =0;
		for (int j =0;j<lines;j++){
			for (int k=0;k<columns;k++){
				Board2D[j][k]=board[l];
				l++;
			}
		}
		for(int i=0;i<lines;i++){
			for(int j=0;j<columns;j++){
				if (Board2D[i][j]!=CellValue.EMPTY){
					checkWinVerti(i,j);
					checkWinHori(i,j);
					checkWinDiag1(i, j);
					checkWinDiag2(i, j);
					checkWinDiag3(i, j);
					checkWinDiag4(i, j);
				}
			}
		}


		if (gameState!=GameState.XWIN || gameState!=GameState.OWIN){
			if (level==lines*columns){
				gameState=GameState.DRAW;
			}
		}




		
	}
		
	private void checkWinHori(int i,int j){
		CellValue[][] Board2D=new CellValue[lines][columns];
		int l =0;
		CellValue[] win=new CellValue[lines*columns];
		int wincount=0;
		for (int z =0;z<lines;z++){
			for (int k=0;k<columns;k++){
				Board2D[z][k]=board[l];
				l++;
			}
		}
			for(int y=0;y<sizeWin;y++){
				for(int x=0;x<columns;x++){
					win[x]=Board2D[i][x];
				}
			}
		for (int a=0;a<win.length;a++){
			if (Board2D[i][j]==win[a]){
				wincount++;
				if (wincount==sizeWin){
					if (Board2D[i][j]==CellValue.X){
						gameState=GameState.XWIN;
					}
					else if (Board2D[i][j]==CellValue.O){
						gameState=GameState.OWIN;
					}
				}
			}
			else{
				wincount=0;
			}

		}
		if (wincount==sizeWin){
			if (Board2D[i][j]==CellValue.X){
				gameState=GameState.XWIN;
			}
			else if (Board2D[i][j]==CellValue.O){
				gameState=GameState.OWIN;
			}
		}
		
	}
	private void checkWinVerti(int i,int j){
		CellValue[][] Board2D=new CellValue[lines][columns];
		int l =0;
		CellValue[] win=new CellValue[lines*columns];
		int wincount=0;
		for (int z =0;z<lines;z++){
			for (int k=0;k<columns;k++){
				Board2D[z][k]=board[l];
				l++;
			}
		}
			for(int y=0;y<sizeWin;y++){
				for(int x=0;x<lines;x++){
					win[x]=Board2D[x][j];
				}
			}
		for (int a=0;a<win.length;a++){
			if (Board2D[i][j]==win[a]){
				wincount++;
				if (wincount==sizeWin){
					if (Board2D[i][j]==CellValue.X){
						gameState=GameState.XWIN;
					}
					else if (Board2D[i][j]==CellValue.O){
						gameState=GameState.OWIN;
					}
				}
			}
			else{
				wincount=0;
			}

		}
		
		
	}
	private void checkWinDiag1(int i,int j){
		CellValue[][] Board2D=new CellValue[lines][columns];
		int l =0;
		CellValue[] win=new CellValue[lines*columns];
		int wincount=0;
		for (int z =0;z<lines;z++){
			for (int k=0;k<columns;k++){
				Board2D[z][k]=board[l];
				l++;
			}
		}
			for(int y=0;y<sizeWin;y++){
				for(int x=0;x<lines+columns;x++){
					if (!(x+i>=lines) && !(x+j>=columns)){
						win[x]=Board2D[i+x][j+x];
					}
					
				}
			}
		for (int a=0;a<win.length;a++){
			if (Board2D[i][j]==win[a]){
				wincount++;
				if (wincount==sizeWin){
					if (Board2D[i][j]==CellValue.X){
						gameState=GameState.XWIN;
					}
					else if (Board2D[i][j]==CellValue.O){
						gameState=GameState.OWIN;
					}
				}
			}
			else{
				wincount=0;
			}

		}

			
	}
	
	private void checkWinDiag2(int i,int j){
		CellValue[][] Board2D=new CellValue[lines][columns];
		int l =0;
		CellValue[] win=new CellValue[lines*columns];
		int wincount=0;
		for (int z =0;z<lines;z++){
			for (int k=0;k<columns;k++){
				Board2D[z][k]=board[l];
				l++;
			}
		}
			for(int y=0;y<sizeWin;y++){
				for(int x=0;x<lines;x++){
					if (!(i-x<0) && !(x+j>=columns)){
						win[x]=Board2D[i-x][j+x];
					}
					
				}
			}
		for (int a=0;a<win.length;a++){
			if (Board2D[i][j]==win[a]){
				wincount++;
				if (wincount==sizeWin){
					if (Board2D[i][j]==CellValue.X){
						gameState=GameState.XWIN;
					}
					else if (Board2D[i][j]==CellValue.O){
						gameState=GameState.OWIN;
					}
				}
			}
			else{
				wincount=0;
			}

		}
	}

	private void checkWinDiag3(int i,int j){
		CellValue[][] Board2D=new CellValue[lines][columns];
		int l =0;
		CellValue[] win=new CellValue[lines*columns];
		int wincount=0;
		for (int z =0;z<lines;z++){
			for (int k=0;k<columns;k++){
				Board2D[z][k]=board[l];
				l++;
			}
		}
			for(int y=0;y<sizeWin;y++){
				for(int x=0;x<lines+columns;x++){
					if (!(x+i>=lines) && !(j-x<0)){
						win[x]=Board2D[i+x][j-x];
					}
					
				}
			}
		for (int a=0;a<win.length;a++){
			if (Board2D[i][j]==win[a]){
				wincount++;
				if (wincount==sizeWin){
					if (Board2D[i][j]==CellValue.X){
						gameState=GameState.XWIN;
					}
					else if (Board2D[i][j]==CellValue.O){
						gameState=GameState.OWIN;
					}
				}
			}
			else{
				wincount=0;
			}

		}
	}
	private void checkWinDiag4(int i,int j){
		CellValue[][] Board2D=new CellValue[lines][columns];
		int l =0;
		CellValue[] win=new CellValue[lines*columns];
		int wincount=0;
		for (int z =0;z<lines;z++){
			for (int k=0;k<columns;k++){
				Board2D[z][k]=board[l];
				l++;
			}
		}
			for(int y=0;y<sizeWin;y++){
				for(int x=0;x<lines+columns;x++){
					if (!(i-x<0) && !(j-x<0)){
						win[x]=Board2D[i-x][j-x];
					}
					
				}
			}
		for (int a=0;a<win.length;a++){
			if (Board2D[i][j]==win[a]){
				wincount++;
				if (wincount==sizeWin){
					if (Board2D[i][j]==CellValue.X){
						gameState=GameState.XWIN;
					}
					else if (Board2D[i][j]==CellValue.O){
						gameState=GameState.OWIN;
					}
				}
			}
			else{
				wincount=0;
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
		CellValue[][] Board2D=new CellValue[lines][columns];
		int l =0;
		for (int j =0;j<lines;j++){
			for (int k=0;k<columns;k++){
				Board2D[j][k]=board[l];
				l++;
			}
		}
		String currentturn="",gridhori="";
		String[] rows = new String[lines];
		for (int i = 0; i < rows.length; i++) {
			rows[i]="";
		}
		String result= new String();
		String Final=new String();
		if (level%2==0){
			currentturn="X to play:";
		}
		else
			currentturn="O to play";
		for (int i=0;i<(4*columns-1);i++){
			gridhori+="-";
		}
		for(int i = 0; i<lines;i++){
			for(int j = 0; j<columns-1;j++){
				if (Board2D[i][j]==CellValue.EMPTY){
					rows[i]+="   "+"|";
				}
				else if (Board2D[i][j]==CellValue.X){
					rows[i]+=" X "+"|";
				}
				else if (Board2D[i][j]==CellValue.O){
					rows[i]+=" O "+"|";
				}
				
			}
			if (Board2D[i][columns-1]==CellValue.X){
				rows[i]+=" "+"X"+" ";
			}
			else if (Board2D[i][columns-1]==CellValue.O){
				rows[i]+=" "+"O"+" ";
			}
			else if (Board2D[i][columns-1]==CellValue.EMPTY){
				rows[i]+=" "+ " "+ " ";
			}
			
		}
		for (int i=0;i<rows.length-1;i++){
			result+=rows[i]+ NEW_LINE+gridhori+NEW_LINE;
		}
		result+=rows[rows.length-1]+NEW_LINE;
		if (gameState==GameState.PLAYING){
			Final = result+currentturn;
		}
		else{
			Final = result;
		}
		return Final;
		}
		// your code here
		// use NEW_LINE defined above rather than \n










}


