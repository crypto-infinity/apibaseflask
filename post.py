# POST Methods

from flask import Flask, request, jsonify
from app import app


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