import java.util.*;
import java.lang.*;
import java.io.*;
 
/* Name of the class has to be "Main" only if the class is public. */
class Ideone
{
	public static int linerSearch(int[] arr, int key){
 
        int size = arr.length;
        for(int i=0;i<size;i++){
            if(arr[i] == key){
                return i;
            }
        }
        return -1;
    }
	public static void main (String[] args) throws java.lang.Exception
	{
		 int[] arr1= {1,2,3,4,5,6,7,8,9,10,11};
        int searchKey = 14;
        System.out.println("Key "+searchKey+" found at index: "+linerSearch(arr1, searchKey));
        int[] arr2= {123,445,421,595,2134,41,304,190};
        searchKey = 421;
        System.out.println("Key "+searchKey+" found at index: "+linerSearch(arr2, searchKey));
 
}
}