## Random ##

- Random Generator
```Dart
import 'dart:math';

var diceRoll = Random().nextInt(6) + 1 // 0 ~ 5
activeDiceImage = "assets/images/dice-$diceRoll.png";

//Rando() 도 결국 Object이라서 매번 새로 만들어져서 메모리를 낭비할 필요가 없다. (물론 자동으로 지워지지만)

final randomizer = Random();
diceRoll = randomizer.nextInt(6) + 1
```
Refers to : [[String]], [[Import]]
