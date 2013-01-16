from flask.ext.wtf import Form, TextField, Required,  \
    PasswordField

class SignupForm(Form):
    email = TextField("Email", validators = [Required()])
    password = PasswordField("password", validators = [Required()])
    password2 = PasswordField("password2", validators = [Required()])
    first_name = TextField("First Name", validators = [Required()])
    last_name = TextField("Last Name", validators = [Required()])
    username = TextField("User Name", validators = [Required()])

class LoginForm(Form):
    email = TextField("Email", validators = [Required()])
    password = PasswordField("password", validators = [Required()])

