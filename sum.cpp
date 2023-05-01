# include <iostream>
# include <vector>

/*
	Author: LeeTuah
	Program: Sum of 'n' amount of numbers
	For: A League in SuperB events.
*/

// returns the sum of the numbers
int sum(std::vector<int> numbers){
	int sum = 0;
	
	// iterating through all the numbers to get their sum
	for(auto i = numbers.begin(); i != numbers.end(); i++){
		sum += *i;
	}
	
	// returning the sum of the numbers
	return sum;
}

int main(int argc, char *argv[]){
	std::vector<int> numbers;
	int size, num;
	
	std::cout << "How many numbers do you want to add?: ";
	std::cin >> size;
	
	// to verify that the size is positive
	if(size < 0) size *= -1;
	else if(size == 0) size += 1;
	
	// iterating to get all the numbers user wants to sum
	for(int i = 0; i < size; i++){
		std::cout << "Enter your number(#" << i+1 << "): ";
		std::cin >> num;
		numbers.push_back(num);
	}
	
	// calling the function and getting the result
	std::cout << "The sum is " << sum(numbers);
	
	return 0;	
}
