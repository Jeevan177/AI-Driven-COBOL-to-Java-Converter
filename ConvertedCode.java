Here is the equivalent Java code for the given COBOL program:
```java
// HelloWorld.java

public class HelloWorld {
    public static void main(String[] args) {
        // Equivalent to DISPLAY "Hello, World!" in COBOL
        System.out.println("Hello, World!");

        // No equivalent to STOP RUN in Java, as the program will terminate naturally
        // after executing the main method
    }
}
```
Let me explain what's happening here:

1. In Java, we define a `public class` called `HelloWorld`, which is the equivalent of the COBOL program's `PROGRAM-ID`.
2. The `main` method is the entry point of the Java program, similar to the `PROCEDURE DIVISION` in COBOL.
3. `System.out.println("Hello, World!")` is the equivalent of `DISPLAY "Hello, World!"` in COBOL. It prints the string "Hello, World!" to the console, followed by a newline character.
4. In COBOL, `STOP RUN` is used to terminate the program. In Java, the program will terminate naturally after executing the `main` method, so we don't need an equivalent statement.

Note that in modern Java, it's common to use a more concise syntax, such as:
```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```
I've kept the original syntax to make it easier to compare with the COBOL code.