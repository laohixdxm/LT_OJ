/*
https://leetcode.com/problems/nim-game/

 You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend. 

*/

#include<iostream>
using namespace std;


bool func1(int num);
bool func2(int num);

bool func1(int num) {
	if(num == 4)
		return false;
	else if(num <4)
		return true;

	if(num % 3 == 0) 
		num = num - 3 + 1;
	else 
		num = num - (num % 3) + 1;
	return !func2(num);  
}

bool func2(int num) {
	if(num == 4)
		return false;
	else if(num <4)
		return true;

	if(num % 3 == 0) 
		num = num - 3 + 1;
	else 
		num = num - (num % 3) + 1;
	return !func1(num);  
}

int main(int argc, char *argv[]) {
	//printf(func1(10));
	int n;
	//cout<<true<<endl;
	cin>>n;
	cout<<func1(n)<<endl;
}
















