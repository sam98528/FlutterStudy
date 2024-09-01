## ListView vs ListView.builder vs Column ##

|        |    Column     |   ListView    |    ListView.Builder    |
| :----: | :-----------: | :-----------: | :--------------------: |
| 스크롤 가능 |       X       |       O       |           O            |
| 동적 생성  |       X       |       X       |           O            |
| 성능 최적화 |       X       |       O       |           O            |
| 랜더링 방식 | 모든 자식 위젯이 한번에 | 모든 자식 위젯이 한번에 | 스크롤 가능한 영역의 자식 위젯만 랜더링 |
refers to: [[ListView]], [[Column & Rows]]
