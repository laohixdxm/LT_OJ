/*
https://leetcode.com/problems/move-zeroes/
*/

#include<iostream>
using namespace std;

#include <vector>

void moveZeroes(vector<int> & nums) {

	int i, j =0;
	while(nums[i]!=0) //i index zero
			i++;
	j = i;	
	while( (nums[j]==0) || (i >=j) ) // j index non-zero
			j++;

	while( (i<nums.size()) && (j<nums.size()) ) 
	{
		int tmp;
		//swap(nums[i], nums[j]);
		tmp = nums[i];
		nums[i] = nums[j];
		nums[j] = tmp;

		while(nums[i]!=0)
			i++;
		while( (nums[j]==0) || (i >=j) )
			j++;
	}

	//for(int i=0;i<nums.size(); i++)
	//	cout<<nums[i]<<endl;
		
} 

int main() {

	vector<int> v2;
	//v2 = {0,1,0,3,12};
	v2 = {0,1,0,3,12, 0,0, 4, 5};

	moveZeroes(v2);
	
	for(int i=0;i<v2.size(); i++)
		cout<<v2[i]<<endl;

}