//Student 1 full name: Jason Lam
//Student 2 full name: N/A
//==================================================


/**
 * Your documentation for this class ....
 * This class is a linked structure and implements stack. It allows you to push objects in, pop objects out, peek objects, and check the size and whether it is empty or not. 
 * It is used frequently in HanoiTowerGame as all the towers are linked by this. 
 *
 */

public class LinkedStack implements Stack {
    public static class Elem {
        private Object value;
        private Elem next;
        
        private Elem( Object value, Elem next ) {
            this.value = value;
            this.next = next;
        }
        public void setValue(Object value){
            this.value=value;
        }
        public void setNext(Elem next){
            this.next=next;
        }
        public Object getValue(){
            return value;
        }
        public Elem getNext(){
            return next;
        }
    }
        private int count;
        private Elem top;
        LinkedStack(){
            top=null;
        }
        //This method checks if the tower is empty. It is used in play method to ensure you are not trying to take from a tower that is empty.
        public boolean isEmpty(){
            return top==null;
        }
        //This method puts an object into the stack. If the stack is empty, it sets the value to the object and the next value to null(meaning its empty). If it is not full, it sets the next to the previous top. 
        public void push(Object O){
            if(top==null){
                top=new Elem(O,null);
            }
            else{
                Elem temp = new Elem (O,top);
                top=temp;
            }
            count++;
        }
        //This method takes the top out of the stack. If the stack is empty, it does not work and returns null. If it has something inside, it takes it out and outputs it.
        public Object pop(){
            Elem temp;
            if(isEmpty()){
                return null;
            }
            temp=top;
            top=top.getNext();
            temp.setNext(null);
            count--;
            return temp.getValue();
        }
        //This method looks at the top of the stack. If the stack is empty, it outputs -1 which allows the play method to function properly. If not, it will look at the top without removing it.
        public Object peek(){
            if (isEmpty()==true){
                return -1;
            }
            return top.getValue();
        }
        //This method returns the size of the stack. It is done by increasing count every successful push and decreasing count every successful pop.
        public int size(){
            return count;
        }
        //This meethod is used to copy a stack. It is used in toString to properly display the contents of the stack without messing up the original stack.
        public LinkedStack copy() {
            LinkedStack copy = new LinkedStack();
            LinkedStack copy2 = new LinkedStack();;
            while (!this.isEmpty()) {
                Object e = this.pop();
                copy2.push(e);
            }
            
            while (!copy2.isEmpty()) {
                Object e = copy2.pop();
                this.push(e);
                copy.push(e);
            }
            return copy;
        }





}