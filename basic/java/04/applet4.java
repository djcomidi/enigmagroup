import java.applet.Applet;
import java.awt.Button;
import java.awt.Color;
import java.awt.Event;
import java.awt.Graphics;
import java.awt.Label;
import java.awt.TextField;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.regex.Pattern;

public class applet4 extends Applet {
	private static final long serialVersionUID = 31337L;
	static final String CHECK_SUM = "129946388659050031";
	static final String ERROR_1 = "Error - Invalid Authorization Code Length!";
	static final String ERROR_2 = "Error - Invalid Authorization Code!";
	static final String ERROR_3 = "Error - Invalid Password Length!";
	static final String ERROR_4 = "Error - Unknown!";
	static final String ERROR_5 = "Error - Incorrect Password, Exiting...";
	static final String SUCCESS = "Correct! Use the AuthKey as the mission password!";
	static final String PHASH = "a8549033af1cda11ab2360d93ebc8764";
	static final String NHASH = "fce0dfbaafd8198a734cd368b3ea4f5e";
	Button okButton;
	TextField passField;
	TextField authField;
	Label label;
	Label lbAuth;
	Label lbPass;
	Color GlobColor = Color.LIGHT_GRAY;

	public void paint(Graphics g) {
		g.setColor(this.GlobColor);
		g.fillRect(0, 0, 1000, 1000);
	}

	public void init() {
		setLayout(null);

		this.passField = new TextField("", 35);
		this.authField = new TextField("0000-0000-0000-0000-0000-0000", 35);

		this.okButton = new Button("Authorize");

		this.label = new Label("Please authorize yourself...");
		this.lbPass = new Label("Password :-");
		this.lbAuth = new Label("Authorization Code :- ");

		this.passField.setBounds(170, 100, 300, 20);
		this.authField.setBounds(170, 130, 300, 20);

		this.okButton.setBounds(200, 200, 100, 20);

		this.label.setBounds(10, 250, 400, 100);
		this.label.setBackground(this.GlobColor);
		this.label.setAlignment(0);

		this.lbAuth.setBounds(10, 130, 150, 20);
		this.lbAuth.setBackground(this.GlobColor);
		this.lbAuth.setAlignment(0);

		this.lbPass.setBounds(10, 100, 150, 20);
		this.lbPass.setBackground(this.GlobColor);
		this.lbPass.setAlignment(0);

		add(this.okButton);
		add(this.passField);
		add(this.authField);
		add(this.lbPass);
		add(this.lbAuth);
		add(this.label);
	}

	public boolean action(Event evt, Object arg) {
		if ((evt.target instanceof Button))
			HandleButtons(arg);
		return true;
	}

	public void HandleButtons(Object labelTemp) {
		if (labelTemp.toString() == "Authorize") {
			String pwd = this.passField.getText();
			String auth = this.authField.getText();

			if ((auth.length() > 35) || (auth.length() <= 0)) {
				this.label.setText("Error - Invalid Authorization Code Length!");
				System.exit(0);
			}

			if (pwd.length() != 8) {
				this.label.setText("Error - Invalid Password Length!");
				System.exit(0);
			} else {
				String temp = hash(pwd);

				if (!temp.equals("a8549033af1cda11ab2360d93ebc8764")) {
					this.label.setText("Error - Incorrect Password, Exiting...");
					System.exit(0);
				}

				String code = genAuthKey(auth);
				String key = genPassKey(pwd);

				if (Long.parseLong(code) <= 0L) {
					this.label.setText("Authorization Check Failed. Exiting...");
					System.exit(0);
				} else {
					long cKey = Long.parseLong(code);
					long lng = Long.parseLong("" + pwd.length() + 2) * 8679L;
					String aHash = hash(auth);
					cKey *= lng;
					cKey += Long.parseLong(key);
					long tKey = Long.parseLong("129946388659050031");

					if ("fce0dfbaafd8198a734cd368b3ea4f5e".equals(aHash))
						if (cKey == tKey) {
							this.label.setText("Correct! Use the AuthKey as the mission password!");
						} else if (cKey != tKey) {
							this.label.setText("Error - Invalid Authorization Code!");
						} else {
							this.label.setText("Error - Unknown!");
							destroy();
						}
				}
			}
		}
	}

	protected static String genAuthKey(String authCode) {
		String[] authArr = Pattern.compile("-").split(authCode);
		String auth1 = authArr[0];
		String auth2 = authArr[1];
		String auth3 = authArr[2];
		String auth4 = authArr[3];
		String auth5 = authArr[4];
		String auth6 = authArr[5];

		char a = authArr[0].charAt(0);
		char b = authArr[1].charAt(0);
		char c = authArr[2].charAt(1);
		char d = authArr[3].charAt(3);
		char e = authArr[4].charAt(0);
		char f = authArr[5].charAt(2);

		char a2 = authArr[0].charAt(1);
		char b2 = authArr[1].charAt(2);
		char c2 = authArr[2].charAt(0);
		char d2 = authArr[3].charAt(1);
		char e2 = authArr[4].charAt(2);
		char f2 = authArr[5].charAt(0);

		long mod1 = authArr[3].charAt(0);
		long mod2 = authArr[3].charAt(2);
		long mod3 = authArr[4].charAt(1);
		long mod4 = authArr[4].charAt(3);
		long mod5 = authArr[5].charAt(1);
		long mod6 = authArr[5].charAt(3);

		if ((a != '8') || (b != '4') || (c != '8') || (d != '2') || (e != '8') || (f != '2')) {
			return "0";
		}
		if ((a2 == '5') && (b2 == '5') && (c2 == '4') && (d2 == '1') && (e2 == '3') && (f2 == '2') && (mod1 == 57L) && (mod2 == 55L) && (mod3 == 54L) && (mod4 == 52L) && (mod5 == 51L) && (mod6 == 51L)) {
			Long aCode = Long.valueOf(Long.parseLong(auth1) * Long.parseLong(auth2) * Long.parseLong(auth3) - Long.parseLong(auth4) - Long.parseLong(auth5) + Long.parseLong(auth6));
			String code = "" + aCode;
			return code;
		}
		return "0";
	}

	protected static String genPassKey(String pwd) {
		long y = 0L;
		int x = 0;

		while (x < pwd.length()) {
			char c = pwd.charAt(x);
			int tmp = c;
			y += tmp;
			y *= x;
			x++;
		}

		String pKey = "" + y;

		return pKey;
	}

	public static String hash(String s) {
		String tmp = "";
		try {
			MessageDigest m = MessageDigest.getInstance("MD5");
			m.update(s.getBytes(), 0, s.length());
			tmp = new BigInteger(1, m.digest()).toString(16);
		} catch (NoSuchAlgorithmException nfeRef) {
		}

		while (tmp.length() < 32) {
			tmp = "0" + tmp;
		}

		return tmp;
	}
}