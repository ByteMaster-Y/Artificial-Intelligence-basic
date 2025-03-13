def TowerOfHanoi(n, s_pole, i_pole, d_pole):
    if n == 1:
        print("Move disc 1 from pole", s_pole, "to pole", d_pole) # 원판이 1개만 남으면 바로 목적지로 이동
        return
    TowerOfHanoi(n-1, s_pole, d_pole, i_pole)  
    print("Move disc", n,"from pole", s_pole, "to pole", d_pole)  
    TowerOfHanoi(n-1, i_pole, s_pole, d_pole)  



n = 4

TowerOfHanoi(n, 'A','B','C')
