from flask.ext.wtf import Email, Form, PasswordField, Required, TextField

class ChangeUsernameForm(Form):
    username = TextField("Username", validators = [Required()])

class ChangePasswordForm(Form):
	current_password = PasswordField("Current Password", validators = [Required()])
	password = PasswordField("New Password", validators = [Required()])
	password2 = PasswordField("Re-enter New Password", validators = [Required()])

class LoginForm(Form):
    email = TextField("Email", validators = [Required(), Email()])
    password = PasswordField("password", validators = [Required()])

class RegisterForm(Form):
    first_name = TextField("First Name", validators = [Required()])
    last_name = TextField("Last Name", validators = [Required()])
    email = TextField("Email", validators = [Required(), Email()])
    email2 = TextField("Re-enter Email", validators = [Required(), Email()])
    password = PasswordField("Password", validators = [Required()])
    password2 = PasswordField("Re-enter Password", validators = [Required()])

class ResetPasswordForm(Form):
    email = TextField("Email", validators = [Required(), Email()])

class ProfileSettingsForm(Form):
    first_name = TextField("First Name", validators = [Required()])
    last_name = TextField("Last Name", validators = [Required()])
    birth_day = TextField("Birth Day")
    birth_day = TextField("Birth Month")
    birth_day = TextField("Birth Year")
    sex = TextField("Sex", validators = [Required()])

class ListSettingsForm(Form):
    name = TextField("Name", validators = [Required()])

class EmailSettingsForm(Form):
    name = TextField("Name", validators = [Required()])

