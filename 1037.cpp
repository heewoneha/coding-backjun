#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
	int cnt;
	cin >> cnt;

	vector<long long>arr(cnt);

	for (int i = 0;i < cnt;i++) {
		cin >> arr[i];
	}

	sort(arr.begin(), arr.end());
	/*for (int i = 0;i < cnt;i++) {
		cout << arr[i];
	}*/
	long long what = -1; //32bit°¡ int¿´³ª

	what = arr.at(0) * arr.at(cnt - 1);


	cout << what;

	return 0;
}