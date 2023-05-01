import java.io.*;
class BinaryToDecimal
{
	static final int converter = 2;
	//Checking if number is Binary or not
	public static boolean isBinary(int num)
	{
		int dig;
		//Extracting all digits of number
		while(num >= 1)
		{
			//If any digit is not 0 and also not 1 then number is obviously not binary
			dig = num % 10;
			if(dig != 0 && dig != 1)
				return false;
			num /= 10;
		}
		//If it doesnt return up there it is binary
		return true;
	}
	public static int BinToDec(int num)
	{
		//COnverting binary to decimal
		int counter = 0, decNum = 0,digit;
		//Going digit by digit
		while(num >= 1)
		{
			//if digit == 0 we dont add anythinh
			digit = num % 10;
			if(digit == 0)
				decNum += digit;
			//Else we use positional notation to add to the value
			else{
				decNum += Math.pow(converter, counter);
			}
			//Simple digit extraction
			num /= 10;
			//Incrementing position
			++counter;
		}
		return decNum;
	}
	public static void main(String[] args)throws IOException {
		int number;
		BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Enter the binary number Xavier : ");
		try{
		
			//Getting number
			number = Integer.parseInt(rd.readLine());
			//Checking if number is binary
			if(isBinary(number))
			{
				System.out.println(number + " in binary is : " + BinToDec(number));
			}else{
				System.out.println("Number is not binary Xavier !");
			}
		//Simple try catch
		}catch(Exception e)
		{
			System.out.println("Something went wrong : (");
		}

	}
}