#include <iostream>
#include <conio.h>
using namespace std;

bool game = true; //игровое правило
int width = 10; // ширина 49
int height = 20; // высота 37
int score = 0; // очки
int life = 4;
class MyClass
{
public:
	int x = 2;
	int y = 20;
	int horizon = 1;
};
class border{
public:
	int x = 2;
	int y = 0;
	int hor = 1;

	void set(int x) {
		y = x;
	}
};
border q1;
border q2;
border q3;
MyClass player;
void Draw() {
	for (int i = 0; i <= width; i++) { //верхняя граница
		cout << '#';
	}
	if (score == 0) {
		cout << "__000";
	}
	else {
		cout << "__" << score;
	}
	cout << endl;
	for (int j = 0; j <= height; j++) { // боковые границы ,поле, объекты 
		for (int i = 0; i <= width; i++) {
			if (i == 0 || i == width || i == player.x && j == player.y || i == player.x + 2 && j == player.y || i == player.x + 1 && j == player.y - 1 || i == player.x && j == player.y - 2 || i == player.x + 1 && j == player.y - 2 || i == player.x + 2 && j == player.y - 2 || i == player.x + 1 && j == player.y - 3 || i == q1.x && j == q1.y || i == q1.x + 2 && j == q1.y || i == q1.x + 1 && j == q1.y - 1 || i == q1.x && j == q1.y - 2 || i == q1.x + 1 && j == q1.y - 2 || i == q1.x + 2 && j == q1.y - 2 || i == q1.x + 1 && j == q1.y - 3 || i == q2.x && j == q2.y || i == q2.x + 2 && j == q2.y || i == q2.x + 1 && j == q2.y - 1 || i == q2.x && j == q2.y - 2 || i == q2.x + 1 && j == q2.y - 2 || i == q2.x + 2 && j == q2.y - 2 || i == q2.x + 1 && j == q2.y - 3 || i == q3.x && j == q3.y || i == q3.x + 2 && j == q3.y || i == q3.x + 1 && j == q3.y - 1 || i == q3.x && j == q3.y - 2 || i == q3.x + 1 && j == q3.y - 2 || i == q3.x + 2 && j == q3.y - 2 || i == q3.x + 1 && j == q3.y - 3) {
				cout << "#"; // граница
			}
			else {
				cout << " "; //воздух
			}
			if (j == 0 && i == 10) {
				cout << "_HI SCORE";
			}
			if (j == 1 && i == 10) {
				if (life == 4) {
					cout << "_####";
				}
				if (life == 3) {
					cout << "_###";
				}
				if (life == 2) {
					cout << "_##";
				}
				if (life == 1) {
					cout << "_#";
				}
			}
		}
		cout << endl;
	}
	for (int i = 0; i <= width; i++) { // нижняя граница
		cout << '#';
	}
}
void Input() {
	if (_kbhit()) { //  проверка на нажатие
		switch (_getch()) { // проверка кнопки
		case 'a' : //сравнивае кнопки
			if (player.horizon != 1) { // блокировка движения в боратную сторону
				player.horizon = 1; // изменение напровления
			}
			break; // выход из switch
		case 'd':
			if (player.horizon != 2) {
				player.horizon = 2;
			}
			break;
		}
	}
}
void Logic() {
	system("cls");
	if (player.horizon == 1) {
		player.x = 2;
	}
	if (player.horizon == 2) {
		player.x = width - 4;
	}
	q1.y += 1; q2.y += 1; q3.y += 1;
	if (q1.y >= 24) {
		q1.y = 0;
		q1.hor = 1 + (rand() % 2);
	}
	if (q1.hor == 1) {
		q1.x = 2;
	}
	if (q1.hor >= 2) {
		q1.x = width - 4;
	}

	if (q2.y >= 24) {
		q2.y = 0;
		q2.hor = 1 + (rand() % 2);
	}
	if (q2.hor == 1) {
		q2.x = 2;
	}
	if (q2.hor == 2) {
		q2.x = width - 4;
	}

	if (q3.y >= 24) {
		q3.y = 0;
		q3.hor = 1 + (rand() % 2);
	}
	if (q3.hor == 1) {
		q3.x = 2;
	}
	if (q3.hor == 2) {
		q3.x = width - 4;
	}

	if (life <= 0) {
		game = false;
	}
	if (q1.y >= 17 && q1.hor == player.horizon || q2.y >= 17 && q2.hor == player.horizon || q3.y >= 17 && q3.hor == player.horizon) {
		life -= 1;
		q1.hor = 1 + (rand() % 2);
		q2.hor = 1 + (rand() % 2);
		q3.hor = 1 + (rand() % 2);
		q1.y = 0;
		q2.y = -8;
		q3.y = -16;

	}
	if (q1.y == 22 || q2.y == 22 || q3.y == 22 ) {
		score += 100;
	}
	if (score >= 999900) {
		score = 0;
	}
}
int main(){
	q1.hor = 1 + (rand() % 2);
	q2.hor = 1 + (rand() % 2);
	q3.hor = 1 + (rand() % 2);
	q2.y = -8;
	q3.y = -16;
	system("title game");
	system("mode con:cols=20 lines=24");
	while (game == true) {
		Input();
		Draw();
		Logic();
	}
	system("pause");
}