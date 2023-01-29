#include <iostream>
#include <conio.h>
using namespace std;
//переменные
bool game = true; //игровое правило
int width = 20; // ширина
int height = 10; // высота
int score = 0; // очки
int run = 0;// 1 - вправо , 2 вниз , 3 влево , 4 вверх
//классы
class player { // класс игрока
public:
	int x = width / 2;
	int y = height / 2;
};
class aplle { // класс яблока
public:
	int x = 1 + rand() % 20;
	int y = 1 + rand() % 10;
};
//инициализируем классы в объекты
aplle apl;
player p;
//функции
void loading() { //загрузка
	string r = ".";
	for (int n = 0; n <= 100; n++) {
		if (r == "....") { r = "."; }
		cout << "loading" << r << n << '%';
		system("cls");
		r += ".";
		if (r == ".") { r += "."; }
	}
}
void Draw() { // отрисовка
	for (int i = 0; i <= width; i++) { //верхняя граница
		cout << '#';
	}
	cout << " ";
	for (int i = 0; i < score; i++) { // панель очков
		cout << "v";
	}
	cout << endl;
	for (int j = 0; j <= height; j++) { // боковые границы ,поле, объекты 
		for (int i = 0; i <= width; i++) {
			if (i == 0 || i == width) {
				cout << "#"; // граница
			}
			else if (i == p.x && j == p.y) {
				cout << "p"; // игрок
			}
			else if (i == apl.x && j == apl.y) {
				cout << '0'; //яблока
			}
			else {
				cout << " "; //воздух
			}
		}
		cout << endl;
	}
	for (int i = 0; i <= width; i++) { // нижняя граница
		cout << '#';
	}
}
void Input() { // ввод
	if (_kbhit()) { //  проверка на нажатие
		switch (_getch()) { // проверка кнопки
		case 'w': //сравнивае кнопки
			if (run != 2) { // блокировка движения в боратную сторону
				run = 4; // изменение напрровления
			}
			break; // выход из switch
		case 'a':
			if (run != 1) {
				run = 3;
			}
			break;
		case 's':
			if (run != 4) {
				run = 2;
			}
			break;
		case 'd' :
			if (run != 3) {
				run = 1;
			}
			break;
		case 'x':
			game = false;
		}
	}
}
void logic() { // игровая логика
	system("cls"); // очистка экрана
	if (run == 4 ) {
			p.y--;
	}
	else if (run == 3) {
			p.x--;
	}
	else if (run == 2 ) {
			p.y++;
	}
	else if (run == 1 ) {
		p.x++;
	}
	if (p.x < 0 || p.x > width || p.y < 0 || p.y > height) {
		game = false;
	}
	if (p.x == apl.x && p.y == apl.y) {
		score++;
		apl.x = 1 + rand() % 20;
		apl.y = 1 + rand() % 10;
	}
}
int main()
{
	loading(); // вызов загрузки
	while (game == true) { // игровой цикл, вызов функций
		Draw();
		Input();
		logic();
	} // действия после проигрыша
	cout << "game over , score " << score << endl;
	system("pause");
	return 0;
}