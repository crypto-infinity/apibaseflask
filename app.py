#api.py

import os

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    #renders the index.html file
    return render_template('index.html')


@app.get('/swagger')
def swagger():
    return jsonify({
        'swagger': '2.0',
        'info': {
            'title': 'API',
            'version': '1.0'
        },
        'paths': {
            '/': {
                'get': {
                    'responses': {
                        '200': {
                            'description': 'Success'
                        }
                    }
                }
            }
        }
    })


@app.post('/test')
def test():
    try:
        with open('test.txt', 'w') as f:
            f.write('Hello, World!')
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

    return jsonify({
        'success': True
    })