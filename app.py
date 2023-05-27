from flask import Flask

FAI=Flask(__name__)

@FAI.route('/sample/<name>')
def sample(name):
    return f'Hii,how r u...{name}'


FAI.run(debug=True)
'''FAI.run(debug=True,port=5001,host='192.168.111.81')'''

    