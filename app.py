from flask import Flask, render_template, request
from additional import get_data

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def base_page():
    repository_list = []
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        if get_data(username) == "ERROR":
            error = 'Error,please, write correct GitHubName'
        else:
            repository_list.extend(get_data(username))
    return render_template('home.html', resitory_date=repository_list, eror=error)


if __name__ == '__main__':
    app.run()
