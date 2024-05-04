// javac -target 1.1 -source 1.2 C:\Users\Admin\Desktop\NETZKUNST\site\ClockApplet.java
import java.applet.*;
import java.awt.*;
import java.util.*;

public class ClockApplet extends Applet implements Runnable {
    private Thread clockThread;

    public void init() {
        // Initialize the applet
    }

    public void start() {
        if (clockThread == null) {
            clockThread = new Thread(this);
            clockThread.start();
        }
    }

    public void stop() {
        if (clockThread != null) {
            clockThread.stop();
            clockThread = null;
        }
    }

    public void run() {
        while (true) {
            repaint();
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public void paint(Graphics g) {
        // Get current time
        Calendar now = Calendar.getInstance();
        int hour = now.get(Calendar.HOUR_OF_DAY);
        int minute = now.get(Calendar.MINUTE);
        int second = now.get(Calendar.SECOND);

        // Display current time
        String time = hour + ":" + minute + ":" + second;
        g.drawString(time, 50, 30);
    }
}
