from flask.ext.wtf import Form, TextField, Required,  \
    PasswordField, Email

class SignupForm(Form):
    email = TextField("Email", validators = [Required(), Email()])
    password = PasswordField("password", validators = [Required()])
    password2 = PasswordField("password confirmation", validators = [Required()])
    first_name = TextField("First Name", validators = [Required()])
    last_name = TextField("Last Name", validators = [Required()])
    username = TextField("User Name", validators = [Required()])

class LoginForm(Form):
    email = TextField("Email", validators = [Required(), Email()])
    password = PasswordField("password", validators = [Required()])

