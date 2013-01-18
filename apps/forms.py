from flask.ext.wtf import Email, Form, PasswordField, Required, TextField

class SignupForm(Form):
    first_name = TextField("First Name", validators = [Required()])
    last_name = TextField("Last Name", validators = [Required()])
    email = TextField("Email", validators = [Required(), Email()])
    email2 = TextField("Re-enter Email", validators = [Required(), Email()])
    password = PasswordField("Password", validators = [Required()])
    password2 = PasswordField("Re-enter Password", validators = [Required()])

class LoginForm(Form):
    email = TextField("Email", validators = [Required(), Email()])
    password = PasswordField("password", validators = [Required()])


class ForgotForm(Form):
    email = TextField("Email", validators = [Required(), Email()])

