## Function Argument ##

 - Named Argument vs Positional Argument
```Dart
void add (a , b) {
	print(a + b);
}

void minus({a,b}){
	print(a - b);
}

void main(){
add(1,2); // Positional Argument -> 3
add(a : 1, b : 2); // Error
minus(1,2); // Error
minus(a: 1, b : 2); // Named Argument -> -1
}
```