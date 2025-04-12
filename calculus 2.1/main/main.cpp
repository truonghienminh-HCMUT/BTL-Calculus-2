#include "iostream"
#include "vector"
#include "string"
#include "cmath"
#include "iomanip"

using namespace std;

const int pi = 3.141592654;

//tao struct cho tung he so va bien
struct Math
{
	char bien;
	int mu = 1;
	double heso = 1;
	string lg; //luong giac
	double gt; //gia tri
};

//dieu kien de bai cho
struct Condition
{
	double phi;
	double r;
};

//tinh tich phan
double inteC(vector<Math> member, Condition condict)
{
	cout << "test";
}


int main()
{
	string problem;
	cout << "Enter function: \n";
	getline(cin, problem);
	int numcon;
	cout << "Enter number of condiction: \n";
	cin >> numcon;
	string tempcon;
	vector<string> condiction;
	for (int i = 0; i < numcon; i++)
	{
		getline(cin, tempcon);
		condiction.push_back(tempcon);
	}
	vector <Math> member;
	Math m;
	bool nega = 0;
	int dem = 0;
	Condition condict = { -1,1,-1,1,1 };

	//doc ham so
		//for (int i = 0; i < problem.length(); i++)
		//{
		//	if (problem[i] == '+' || problem[i] == '-')
		//	{
		//		if (dem != 0) member.push_back(m);
		//		if (problem[i] == '-') nega = 1;
		//	}

		//}

	//doc condition dang so cap
	for (int i = 0; i < condition.length(); i++)
	{
		condict.r = 0;
		string str = "x^2+y^2<=";
		if (condition.find(str) != string::npos)
			for (int i = str.length(); i < condition.length(); i++)
				if (isdigit(condition[i]))
					condict.r = condition[i] - '0' + condict.r * 10;
	}
	condict.r = sqrt(condict.r);
	cout << condict.r;


	//cout << member[0].heso << '*' << member[0].vari << '^' << member[0].power <<endl;
	//cout << member[1].heso << '*' << member[1].vari << '^' << member[1].power;


	cout << fixed << setprecision(10) << inteC(member, condict);



	return 0;
}
