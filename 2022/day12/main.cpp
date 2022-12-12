#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <utility>

using std::string;
using std::vector;

// Failed attempt

void main()
{
    vector<vector<char> *> grid;

    std::ifstream file("input.txt");
    string line;

    while (file)
    {
        file >> line;
        vector<char> *tmp = new vector<char>();

        for (char &c : line)
        {
            tmp->push_back(c);
        }

        grid.push_back(tmp);
    }
    std::pair<int, int> start;

    // find S
    for (int i = 0; i < grid.size(); i++)
    {
        for (int j = 0; j < grid.size(); j++)
        {
            if (grid[i][j] == 'S')
            {
                start = std::make_pair(i, j);
            }
        }
    }
}