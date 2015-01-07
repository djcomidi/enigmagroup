import java.applet.Applet;
import java.awt.Button;
import java.awt.Color;
import java.awt.Event;
import java.awt.Graphics;
import java.awt.Label;
import java.awt.TextField;

public class applet3 extends Applet {
	Button okButton;
	TextField passField;
	Label label;
	Color GlobColor = Color.LIGHT_GRAY;

	public void paint(Graphics g) {
		g.setColor(this.GlobColor);
		g.fillRect(0, 0, 500, 500);
	}

	public void init() {
		setLayout(null);

		this.passField = new TextField("", 100);

		this.okButton = new Button("Login");

		this.label = new Label("Enter password!");

		this.passField.setBounds(50, 30, 180, 20);

		this.okButton.setBounds(50, 60, 180, 20);

		this.label.setBounds(10, 90, 260, 20);
		this.label.setBackground(this.GlobColor);
		this.label.setAlignment(1);

		add(this.okButton);
		add(this.passField);
		add(this.label);
	}

	public boolean action(Event evt, Object arg) {
		if ((evt.target instanceof Button))
			HandleButtons(arg);
		return true;
	}

	protected void HandleButtons(Object labelTemp) {
		long p1 = 0L;
		long p2 = 0L;

		String real = GenPass();

		if (labelTemp.toString() == "Login") {
			String pwd = this.passField.getText();

			p1 = CheckPass(pwd);
			p2 = CheckPass(real);

			if (pwd.equals(real)) this.label.setText("Congratulations!");
			else
				this.label.setText("Incorrect!");
		} else {
			this.label.setText("Error!");
		}
	}

	protected static String GenPass() {
		int tmp1 = 69;
		int tmp2 = 71;
		int tmp3 = 89;
		int tmp4 = 53;
		int tmp5 = 42;
		int tmp6 = 90;
		int tmp7 = 109;
		int tmp8 = 64;
		int tmp9 = 77;
		int tmp10 = 89;

		int dud1 = 34;
		int dud2 = 67;
		int dud3 = 88;
		int dud4 = 42;
		int dud5 = 12;
		int dud6 = 22;
		int dud7 = 109;
		int dud8 = 62;
		int dud9 = 11;
		int dud10 = 9;
		int dud11 = 111;

		String pass = Character.toString((char)tmp1);
		pass = pass + Character.toString((char)tmp2);
		pass = pass + Character.toString((char)tmp3);
		pass = pass + Character.toString((char)tmp4);
		pass = pass + Character.toString((char)tmp5);
		pass = pass + Character.toString((char)tmp6);
		pass = pass + Character.toString((char)tmp7);
		pass = pass + Character.toString((char)tmp8);
		pass = pass + Character.toString((char)tmp9);
		pass = pass + Character.toString((char)tmp10);

		return pass;
	}

	protected static long CheckPass(String phrase) {
		int x = 0;
		long y = 0L;

		while (x < phrase.length()) {
			char c = phrase.charAt(x);
			int tmp = c;
			y += tmp;
			y += x;
			x++;
		}
		return y;
	}
}
