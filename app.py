from flask import Flask, render_template, request
import requests
import traceback

app = Flask(__name__)

# configure below credentials 
JENKINS_URL = "http://localhost:8080/job/generic_build/buildWithParameters"
JENKINS_USER_TOKEN = "1181329ec4cf7d254b73408e7ed8b22d4f"
JENKINS_USER = "shariq"

@app.route('/')
def main():
    return render_template('app.html')

@app.route('/send', methods=['POST'])
def send():
    try:
        if request.method == 'POST':
            github_url = request.form['github_url']
            github_branch = request.form['github_branch']
            github_credentials = request.form['github_credentials']
            build_tool = request.form['build_tool']
            doSonarScan = request.form.getlist('sonar_scan')
            doEC2deploy = request.form.getlist('ec2_deploy')
    except e:
        traceback.print_exc()
        result = status_code = -1
    try:
        my_data = {'Github_URL' : github_url, 'Github_Branch': github_branch, 'Github_Credentials' : github_credentials, 'Perform_Sonar_Scan' : doSonarScan , 'Perform_EC2_deployment' : doEC2deploy, 'build_tool' : build_tool}    
        response = requests.post(JENKINS_URL, auth=(JENKINS_USER, JENKINS_USER_TOKEN), data = my_data)
    except e:
        traceback.print_exc()
        result = status_code = -1
        
    result = response.status_code
    
    if (result is '201'):
        result = "Job has been triggered successfully"
    else:
        result = "Error Encountered!! Please check logs"
    return render_template('app.html',result=result)

if __name__ == ' __main__':
    app.run(debug=True,host='0.0.0.0')
