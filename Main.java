import javax.swing.*;

public class Main {
    public static void main(String[] args) {
        System.out.println("You Java program has compiled and is now running!");

        //creating instance of JFrame
        JFrame f = new JFrame();

        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JButton b1 = new JButton("Hello, World!");
        b1.setBounds(90, 100, 180, 40);
        f.add(b1);

        f.setSize(400, 400);
        f.setLayout(null);
        f.setVisible(true);
    }
}