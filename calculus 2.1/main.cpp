#include "iostream"
#include "vector"
#include "string"
#include "cmath"
#include "iomanip"
#include "sstream"

using namespace std;

const double pi = 3.141592654;

//tao struct cho tung he so va bien
struct Math
{
	char bien = ' '; //x: x, y: y, r: r, u: x*y, z: x/y
	int mu = 1;
	int mulg = 1;
	double heso = 1;
	string lg = ""; //luong giac
	double gt = 1; //gia tri
};

//dieu kien de bai cho
struct Condiction
{
	double xl;
	double xm;
	double yl;
	double ym;
	double r;
};

struct CondictionLG
{
	double phil = 0;
	double phim = pi*2;
	double rl = 0;
	double rm = 1;
};

Math chuyenTDC(Math member);
Math inteR(Math member, CondictionLG condict);
double inteP(Math member, CondictionLG condict);

//tinh tich phan
double inteC(vector<Math> member, CondictionLG condict)
{
	vector<Math> m;
	double sum=0;
	for (int i = 0; i < member.size(); i++)
	{
		m.push_back(chuyenTDC(member[i]));
		cout << m[i].heso << '*' << m[i].bien << '^' << m[i].mu<<'*'<<m[i].lg << '^' << m[i].mulg << endl;
		sum += inteP(inteR(m[i], condict), condict);
	}
	
	return sum;
}

Math inteR(Math member, CondictionLG condict) //tich phan theo R
{
	Math m = member;
	m.mu++;
	m.heso /= m.mu;
	m.gt = pow(condict.rm, m.mu) - pow(condict.rl, m.mu);
	return m;
}

double inteP(Math member, CondictionLG condict) //tich phan theo Phi
{
	cout << member.heso * member.gt << endl;
	Math m = member;
	if (member.lg == "cos")
	{
		if (member.mulg == 2)
		{
			cout << condict.phim << ' '<<condict.phil << endl;
			cout << m.gt * m.heso * (condict.phim / 2.0 + sin(2 * condict.phim) / 4.0) - m.gt * m.heso * (condict.phil / 2.0 + sin(2 * condict.phil) / 4.0) << endl;
			return m.gt * m.heso * (condict.phim / 2.0 + sin(2 * condict.phim) / 4.0) - m.gt * m.heso * (condict.phil / 2.0 + sin(2 * condict.phil) / 4.0);
		}
		else
		{			
			cout << "cos: " << m.gt * m.heso * sin(condict.phim) - m.gt * m.heso * sin(condict.phil) << endl;
			return m.gt * m.heso * sin(condict.phim) - m.gt * m.heso * sin(condict.phil);
		}
	}
	if (member.lg == "sin")
	{
		if (member.mulg == 2)
		{
			return m.gt * m.heso * (condict.phim / 2.0 + sin(2 * condict.phim) / 4.0) - m.gt * m.heso * (condict.phil / 2.0 - sin(2 * condict.phil) / 4.0);
		}
		else
		{			
			cout << "sin: " << -(m.gt * m.heso * cos(condict.phim)) + (m.gt * m.heso * cos(condict.phil)) << endl;
			return -(m.gt * m.heso * cos(condict.phim)) + (m.gt * m.heso * cos(condict.phil));
		}
	}
	if (member.lg == "sin2")
	{
		return -(m.gt * m.heso * sin(2 * condict.phim) - m.gt * m.heso * sin(2 * condict.phil));
	}
	if (member.lg == "tan")
	{
		return tan(condict.phim) - tan(condict.phil);
	}

	return 0;
}

Math chuyenTDC(Math member) //chuyen tu toa do decartes sang toa do cuc
{
	Math m = member;
	if (member.bien == 'x')
	{
		m.bien = 'r';
		m.lg = "cos";
		m.mulg = m.mu;
		m.mu += 1;
	}
	if (member.bien == 'y')
	{
		m.bien = 'r';
		m.lg = "sin";
		m.mulg = m.mu;
		m.mu += 1;
	}
	if (member.bien == ' ')
	{
		m.bien = 'r';
		m.mu = 1;
		m.mulg = 0;
	}
	if (member.bien == 'u')
	{
		m.bien = 'r';
		m.lg = "sin2";
		m.mulg = m.mu;
		m.mu *= 2;
		m.heso /= 2.0;
	}
	if (member.bien == 'v')
	{
		m.bien = 'r';
		m.lg = "tan";
		m.mulg = m.mu;
		m.mu = 1;
	}
	return m;
}

int main()
{
	string temp = ""; //string tam thoi de luu string cho vector,...
	string problem;
	cout << "Enter function: \n";
	getline(cin, problem);
	//int numcon;
	//cout << "Enter number of condiction: \n";
	//cin >> numcon;
	//cin.ignore(); //bi loi voi getline o duoi
	//vector<string> condiction;
	//for (int i = 0; i < numcon; i++)
	//{
	//	getline(cin, temp);
	//	condiction.push_back(temp);
	//}
	vector <Math> member;
	Math m;
	bool nega = 0, hs = 0; //nega: dau am, hs: he so da duoc count
	bool hesolamot = 0; //loi he so = 1
	int dembien = 1;
	Condiction condict = { -1,1,-1,1,1 };
	stringstream ss(problem);
	temp = "";
	string tempvari;
	//doc ham so
	for (char c : problem+" ") // bi sot so cuoi cung
	{
		//kiem tra dau he so
		
		//dem he so
		if (isdigit(c))
		{
			temp += c;
		}
		else
		{
			if (!temp.empty())
			{
				if(hs == 0 && !hesolamot)
				{
					m.heso = nega ? -stoi(temp) : stoi(temp);
					hs = 1;
					temp = "";
				}
				else
				{
					m.mu = stoi(temp);
					temp = "";
					hs = 0;
				}
			}
			if (isalpha(c) || c == '/')
			{
				tempvari += c;
				if(c != '/') m.bien = c;
				if (m.heso == 1) hesolamot = 1;
			}
		}
		if (c == '+' || c == '-') // reset va them member
		{
			if (dembien != 0)
			{
				dembien++;
				if (tempvari == "xy") m.bien = 'u';
				if (tempvari == "x/y") m.bien = 'v';
				tempvari = "";
				member.push_back(m);
				m = Math();
				if (c == '-')
					nega = 1;
				else
					nega = 0;
				hs = 0;
			}
			else if (c == '-')
			{
				nega = 1;
			}
			continue;
		}
		
	}
	if (tempvari == "xy") m.bien = 'u';
	if (tempvari == "x/y") m.bien = 'v';
	member.push_back(m);

	
	//dieu kien
	CondictionLG dieukien;
	int numcon;
	cout << "Enter number of condiction: \n";
	cin >> numcon;
	cin.ignore(); //bi loi voi getline o duoi

	cout << "Type of condiction: (Type 0 - 4)" << endl;
	cout << "0. Circle x^2 +y^2 <= a" << endl;
	cout << "1. Between Two Circles a <= x^2 + y^2 <= b" << endl;
	cout << "2. Between Two Circles ax (or ay) <= x^2 + y^2 <= bx (or by)" <<" chua lam xong" << endl;
	cout << "3. Domain ax + by >= c" << endl;
	cout << "4. Domain ax + by <= c" << endl;
	cout << "Select in order to avoid error." << endl;
	int choose;
	bool khoitao = 0;
	for (int i = 0; i < numcon; i++)
	{
		cout << "Enter your choice: " << endl;
		cin >> choose;
		if (choose < 0 || choose > 4)
		{
			i--;
			cout << "Type again" << endl;
			continue;
		}
		double a, b, c, k, phi;
		switch (choose)
		{
		case 0:
			cout << "Type a: "; cin >> a;
			dieukien.rm = sqrt(a);
			break;
		case 1: 
			cout << "Type a: "; cin >> a;
			cout << "Type b: "; cin >> b;
			dieukien.rl = sqrt(a);
			dieukien.rm = sqrt(b);
			break;
		case 2:
			break;
		case 3: 
			cout << "Type a: "; cin >> a;
			cout << "Type b: "; cin >> b;
			cout << "Type c: "; cin >> c;
			phi = atan2(b , a);
			k = c / (dieukien.rm * sqrt(a * a + b * b));
			
			if (k >= -1 && k <= 1)
			{				
				double ak = acos(k);
				if (!khoitao)
				{
					dieukien.phil = phi - ak;
					dieukien.phim = phi + ak;
					khoitao = 1;
				}

				if (phi - ak >= dieukien.phil) dieukien.phil = phi - ak;
				if (phi + ak <= dieukien.phim) dieukien.phim = phi + ak;
				cout << dieukien.phil << ' ' << dieukien.phim << endl;
			}
			break;
		case 4: 
			double a, b, c;
			cout << "Type a: "; cin >> a;
			cout << "Type b: "; cin >> b;
			cout << "Type c: "; cin >> c;
			phi = atan2(b , a);
			k = c / (dieukien.rm * sqrt(a * a + b * b));
			if (k >= -1 && k <= 1)
			{
				double ak = acos(k);
				if (ak + phi >= dieukien.phil) dieukien.phil = ak + phi;
				if (phi - ak + 2 * pi <= dieukien.phim) dieukien.phim = phi - ak + 2 * pi;
			}
			break;
		default: break;
		}
	}
	//Tinh toan
	


	//doc Condiction dang so cap
	//for (int i = 0; i < condiction[0].length(); i++)
	//{
	//	condict.r = 0;
	//	string str = "x^2+y^2<=";
	//	if (condiction[0].find(str) != string::npos)
	//		for (int i = str.length(); i < condiction[0].length(); i++)
	//			if (isdigit(condiction[0][i]))
	//				condict.r = condiction[0][i] - '0' + condict.r * 10;
	//}
	//condict.r = sqrt(condict.r);
	//cout << condict.r;

	for(int i = 0; i < dembien; i++)
	cout << member[i].heso << '*' << member[i].bien << '^' << member[i].mu <<endl;
	cout << "Result: " << inteC(member, dieukien);
	//cout << member[1].heso << '*' << member[1].vari << '^' << member[1].power;


	//cout << fixed << setprecision(10) << inteC(member, condict);



	return 0;
}
