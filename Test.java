public class Test {
    public static void main(String[] args) {
        Complex d = 0;
        System.out.println(d);
        while (!StdIn.isEmpty()) {
            double value = StdIn.readDouble();
            StdOut.println(value);
        }
    }
}
