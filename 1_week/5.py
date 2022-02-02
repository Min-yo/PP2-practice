'''#include <bits/stdc++.h>
using namespace std;

bool isPri(int n){
    for(int i = 2; i*i < n; i++){
        if(n % i == 0)
            return false;
    }
    return true;
}

int main(){
    int n, m;
    cin >> n >> m;
    if(n > 500 || !isPri(n) || m%2 != 0){
        cout << "Try next time!";
    }
    else    
        cout << "Good job!";
    return 0;
}'''
# map function
#x, y = map(int, input().split())
distance, cartridges = [int(x) for x in input().split()] #x, y = [int(x) for x in input().split()]  


flag = True
for x in range(2, distance):
    if(distance % x == 0):
        flag = False
    

if(cartridges%2 == 0 and flag and distance<500):
    print("Good job!")
else:
    print("Try next time!")