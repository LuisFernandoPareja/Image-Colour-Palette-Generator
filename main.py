from flask import Flask, render_template, request, send_from_directory, url_for
from flask_bootstrap import Bootstrap5
from flask_uploads import UploadSet, IMAGES, configure_uploads
from ColorGenerator import gen_color_palette
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some_random_string'
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

Bootstrap5(app)


class UploadForm(FlaskForm):
    image = FileField(
        validators=[
            FileAllowed(photos, 'Only images allowed'),
            FileRequired('File field should not be empty')
        ]
    )
    submit = SubmitField('Upload')


@app.route('/uploads/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)


@app.route('/', methods=['GET', 'POST'])
def home():
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.image.data)
        file_url = url_for('get_file', filename=filename)
    else:
        file_url = None
    return render_template('index.html', form=form, file_url=file_url)




if __name__ == '__main__':
    app.run(debug=True)
