
import java.util.*;

/**
 * Write a description of class Calculator here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Calculator
{
    // instance variables - replace the example below with your own
    private int num1;
    private int num2;
    private int sum;
    /**
     * Constructor for objects of class Calculator
     */
    public Calculator()
    {
        // initialise instance variables
        num1 = 0;
        num2 = 0;
        sum = 0;
    }

    /**
     * AcceptInput
     * 
     * 
     * 
     */
    public void AcceptInput()
    {
        // put your code here
        //Assuming we are accepting input from the user
        num1 = 3;
        num2 = 5;
//         ArrayList list = new ArrayList();
//         list.add(3);
//         list.add(5);
//         return list;
    }
    
    /**
     * Calculate
     * 
     * 
     * 
     */
    public int Calcuate()
    {
        // put your code here
        //Assuming we are accepting input from the user
        sum  = num1 + num2;
        return sum;
    }
    
     /**
     * Display
     * 
     * 
     * 
     */
    public int Display()
    {
        return sum;
    }
}
