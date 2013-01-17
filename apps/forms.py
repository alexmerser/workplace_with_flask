from flask.ext.wtf import Form, TextField, Required,  \
    PasswordField, Email

class SignupForm(Form):
    email = TextField("Email", validators = [Required(), Email()])
    email2 = TextField("Re-enter Email", validators = [Required(), Email()])
    password = PasswordField("Password", validators = [Required()])
    password2 = PasswordField("Re-enter Password", validators = [Required()])
    first_name = TextField("First Name", validators = [Required()])
    last_name = TextField("Last Name", validators = [Required()])

class LoginForm(Form):
    email = TextField("Email", validators = [Required(), Email()])
    password = PasswordField("password", validators = [Required()])


class ForgotForm(Form):
    email = TextField("Email", validators = [Required(), Email()])

