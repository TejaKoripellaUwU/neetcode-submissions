class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict_ls = {}
        col_dict_ls = {}
        sq_dict_ls = {}
        for r_idx,row in enumerate(board):
            for col_idx,el in enumerate(row):
                if el != ".":
                    sq_dict_key = 3*(r_idx//3) + col_idx//3
                    sq_v = sq_dict_ls.get(sq_dict_key,set())
                    if el in sq_v:
                        print(3*(r_idx//3) )

                        print(sq_dict_key)
                        print(sq_v)
                        print("sq false trig")
                        return False
                    else:
                        sq_v.add(el)
                    sq_dict_ls.update({sq_dict_key:sq_v})

                    col_v = col_dict_ls.get(col_idx,set())
                    if el in col_v:
                        print("col false trig")
                        return False
                    else:
                        col_v.add(el)
                    col_dict_ls.update({col_idx:col_v})

                    row_v = row_dict_ls.get(r_idx,set())
                    if el in row_v:
                        print("row false trig")
                        return False
                    else:
                        row_v.add(el)
                    row_dict_ls.update({r_idx:row_v})
        return True
