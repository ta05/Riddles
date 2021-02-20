#include <iostream>
#include <string>
#include <time.h>
using namespace std;

int main() {
    int length;
    cout << "Welcome to The Hiding Cat Puzzle.\nEnter the number of boxes (minimum 2): ";
    cin >> length;

    while(length <= 1){
        cout << "Please enter a valid number of boxes (minimum 2): ";
        cin >> length;
    }

    srand ( time(NULL) ); // to seed the random number

    int boxes[length] = {0};
    int guess;
    int numGuess = 0;
    bool correct = false;

    int position = (rand() % length) + 1;
    boxes[position] = 1;

    do {
        cout << "\nGuess a box between " << 1 << " and " << length << ": ";
        cin >> guess;
        while(guess < 1 || guess > length) {
            cout << "Please enter a valid guess!" << endl;
            cout << "\nGuess a box between " << 1 << " and " << length << ": ";
            cin >> guess;
        }
        numGuess++;
        if(boxes[guess - 1] == 1) {
            cout << "\nCorrect! The cat is in box " << guess << endl;
            correct = true;
            break;
        }
        else {
            cout << "\nWrong! The cat is not in box " << guess << endl;
            cout << "Guess again" << endl;

            // cout << "The cat is in box " << position + 1 << endl;

            boxes[position]--;
            if (position == length - 1) {
                position--;
            }
            else if (position == 0) {
                position++;
            }
            else {
                if(rand() % 2 < 1) {
                    position--;
                }
                else {
                    position++;
                }
            }
            boxes[position]++;
        }
        // cout << "The cat moved to box " << position + 1 << endl;
    } while (!correct);

    cout << "You found the cat in " << numGuess << " attempt(s)!";
}

