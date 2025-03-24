# GET Methods

from flask import Flask, request, jsonify
from app import app

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