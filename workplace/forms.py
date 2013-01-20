from flask.ext.wtf import Email, Form, PasswordField, Required, TextField

class AccountGeneralForm(Form):
    username = TextField("Username", validators = [Required()])

class AccountEmailsForm(Form):
    email = TextField("Email", validators = [Required(), Email()])

class AccountListsForm(Form):
    list_name = TextField("Name", validators = [Required()])

class AccountPasswordForm(Form):
	current_password = PasswordField("Current Password", validators = [Required()])
	password = PasswordField("New Password", validators = [Required()])
	password2 = PasswordField("Re-enter New Password", validators = [Required()])

class AccountProfileForm(Form):
    first_name = TextField("First Name", validators = [Required()])
    last_name = TextField("Last Name", validators = [Required()])
    birth_day = TextField("Birth Day")
    birth_month = TextField("Birth Month")
    birth_year = TextField("Birth Year")
    sex = TextField("Sex")

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

