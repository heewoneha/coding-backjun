#include<iostream>
#include<string>
#include<stack>
using namespace std;
bool what(string ps) {
	stack<char> st;

	int num = ps.size();

	char c;
	for (int i = 0;i < num;i++) {
		c = ps[i];

		if (c == '(') {
			st.push(c);
		}

		else if (c == ')') {
			if (!st.empty()) {
				st.pop();
			}
			else {
				return false;
			}
		}
	}

	if (!st.empty()) {
		return false;
	}
	else {
		return true;
	}
}

int main() {
	int howMany = 0;
	cin >> howMany;
	string ps;
	while (howMany--) {
		cin >> ps;

		if (what(ps) == true) {
			cout << "YES" << endl;
		}

		else {
			cout << "NO" << endl;
		}

		ps="";
	}

	return 0;
}