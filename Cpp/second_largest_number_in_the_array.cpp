// Problem statement:-
// You have been given an array/list 'ARR' of integers. Your task is to find the second largest element present in the 'ARR'.

// Note:
// a) Duplicate elements may be present.
// b) If no such element is present return -1.

// Example:-
// Input: Given a sequence of five numbers 2, 4, 5, 6, 8.
// Output:  6

#include <bits/stdc++.h> 
#include <iostream>
#include <vector>
int findSecondLargest(int n, vector<int> &arr)
{
    if( n<2){
        return -1;
    }
    // int largest= INT_MIN ;
    int largest = arr[0];
    int secondlargest = INT_MIN;  // INT_MIN assigns the lowest integer value to the variable possible in int range of cpp.
    for ( int i =1; i<n; i++)
    {
        if (arr[i]>largest){
            secondlargest = largest;
            largest= arr[i];
        }    
        else{
            if( arr[i]>secondlargest && arr[i]<largest){
                secondlargest= arr[i];
            }
        }
    }
    if (secondlargest == INT_MIN){
        return -1;
    }

    return secondlargest;
}
