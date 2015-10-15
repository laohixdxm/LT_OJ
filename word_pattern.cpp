/*
https://leetcode.com/problems/word-pattern/
*/

#include <iostream>
#include <string>
#include <unordered_map>
#include <sstream>
#include <iterator>
#include <vector>

using namespace std;

//unordered_map<char, string> table;

bool wordPattern(string pattern, string str) {
	
	unordered_map<char, string> table;
		
	istringstream buf(str);
	istream_iterator<string> beg(buf), end;
	vector<string> tokens(beg, end);

	cout<<pattern.length()<<tokens.size()<<endl;
	if(pattern.length() != tokens.size()) 
		return false;

	for(int i=0;i<pattern.length();i++) {
		//table[pattern[i]] = tokens[i];
		pair<char, string> cur_pair = {pattern[i], tokens[i]};
		cout<<pattern[i]<<tokens[i]<<endl;
		cout<<table.size()<<endl;

		if(table.count(pattern[i])) {
			//cout<<table[0]<<endl;
			//return 0;
			
			if(tokens[i] == table[pattern[i]])
				continue;
			else
				return false;
		}	
		else {
			for(int j=0; j<i; j++)
				if(table[[pattern[i]]] == tokens[i])
					return false;
			//if(token[i] not in values)
				//table[pattern[i]] = tokens[i];//insert	
			table.insert(cur_pair);
			//cout<<table['a']<<endl;
		}					
	}
	return true;	 

}


int main() {
/*	
	bool res= wordPattern("abba", "dog cat cat dog");
	bool res2= wordPattern("abba", "dog cat cat fish"); //different value for same key
	bool res3= wordPattern("aaaa", "dog cat cat dog");
	bool res4= wordPattern("abba", "dog dog dog dog"); //same value for different key
	bool res5= wordPattern("jquery", "jquery"); //same value for different key
*/

	bool res6= wordPattern("deadbeef", "d e a d b e e f"); //same value for different key

//	for(int i=0;i<tokens.size();i++)
//		cout<<tokens[i]<<endl;
/*
	cout<<res<<endl;
	cout<<res2<<endl;
	cout<<res3<<endl;
	cout<<res4<<endl;
	cout<<res5<<endl;
*/
	cout<<res6<<endl;

	//for(int i=0; i<table.size(); i++)
	cout<<table.size()<<endl;

		cout<<table['d']<<endl;
		cout<<table['e']<<endl;
		cout<<table['a']<<endl;
		//cout<<table['d']<<endl;
		cout<<table['b']<<endl;
		//cout<<table['d']<<endl;
		//cout<<table['d']<<endl;
		cout<<table['f']<<endl;

	//cout<<true<<endl;

}