//Student 1 full name: Jason Lam
//Student 2 full name: N/A
//==================================================


/**
 * Your documentation for this interface ....
 * This class is an interface. It has 5 methods, push which has an object argument, pop which outputs an object, isEmpty which outputs a boolean, peek which outputs an object and size which outputs an int.
 *
 */

public interface Stack {
	//your code here
	public abstract void push(Object O );
    public abstract Object pop();
    public abstract boolean isEmpty();
	public abstract Object peek();
    public abstract int size();
}