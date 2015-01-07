import java.applet.Applet;
import java.awt.Button;
import java.awt.Color;
import java.awt.Event;
import java.awt.Graphics;
import java.awt.Label;
import java.awt.TextField;

public class applet2 extends Applet {
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
		this.passField.setBounds(50, 30, 100, 20);

		this.okButton = new Button("Login");
		this.okButton.setBounds(50, 60, 100, 20);

		this.label = new Label("Enter password!");
		this.label.setBounds(10, 90, 180, 20);
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
		String p1 = "yhnH";
		String p2 = "hjwB";
		String p3 = "vfUK";
		String p4 = "_212";
		String p5 = "e8k0";
		String p6 = "IJKR";

		String temp = p6 + p2 + p4 + p3 + p1 + p5;

		if (labelTemp.toString() == "Login") {
			String pwd = this.passField.getText();

			if (pwd.equals(temp)) this.label.setText("Congratulations!");
			else
				this.label.setText("Incorrect!");
		} else {
			this.label.setText("Error!");
			destroy();
		}
	}
}
