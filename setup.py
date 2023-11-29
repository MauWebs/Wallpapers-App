from distutils.core import setup

import py2exe

setup(
    windows=[{'script': 'app.py'}],
    options={
        'py2exe': {
            'includes': ['PIL'],
        },
    },
    # data_files=[
    #     ('img', ['img/img1.jpg', 'img/img2.jpg', 'img/img3.jpg', 'img/img4.jpg']),
    # ],
)