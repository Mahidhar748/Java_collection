package Java_collection;

public class First {
public static int reverseData(int data){
    int answer = 0;
    while(data !=0){
        answer = answer*10+data%10;
        data/=10;
   }
    return answer;
}
    public static void main(String[] args) {
        System.out.println(reverseData(5783789));
    
    }
}
