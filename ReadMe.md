1. Install python, flask, requests modules to run the application

2. In jenkins, create a pipeline job and configure below parameters and enable "This project is parameterized option"
a. Github_URL
b. Github_Credentials
c. Project_file_location
d. Checkbox for Sonar Scan
e. Checkbox for Ansible deployment
f. Branch for github checkout

3. Install sonar-scanner plugin in Jenkins and configure it from Manage Jenkins --> Configure System

4. Configure Credentials 
a. For Github checkout in Jenkins
b. For Sonarscan in Jenkins
c. Access key and secret keys for EC2 ins Jenkins 

5. Configure Sonarscan url in Jenkins configuration

6. Update JENKINS_URL parameter in app.py to point to Jenkins job

7. Create token for user and update in app.py

8. Create keys in aws

9. Create token in sonar

10. Artifacts:
https://github.com/acenawaz01/Hello-World
https://github.com/acenawaz01/CICD-Solution.git

11. Start flask app by running below command from location where app.py is located. Ensure you have installed python and flask
flask run
