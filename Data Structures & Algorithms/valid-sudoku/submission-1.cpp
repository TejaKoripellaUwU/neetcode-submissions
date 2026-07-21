#include <print>

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<unordered_set<int>> rows(9);
        vector<unordered_set<int>> cols(9);
        vector<unordered_set<int>> boxes(9);

        for (int row = 0; row<9; row++){
            for (int col = 0; col<9; col ++){
                if (board[row][col] == '.'){
                    continue;
                }
                if (rows[row].contains(board[row][col]) ||
                cols[col].contains(board[row][col]) ||
                boxes[(row/3) * 3 + col/3].contains(board[row][col])){
                    return false;
                }
                rows[row].insert(board[row][col]);
                cols[col].insert(board[row][col]);
                boxes[(row/3) * 3 + col/3].insert(board[row][col]);
            }
        }
        return true;
    }
};
