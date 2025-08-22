public class EchoDouble {
    public static void main(String[] args) {
        while (!StdIn.isEmpty()) {
            double value = StdIn.readDouble();
            StdOut.println(value);
        }
    }
}
