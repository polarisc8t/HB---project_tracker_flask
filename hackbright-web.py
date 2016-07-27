from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    trifecta = hackbright.get_grades_by_github(github)
    import pdb; pdb.set_trace()
    print "TRIFECTA %s" % trifecta
    return render_template("student_info.html",
                           first=first,
                           last=last,
                           trifecta=trifecta)


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/add_new_student")
def add_new_student():
    """Show form for searching for a new student."""

    return render_template("add_new_student.html")

@app.route("/new_student", methods=['POST'])
def make_new_student():
    """Show information about a new student."""

    first = request.form.get('first')
    last = request.form.get('last')
    github = request.form.get('github')
    hackbright.make_new_student(first, last, github)
    html = render_template("new_student.html",
                           first=first,
                           last=last,
                           github=github)
    
    return html


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
