from flask import Flask, jsonify, request
import settings
app=Flask(__name__)
@app.route("/",methods=['GET','POST'])
def index():
    if request.method=='GET':
#getting the url argument
        url = request.args.get('url')
        remote_addr = request.remote_addr
        ip = settings.IP
        TERM_PROGRAM = settings.TERM_PROGRAM
        return jsonify({'Success':"This is a GET API method",'ip':ip,'url': url,'remote_addr':remote_addr,'TERM_PROGRAM':TERM_PROGRAM})
    else:
        return jsonify({'Error':"This is a GET API method"})
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=9007)