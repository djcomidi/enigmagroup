import java.applet.Applet;
import java.awt.Button;
import java.awt.Color;
import java.awt.Event;
import java.awt.Graphics;
import java.awt.Label;
import java.awt.TextField;

public class applet1 extends Applet {
	Button okButton;
	TextField passField;
	Label label;

	public void paint(Graphics g) {
		g.setColor(Color.gray);
		g.fillRect(0, 0, 200, 200);
	}

	public void init() {
		setLayout(null);

		this.passField = new TextField("", 100);
		this.passField.setBounds(50, 30, 100, 20);
		this.okButton = new Button("Login");
		this.okButton.setBounds(50, 60, 100, 20);
		this.label = new Label("Enter password!");
		this.label.setBounds(10, 90, 180, 20);
		this.label.setBackground(Color.gray);
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
		String real = "JavaApplet";

		if (labelTemp.toString() == "Login") {
			String pwd = this.passField.getText();

			if (pwd.equals(real)) this.label.setText("Congratulations!");
			else
				this.label.setText("Incorrect!");
		} else {
			this.label.setText("Error!");
		}
	}
}
